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
    여러 함수 도구를 지원하는 Agent 인스턴스를 생성하고 구성합니다.

    이 함수는 환경 변수를 로드하고, 에이전트의 안내 템플릿을 정의하며,
    이름, 모델, 설명, 안내문, 환율 및 주가 정보를 조회하는 도구를 포함하여 Agent를 초기화합니다.
    이 에이전트는 적절한 함수 도구를 호출하여 사용자 질의에 답변하고, 응답을 지정된 형식에 맞게 제공합니다.

    반환값:
        Agent: 환율 및 주식 정보 질의 처리가 가능한 구성된 Agent 인스턴스
    """

    INSTRUCTION = """

        당신은 환율 정보와 주식 정보를 검색하여 답변하는 AI 에이전트입니다.

        1. 환율 정보 검색
            기준 환율과 대상 환율을 알려주면, 주어진 날짜를 기준으로 환율 정보를 안내합니다.
            질문에서 기준 환율, 대상 환율, 날짜 정보를 추출하여 'get_exchange_rate' 도구에 전달해 검색하세요.
            답변 형식은 다음과 같습니다.
            - 기준 환율: USD
            - 대상 환율: KRW
            - 날짜: 2025-05-20
            - 환율 정보: 1400

        2. 주식 정보 검색
            주식 정보는 주어진 심볼을 기준으로 오늘 날짜의 주가를 안내합니다.
            회사명에서 심볼을 추출하여 'get_stock_price' 도구에 전달해 검색하세요.
            답변 형식은 다음과 같습니다.
            - 주식 정보: Google
            - 날짜: 2025-05-20
            - 주가: $200

        참고: 답변 시 반드시 사용자가 질문에 사용한 언어와 동일한 언어로 답변해야 합니다.

    """

    agent = Agent(
        name = "basic_agent",
        model = os.getenv("MODEL"),
        description = "사용자 질의에 답변하는 에이전트",
        instruction = INSTRUCTION,
        tools=[function.get_exchange_rate, function.get_stock_price],

    )

    return agent

root_agent = build_agent()