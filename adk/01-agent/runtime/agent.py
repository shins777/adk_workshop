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
from google.adk.agents import Agent

from .sub_agent import positive_critic, negative_critic

load_dotenv()

def build_agent() -> Agent:
    """
    비평 작업을 위한 서브 에이전트를 포함하는 루트 Agent 인스턴스를 생성하고 설정 함수
    - 환경 변수를 불러오고, 에이전트의 지시문 템플릿을 정의.
    - 긍정 및 부정 비평을 위한 서브 에이전트 설정.
    - 사용자 요청에 따라 특정 비평 작업을 위임.

    반환값:
        Agent: 사용자 질의를 처리할 준비가 된 서브 에이전트가 포함된 설정된 Agent 인스턴스 반환.
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        사용자의 질문에 따라 다음과 같이 서브 에이전트를 사용하여 답변을 제공해야 합니다.

            1. 사용자가 긍정적인 비평을 요청하면, positive_critic 에이전트를 사용하여 긍정적인 비평을 작성하세요.
            2. 사용자가 부정적인 비평을 요청하면, negative_critic 에이전트를 사용하여 부정적인 비평을 작성하세요.

        참고: 답변 시 반드시 사용자가 질문한 언어와 동일한 언어로 답변해야 합니다.
        
    """

    agent = Agent(
        name = "root_agent",
        model = os.getenv("MODEL"),
        description = "사용자 질의에 대한 질문에 답변하는 에이전트",
        instruction = INSTRUCTION,
        sub_agents = [positive_critic, negative_critic],
    )        
    return agent

root_agent = build_agent()