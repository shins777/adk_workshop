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

import os
from dotenv import load_dotenv
from google.adk.agents import SequentialAgent
from google.adk.agents import Agent

from .sub_agent import positive_critic, negative_critic, review_critic

load_dotenv()

#--------------------------------[build_agent]----------------------------------

def build_agent() -> Agent:
    """
    여러 서브 에이전트로 구성된 SequentialAgent를 생성하고 설정합니다.

    이 함수는 'pipeline_agent'라는 SequentialAgent를 초기화하며,
    positive_critic, negative_critic, review_critic 서브 에이전트들을 순차적으로 실행합니다.
    각 서브 에이전트는 전체 작업의 특정 부분을 담당하며,
    SequentialAgent가 이들의 실행을 순서대로 조율합니다.

    반환값:
        Agent: 사용자 질의를 처리할 준비가 된 SequentialAgent 인스턴스
    """

    # SequentialAgent does not requrire instruction because each sub agent has their own instruction. 
    agent = SequentialAgent(
        name="pipeline_agent",
        sub_agents=[positive_critic, negative_critic, review_critic],
        description="Executes a sequence of positive_critic, negative_critic, and review_critic.",
    )

    return agent

root_agent = build_agent()
