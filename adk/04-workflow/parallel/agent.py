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
from google.adk.agents import ParallelAgent

from .sub_agent import positive_critic, negative_critic, review_critic

load_dotenv()

def build_agent():
    """
    ParallelAgent와 SequentialAgent를 활용하여 워크플로우 에이전트를 생성하고 설정합니다.

    이 함수는 긍정/부정 비평을 병렬로 실행하는 parallel agent와,
    병렬 연구 에이전트 실행 후 리뷰 비평을 순차적으로 실행하는 sequential agent를 정의합니다.
    최종적으로 여러 연구 에이전트를 병렬로 실행한 뒤, 리뷰 단계를 거치는 워크플로우를 수행합니다.

    반환값:
        SequentialAgent: 병렬 및 순차 워크플로우를 통해 사용자 질의를 처리할 수 있는 설정된 에이전트
    """

    parallel_research_agent = ParallelAgent(
        name="parallel_research_agent",
        sub_agents=[positive_critic, negative_critic],
        description="여러 연구 에이전트를 병렬로 실행하여 정보를 수집하는 에이전트입니다."
    )

    pipeline_agent = SequentialAgent(
        name="pipeline_agent",
        sub_agents=[parallel_research_agent, review_critic],
        description="parallel_research_agent와 review_critic을 순차적으로 실행하는 에이전트입니다.",
    )
    return pipeline_agent

root_agent = build_agent()
