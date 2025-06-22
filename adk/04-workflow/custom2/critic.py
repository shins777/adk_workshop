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

from typing import AsyncGenerator
from typing_extensions import override

from google.adk.agents import LlmAgent, BaseAgent
from google.adk.agents.invocation_context import InvocationContext

from google.adk.events import Event

class CriticAgent(BaseAgent):
    """
    긍정 및 부정 비평 서브 에이전트를 오케스트레이션하는 커스텀 에이전트입니다.

    이 에이전트는 인보케이션 컨텍스트를 받아 긍정 비평 에이전트와 부정 비평 에이전트를 순차적으로 실행합니다.
    각 서브 에이전트가 실행 중 생성하는 모든 이벤트를 yield합니다.

    속성:
        positive_critic_agent (LlmAgent): 긍정 비평을 담당하는 서브 에이전트
        negative_critic_agent (LlmAgent): 부정 비평을 담당하는 서브 에이전트
    """

    positive_critic_agent: LlmAgent
    negative_critic_agent: LlmAgent

    # model_config는 필요 시 Pydantic 설정(예: arbitrary_types_allowed 등)을 지정할 수 있습니다.
    model_config = {"arbitrary_types_allowed": True}

    def __init__(
        self,
        name: str,
        positive_critic_agent: LlmAgent,
        negative_critic_agent: LlmAgent,
    ):
        # 비평용 서브 에이전트로 CriticAgent를 초기화합니다.
        super().__init__(
            name=name,
            positive_critic_agent=positive_critic_agent,
            negative_critic_agent=negative_critic_agent,
        )

    @override
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        """
        긍정 및 부정 비평 서브 에이전트를 순차적으로 비동기 실행하며, 각 단계의 이벤트를 yield합니다.

        이 메서드는 먼저 주어진 인보케이션 컨텍스트로 긍정 비평 에이전트를 실행하고,
        각 이벤트를 yield합니다. 긍정 비평이 끝나면 동일한 컨텍스트로 부정 비평 에이전트를 실행하여
        그 이벤트도 yield합니다. CriticAgent는 이처럼 2단계 비평 프로세스를 오케스트레이션하며,
        모든 중간 및 최종 이벤트를 호출자에게 스트리밍합니다.

        인자:
            ctx (InvocationContext): 사용자 입력 및 실행 상태를 담은 인보케이션 컨텍스트

        Yields:
            Event: 긍정 및 부정 비평 서브 에이전트가 실행 중 생성한 이벤트
        """
        #-----------[positive_critic_agent]--------------
        print(f"[{self.name}] Running positive_critic_agent...")
        async for event in self.positive_critic_agent.run_async(ctx):
            print(f"[{self.name}] Event from positive_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event # 이벤트를 yield하고 다음 단계로 진행

        #-----------[negative_critic_agent]--------------
        print(f"[{self.name}] Running negative_critic_agent...")
        async for event in self.negative_critic_agent.run_async(ctx):
            print(f"[{self.name}] Event from negative_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event # 이벤트를 yield하고 다음 단계로 진행

