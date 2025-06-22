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

from . import function

load_dotenv()

def build_agent() -> Agent:
    """
    환율 조회용 함수형 툴이 포함된 Agent 인스턴스를 생성하고 설정합니다.

    이 함수는 환경 변수를 불러오고, 에이전트의 지시문 템플릿을 정의하며,
    이름, 모델, 설명, 지시문, 환율 정보 조회 툴을 포함해 Agent를 초기화합니다.
    이 에이전트는 적절한 함수형 툴을 호출해 사용자 질의에 답변하고, 결과를 포맷에 맞게 반환하도록 설계되었습니다.

    반환값:
        Agent: 환율 정보 질의를 처리할 준비가 된 설정된 Agent 인스턴스
    """

    INSTRUCTION = """

        당신은 환율 정보를 검색하여 답변하는 AI 에이전트입니다.
        
        1. 환율 정보 검색
            기준 환율과 대상 환율을 알려주면, 주어진 날짜를 기준으로 환율 정보를 안내합니다.
            질문에서 기준 환율, 대상 환율, 날짜 정보를 추출하여 'get_exchange_rate' 도구에 전달해 검색하세요.
            답변 형식은 다음과 같습니다.
            - 기준 환율: USD
            - 대상 환율: KRW
            - 날짜: 2025-05-20
            - 환율 정보: 1400

        참고: 답변 시 반드시 사용자가 질문에 사용한 언어와 동일한 언어로 답변해야 합니다.

    """

    agent = Agent(
        name = "basic_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
        tools=[function.get_exchange_rate],

    )
    return agent

root_agent = build_agent()