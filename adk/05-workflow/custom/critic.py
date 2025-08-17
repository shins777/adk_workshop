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

from google.adk.agents import LlmAgent, BaseAgent, SequentialAgent
from google.adk.agents.invocation_context import InvocationContext

from google.adk.events import Event
from google.adk.agents import SequentialAgent

class CriticAgent(BaseAgent):
    """
    하위 에이전트를 사용하여 다단계 비평 워크플로를 조율하는 맞춤형 에이전트입니다.

    CriticAgent는 positive_critic_agent, negative_critic_agent,
    review_critic_agent라는 세 가지 LlmAgent 하위 에이전트를 조정합니다. 먼저 긍정 비평, 부정 비평, 마지막으로
    리뷰 비평을 실행하여 각 단계의 이벤트를 생성합니다. 에이전트는 필요한 출력 조건이 충족되지 않으면(예: 상태에 키워드 누락) 워크플로를 조기에 중단할 수 있습니다. 이를 통해
    사용자 입력 또는 생성된 콘텐츠에 대한 복잡하고 조건부적인 다단계 평가 및 검토가 가능합니다.

    Attributes:
        positive_critic_agent (LlmAgent): 긍정적인 비판을 생성하는 에이전트.
        negative_critic_agent (LlmAgent): 부정적인 비판을 생성하는 에이전트.
        review_critic_agent (LlmAgent): 종합된 비평을 검토하는 에이전트.
        sequential_agent (SequentialAgent): 워크플로를 관리하기 위한 내부 순차 에이전트입니다.

    Methods:
        _run_async_impl(ctx): 각 단계에서 이벤트를 생성하여 비판 워크플로를 비동기적으로 실행합니다.
        
    """

    positive_critic_agent: LlmAgent
    negative_critic_agent: LlmAgent
    review_critic_agent: LlmAgent

    sequential_agent: SequentialAgent

    # model_config allows setting Pydantic configurations if needed, e.g., arbitrary_types_allowed
    model_config = {"arbitrary_types_allowed": True}

    def __init__(
        self,
        name: str,
        positive_critic_agent: LlmAgent,
        negative_critic_agent: LlmAgent,
        review_critic_agent: LlmAgent,
    ):
        sequential_agent = SequentialAgent(
            name="PostProcessing", sub_agents=[positive_critic_agent, negative_critic_agent]
        )

        sub_agents_list = [
            sequential_agent,
            review_critic_agent,
        ]

        super().__init__(
            name=name,
            positive_critic_agent=positive_critic_agent,
            negative_critic_agent=negative_critic_agent,
            review_critic_agent=review_critic_agent,
            sequential_agent=sequential_agent,
            sub_agents=sub_agents_list,
        )

    @override
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:

        """
        다단계 비평 워크플로를 비동기적으로 실행합니다.

        이 메서드는 긍정적 비평 에이전트, 부정적 비평 에이전트, 그리고 리뷰 비평 에이전트를 순차적으로 실행하여
        각 단계의 이벤트를 생성합니다. 필요한 출력 조건이 충족되지 않으면 (예: 단계 후 상태에 키워드가 누락된 경우) 워크플로가 조기에 중단됩니다.
        이를 통해 사용자 입력 또는 생성된 콘텐츠에 대한 조건부 단계적 평가 및 검토가 가능합니다.

        Args:
        ctx(InvocationContext): 세션 및 상태 정보가 포함된 호출 컨텍스트입니다.

        Return:
        이벤트: 워크플로 실행 중 각 하위 에이전트에서 생성된 이벤트입니다.
        """

        #-----------[positive_critic_agent]--------------
        print(f"[{self.name}] Running positive_critic_agent...")
        async for event in self.positive_critic_agent.run_async(ctx):

            print(f"[{self.name}] Event from positive_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event # yield an event and move on to the next step

        # 처리결과를 보고 positive_critic_output에서 "images" 키워드가 없으면 워크플로우를 중단합니다.
        # 특정 조건에 부합하지 않으면 워크플로우를 중단합니다
        # if "images" not in ctx.session.state["positive_critic_output"].lower():
        #     print(f"[{self.name}] Failed to generate answer since no mention about images . Aborting workflow.")
        #     return # Stop processing if positive critic is failed

        #-----------[negative_critic_agent]--------------
        print(f"[{self.name}] Running negative_critic_agent...")
        async for event in self.negative_critic_agent.run_async(ctx):
            print(f"[{self.name}] Event from negative_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event # yield an event and move on to the next step

        # 처리결과를 보고 negative_critic_output에서 "social" 키워드가 없으면 워크플로우를 중단합니다.
        # 특정 조건에 부합하지 않으면 워크플로우를 중단합니다.
        # if "social" not in ctx.session.state["negative_critic_output"].lower():
        #     print(f"[{self.name}] Failed to generate answer since no mention about social issues . Aborting workflow.")
        #     return # Stop processing if negative critic is failed

        #-----------[review_critic_agent]--------------
        print(f"[{self.name}] Running review_critic_agent")
        async for event in self.review_critic_agent.run_async(ctx):
            print(f"[{self.name}] Event from review_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event
