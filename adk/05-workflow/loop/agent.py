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

from dotenv import load_dotenv
from google.adk.agents import SequentialAgent
from google.adk.agents import LoopAgent

from .sub_agent import research_agent
from .sub_agent import critic_agent
from .sub_agent import refine_agent
from .sub_agent import conclusion_agent

load_dotenv()

def build_agent():
    """
    LoopAgent와 SequentialAgent를 활용하여 워크플로우 에이전트를 생성하고 설정합니다.

    이 함수는 반복적인 비평/개선 루프를 위한 loop agent와, 연구-비평/개선-결론의 순차적 흐름을 담당하는 sequential agent를 정의합니다.
    최종적으로 연구 → 비평/개선 루프 → 결론의 다단계 워크플로우를 실행하는 에이전트를 반환합니다.

    반환값:
        SequentialAgent: 다단계 워크플로우를 통해 사용자 질의를 처리할 수 있는 설정된 에이전트
    """

    critics_loop = LoopAgent(
        name="critics_loop",
        sub_agents=[
            critic_agent,
            refine_agent,
        ],
        max_iterations=3  # 비평/개선 루프 최대 반복 횟수
    )

    confirmation_agent = SequentialAgent(
        name="confirmation_agent",
        sub_agents=[
            research_agent, 
            critics_loop,
            conclusion_agent
        ],
        description="research_agent와 critics_loop를 순차적으로 실행하는 에이전트입니다.",
    )
    return confirmation_agent

root_agent = build_agent()
