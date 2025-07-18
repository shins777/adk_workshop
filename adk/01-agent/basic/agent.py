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

load_dotenv()

def build_agent() -> Agent:
    """
    사용자 질문에 답변하는 기본 Agent 인스턴스를 생성하고 설정합니다.
    이 함수는 환경 변수를 불러오고, 에이전트의 지시문 템플릿을 정의하며,
    이름, 모델, 설명, 지시문을 포함해 Agent를 초기화합니다.
    이 에이전트는 사용자 질문에 간결하고 구조화된 답변을 제공하도록 설계되었습니다.

    반환값:
        Agent: 사용자 질문을 처리할 준비가 된 설정된 Agent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변하는 AI 에이전트입니다.
        답변을 제공할 때는 질문에 대한 이해를 설명하고 간결하고 명확하게 응답하세요:
    """

    agent = Agent(
        name = "basic_agent",
        model = os.getenv("MODEL"),
        description = "사용자 질의에 대한 질문에 답변하는 에이전트",
        instruction = INSTRUCTION,
    )
    return agent

root_agent = build_agent()
