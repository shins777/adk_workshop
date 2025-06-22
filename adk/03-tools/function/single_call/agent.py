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

        You are an AI Agent that searches for exchange rate information and stock information and answers.
        
        1. Search for exchange rate information
            If you tell me the base exchange rate and the target exchange rate, I will tell you the exchange rate information based on the given date.
            Please find the target exchange rate, target exchange rate, and date information from the given question and pass them to the 'get_exchange_rate' tool to search.
            The answer format is as follows.
            - Base exchange rate: USD
            - Target exchange rate: KRW
            - Date: 2025-05-20
            - Exchange rate information: 1400

        Note : When answering, Must be sure to use the same language the user used when asking the question. 

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