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
    서브 에이전트를 활용해 다단계 비평 워크플로우를 오케스트레이션하는 커스텀 에이전트입니다.

    CriticAgent는 세 개의 LlmAgent 서브 에이전트(positive_critic_agent, negative_critic_agent, review_critic_agent)를 조율합니다.
    먼저 긍정 비평, 그 다음 부정 비평, 마지막으로 종합 리뷰를 순차적으로 실행하며 각 단계의 이벤트를 yield합니다.
    만약 필수 출력 조건(예: 상태에 특정 키워드가 없음)이 충족되지 않으면 워크플로우를 조기에 중단할 수 있습니다.
    이를 통해 사용자 입력 또는 생성된 콘텐츠에 대한 복합적이고 조건부, 다단계 평가 및 리뷰가 가능합니다.

    속성:
        positive_critic_agent (LlmAgent): 긍정 비평을 생성하는 에이전트
        negative_critic_agent (LlmAgent): 부정 비평을 생성하는 에이전트
        review_critic_agent (LlmAgent): 긍정/부정 비평을 종합 리뷰하는 에이전트
        sequential_agent (SequentialAgent): 워크플로우 관리를 위한 내부 시퀀스 에이전트

    메서드:
        _run_async_impl(ctx): 비동기로 비평 워크플로우를 실행하며 각 단계별 이벤트를 yield
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
        다단계 비평 워크플로우를 비동기로 실행합니다.

        이 메서드는 긍정 비평, 부정 비평, 종합 리뷰 에이전트를 순차적으로 실행하며,
        각 단계의 이벤트를 yield합니다. 만약 필수 출력 조건(예: 단계 후 상태에 특정 키워드가 없음)이 충족되지 않으면
        워크플로우를 조기에 중단합니다. 이를 통해 사용자 입력 또는 생성된 콘텐츠에 대한 조건부, 단계별 평가 및 리뷰가 가능합니다.

        인자:
            ctx (InvocationContext): 세션 및 상태 정보를 담은 인보케이션 컨텍스트

        Yields:
            Event: 워크플로우 실행 중 각 서브 에이전트가 생성한 이벤트
        """

        #-----------[positive_critic_agent]--------------
        print(f"[{self.name}] Running positive_critic_agent...")
        async for event in self.positive_critic_agent.run_async(ctx):
            print(f"[{self.name}] Event from positive_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event # 이벤트를 yield하고 다음 단계로 진행

        if "images" not in ctx.session.state["positive_critic_output"].lower():
            print(f"[{self.name}] Failed to generate answer since no mention about images . Aborting workflow.")
            return # positive critic 실패 시 처리 중단

        #-----------[negative_critic_agent]--------------
        print(f"[{self.name}] Running negative_critic_agent...")
        async for event in self.negative_critic_agent.run_async(ctx):
            print(f"[{self.name}] Event from negative_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event # 이벤트를 yield하고 다음 단계로 진행

        if "social" not in ctx.session.state["negative_critic_output"].lower():
            print(f"[{self.name}] Failed to generate answer since no mention about social issues . Aborting workflow.")
            return # negative critic 실패 시 처리 중단

        #-----------[review_critic_agent]--------------
        print(f"[{self.name}] Running review_critic_agent")
        async for event in self.review_critic_agent.run_async(ctx):
            print(f"[{self.name}] Event from review_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event
