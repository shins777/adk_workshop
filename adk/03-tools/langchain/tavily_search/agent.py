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

from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.tools import TavilySearchResults

from . import function

load_dotenv()

# Instantiate the LangChain tool
tavily_tool_instance = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True,
)

# Wrap it with LangchainTool for ADK
adk_tavily_tool = LangchainTool(tool=tavily_tool_instance)

def build_agent():
    """
    LangChain Tavily 검색 및 환율 조회 도구가 포함된 Agent 인스턴스를 생성하고 구성합니다.

    이 함수는 에이전트의 안내 템플릿을 정의하고, 이름, 모델, 설명, 안내문,
    웹 검색(Tavily 검색 도구) 및 환율 조회 도구를 포함하여 Agent를 초기화합니다.
    이 에이전트는 적절한 도구를 호출하여 사용자 질의에 답변하고, 지정된 구조에 맞게 응답을 포맷합니다.

    반환값:
        Agent: 웹 검색 및 환율 질의 처리가 가능한 구성된 Agent 인스턴스
    """

    INSTRUCTION = """

        당신은 환율 정보와 웹 검색 정보를 검색하여 답변하는 AI 에이전트입니다.
        
        1. 환율 정보 검색
            기준 환율과 대상 환율을 알려주면, 주어진 날짜를 기준으로 환율 정보를 안내합니다.
            질문에서 기준 환율, 대상 환율, 날짜 정보를 추출하여 'get_exchange_rate' 도구에 전달해 검색하세요.
            답변 형식은 다음과 같습니다.
            - 기준 환율: USD
            - 대상 환율: KRW
            - 날짜: 2025-05-20
            - 환율 정보: 1400
        
        2. 환율 질문이 아닌 웹 검색이 필요하다면 아래 adk_tavily_tool 도구를 사용해 검색하세요.
        
        답변을 제공할 때는 반드시 아래 형식을 정확히 따라야 합니다:

        1. 질문: 
        2. 참고 출처: 
        3. 답변: 

        참고: 답변 시 반드시 사용자가 질문에 사용한 언어와 동일한 언어로 답변해야 합니다.

    """

    agent = Agent(
        name = "root_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
        tools=[adk_tavily_tool, function.get_exchange_rate]
    )
    return agent

root_agent = build_agent()