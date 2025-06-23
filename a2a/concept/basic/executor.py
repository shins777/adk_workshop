# Copyright 2025 Forusone(forusone777@gmail.com)
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

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message
from a2a.utils.errors import ServerError
from a2a.types import UnsupportedOperationError

class EchoAgent:
    """
    사용자의 질의를 대문자로 변환하여 그대로 반환하는 간단한 에이전트입니다.

    EchoAgent는 비동기 메서드 `invoke`만을 제공하며, 입력된 질의를 대문자로 변환한 후 포맷팅된 문자열로 반환합니다.
    이 클래스는 에이전트가 입력을 처리하고 응답하는 방식을 시연하거나 테스트할 때 사용됩니다.

    메서드:
        invoke(query: str) -> str: 입력 질의를 대문자로 변환하여 비동기로 반환합니다.
    """

    async def invoke(self, query: str) -> str:
        return f"\n###  🤖 EchoAgent : {query.upper()}"

class EchoAgentExecutor(AgentExecutor):
    """
    사용자의 질의를 EchoAgent에 위임하고, 응답을 이벤트 큐에 넣는 에이전트 실행기입니다.

    EchoAgentExecutor는 EchoAgent의 생명주기를 관리하며, 실행 컨텍스트와 이벤트 큐를 처리합니다.
    사용자 입력을 받아 에이전트를 호출해 응답을 생성하고, 그 결과를 이벤트로 큐에 넣어 후속 처리가 가능하게 합니다.
    또한, 지원하지 않는 작업에 대해 오류를 발생시키는 cancel 메서드도 제공합니다.

    메서드:
        execute(context, event_queue): 사용자 질의를 처리하고, 에이전트를 호출해 응답을 이벤트 큐에 넣습니다.
        cancel(context, event_queue): 취소 작업이 지원되지 않음을 알리는 오류를 발생시킵니다.
    """

    def __init__(self):
        self.agent = EchoAgent()

    async def execute(self,
                      context: RequestContext,
                      event_queue: EventQueue,) -> None:
    
        print(f"### Before invoking Agent context : {context}")
        
        # https://google-a2a.github.io/A2A/sdk/python/#a2a.server.agent_execution.RequestContext
        message = context.message
        query = context.get_user_input()

        print(f"### Message : {message}")
        print(f"### User's query : {query}")
    
        result = await self.agent.invoke(query=query)        

        print(f"### After invoking Agent result : {result}")

        # Put the result to event_eqeue to send the results to the client. 
        event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, 
                     context: RequestContext, 
                     event_queue: EventQueue) -> None:
        
        raise ServerError(error=UnsupportedOperationError())

