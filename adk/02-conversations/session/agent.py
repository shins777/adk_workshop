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
    Google Search 도구 지원이 포함된 Agent 인스턴스를 생성하고 구성합니다.
    이 에이전트는 사용자의 질문에 대해 Google 검색을 수행하고,
    질문, 출처 정보, 답변이 포함된 구조화된 형식으로 답변을 제공합니다.

    반환값:
        Agent: 사용자 질의 처리가 가능한 구성된 Agent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        사용자가 질문을 입력하면, 해당 질문에 대해 Google 검색(tool:google_search)을 수행하고 결과를 바탕으로 답변을 제공해야 합니다. 전체적으로 답변은 간결하고 명확해야 하며, 사용자가 질문한 언어로 작성되어야 합니다.
        
    """

    search_agent = Agent(
        name = "search_agent",
        model = os.getenv("GOOGLE_GENAI_MODEL"),
        description = "사용자 질문에 답변하는 에이전트",
        instruction = INSTRUCTION,
        tools=[google_search],
    )
    return search_agent

root_agent = build_agent()