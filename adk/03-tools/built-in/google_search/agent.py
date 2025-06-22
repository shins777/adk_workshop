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
        You are an agent who provides answers to users' questions.
        When a user enters a question, you should perform a Google search(tool:google_search) for that question and provide an answer based on the results.
        When you provide an answer, you have to follow the below format exactly:

        1. Question: 
        2. Search sources: 
        3. Answer: 

        Note : When answering, Must be sure to use the same language the user used when asking the question. 
                
    """

    agent = Agent(
        name = "search_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
        tools=[google_search],
    )
    return agent

root_agent = build_agent()