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
from google.adk.tools import google_search

load_dotenv()

def build_agent() -> Agent:
    """
    Google Search 툴이 포함된 Agent 인스턴스를 생성하고 설정합니다.

    이 함수는 환경 변수를 불러오고, 에이전트의 지시문 템플릿을 설정하며,
    이름, 모델, 설명, 지시문, Google Search 툴을 포함해 Agent를 초기화합니다.
    이 에이전트는 자체 지식과 검색 기능을 활용해 사용자 질문에 답변하도록 설계되었습니다.

    반환값:
        Agent: 사용자 질의를 처리할 준비가 된 설정된 Agent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        사용자가 질문을 입력하면, 해당 질문에 대해 Google 검색(tool:google_search)을 수행하고 결과를 바탕으로 답변을 제공해야 합니다. 전체적으로 답변은 간결하고 명확해야 하며, 사용자가 질문한 언어로 작성되어야 합니다.

        답변을 제공할 때는 반드시 아래 형식을 정확히 따라야 합니다. 

        1. 질문에 대한 이해
        2. 검색 결과 전체 요약: 
        3. 검색 소스 별 요약:

    """

    agent = Agent(
        name = "search_agent",
        model = os.getenv("MODEL"),
        description = "사용자 질의에 답변하는 에이전트",
        instruction = INSTRUCTION,
        tools=[google_search],
    )
    return agent

root_agent = build_agent()