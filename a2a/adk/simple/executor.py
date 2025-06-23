# Copyright 2025 Forusone(shins777@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk import Runner
from google.genai import types
from collections.abc import AsyncGenerator
from google.adk.events import Event

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message
from a2a.utils.errors import ServerError
from a2a.server.tasks import TaskUpdater

from a2a.types import (
    AgentCard,
    FilePart,
    FileWithBytes,
    FileWithUri,
    Part,
    TaskState,
    TextPart,
    UnsupportedOperationError,
)

from .convert import convert_a2a_parts_to_genai
from .convert import convert_genai_parts_to_a2a

class ADKAgentExecutor(AgentExecutor):
    """
    Google ADK 에이전트를 A2A 서버 프레임워크와 연동하는 에이전트 실행기입니다.

    ADKAgentExecutor는 Google ADK 에이전트의 실행을 관리하며, 세션 관리, A2A/GenAI 메시지 변환,
    이벤트 큐 업데이트를 담당합니다. 사용자 입력을 처리하고, 에이전트를 비동기로 호출하며,
    작업 상태 및 산출물을 이벤트 큐에 업데이트합니다. 또한 지원하지 않는 작업 취소 메서드도 제공합니다.

    메서드:
        execute(context, event_queue): 사용자 질의를 처리하고 ADK 에이전트를 실행, 이벤트 큐를 갱신합니다.
        cancel(context, event_queue): 취소 미지원 오류를 발생시킵니다.
    """

    def __init__(self, runner: Runner, agent_card: AgentCard):

        self.runner = runner
        self.agent_card = agent_card

    def run_agent( self, 
                    session_id, 
                    user_id, 
                    new_message: types.Content) -> AsyncGenerator[Event]:

        """
        주어진 세션 및 사용자 정보로 ADK 에이전트를 비동기로 실행합니다.

        이 메서드는 에이전트의 비동기 실행(run_async)을 호출하며, 세션 ID, 사용자 ID,
        새 메시지 콘텐츠를 전달합니다. 실행 중 생성되는 이벤트(중간/최종 응답 등)를 yield합니다.

        인자:
            session_id (str): 대화 세션 식별자
            user_id (str): 사용자 식별자
            new_message (types.Content): 에이전트가 처리할 사용자 메시지 콘텐츠

        Yields:
            Event: 실행 중 생성되는 이벤트
        """

        return self.runner.run_async(
            session_id=session_id, user_id=user_id, new_message=new_message
        )
    
    async def execute(self,
                      context: RequestContext,
                      event_queue: EventQueue,) -> None:
    
        """
        사용자 질의에 대해 ADK 에이전트를 실행하고, 이벤트 큐를 갱신합니다.

        이 메서드는 요청 컨텍스트에서 사용자 입력을 처리하고, 작업 상태를 관리하며,
        에이전트용 메시지를 빌드하고, 세션을 보장한 뒤, 에이전트를 비동기로 실행합니다.
        중간 및 최종 응답, 산출물, 상태 업데이트를 이벤트 큐에 반영하여 스트리밍/비스트리밍 워크플로우 모두 지원합니다.

        인자:
            context (RequestContext): 사용자 입력 및 작업 정보를 담은 요청 컨텍스트
            event_queue (EventQueue): 에이전트 응답 및 상태 업데이트를 게시할 이벤트 큐

        반환값:
            None
        """

        print(f"### [ADKAgentExecutor|execute] Before invoking Agent context : {context}")
        print(f"### [ADKAgentExecutor|execute] Current task : {context.current_task}")
        print(f"### [ADKAgentExecutor|execute] Message : {context.message}")
        print(f"### [ADKAgentExecutor|execute] User's query : {context.get_user_input()}")
        print(f"### [ADKAgentExecutor|execute] Context ID : {context.message.contextId}")
        
        # Get session id from context. 
        session_id = context.message.contextId

        # Run the agent until either complete or the task is suspended.
        # https://google-a2a.github.io/A2A/sdk/python/#a2a.server.tasks.TaskUpdater
            # Helper class for agents to publish updates to a task's event queue.
            # Simplifies the process of creating and enqueueing standard task events.

        task_updater = TaskUpdater(event_queue, context.task_id, context.context_id)
        
        # Marks the task as submitted and publishes a status update.
        if not context.current_task:
            task_updater.submit()
        
        # Marks the task as working and publishes a status update.
        task_updater.start_work()

        # Message building.
        new_message = types.UserContent(
            parts=convert_a2a_parts_to_genai(context.message.parts),
        )

        # Get or create session from session_id(derived from context.message.contextId.)
        
        session = await self.runner.session_service.get_session(
            app_name=self.runner.app_name, user_id='self', session_id=session_id
        ) or await self.runner.session_service.create_session(
            app_name=self.runner.app_name, user_id='self', session_id=session_id
        )

        # Run Agent
        async for event in self.run_agent(session_id=session.id, 
                                         user_id=session.user_id, 
                                         new_message=new_message):
            
            if event.is_final_response():
                # Change content's part to fit to a2a part format. 
                parts = convert_genai_parts_to_a2a(event.content.parts)
                print('Yielding final response: %s', parts)
                task_updater.add_artifact(parts)
                task_updater.complete()

                break
            if not event.get_function_calls():
                print('Yielding update response')
                task_updater.update_status(
                    TaskState.working,
                    message=task_updater.new_agent_message(
                        convert_genai_parts_to_a2a(event.content.parts),
                    ),
                )
            else:
                print('Skipping event')

        print(f"### After invoking Agent")

    async def cancel(self, 
                     context: RequestContext, 
                     event_queue: EventQueue) -> None:
        
        raise ServerError(error=UnsupportedOperationError())

