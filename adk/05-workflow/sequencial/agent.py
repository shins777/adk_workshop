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

from .sub_agent import positive_critic, negative_critic, review_critic

load_dotenv()

def build_agent():
    """
    다단계 워크플로우를 위한 SequentialAgent를 생성하고 설정합니다.

    이 함수는 'pipeline_agent'라는 이름의 SequentialAgent를 초기화하며,
    positive_critic, negative_critic, review_critic 서브 에이전트를 순차적으로 실행합니다.
    에이전트는 각 서브 에이전트를 순서대로 실행하여 비평 및 리뷰가 구조적으로 이루어지도록 설계되어 있습니다.

    반환값:
        SequentialAgent: 순차 워크플로우를 통해 사용자 질의를 처리할 수 있는 설정된 에이전트
    """

    pipeline_agent = SequentialAgent(
        name="pipeline_agent",
        sub_agents=[positive_critic, negative_critic, review_critic],
        description="positive_critic, negative_critic, review_critic을 순차적으로 실행하는 에이전트입니다.",
    )
    return pipeline_agent

root_agent = build_agent()
