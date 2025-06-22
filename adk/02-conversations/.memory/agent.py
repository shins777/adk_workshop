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
from google.adk.tools import load_memory # Tool to query memory

load_dotenv()

#--------------------------------[build_search_agent]----------------------------------

def build_search_agent() -> Agent:
    """
    Google Search 도구 지원이 포함된 Agent 인스턴스를 생성하고 구성합니다.
    이 에이전트는 google_search 도구를 사용하여 사용자의 질문에 대해 Google 검색을 수행하고,

    반환값:
        Agent: Google Search를 활용해 질의에 답변하는 Agent 인스턴스
    """

    SEARCH_INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        사용자가 질문을 입력하면, 해당 질문에 대해 Google 검색(tool:google_search)을 수행하고 결과를 바탕으로 답변을 제공해야 합니다. 전체적으로 답변은 간결하고 명확해야 하며, 사용자가 질문한 언어로 작성되어야 합니다.
        
    """

    search_agent = Agent(
        name = "search_agent",
        model = os.getenv("MODEL"),
        description = "사용자 질의에 답변하는 에이전트",
        instruction = SEARCH_INSTRUCTION,
        tools=[google_search],
    )
    return search_agent

#--------------------------------[build_recall_agent]----------------------------------

def build_recall_agent() -> Agent:
    """
    메모리 리콜 기능이 포함된 Agent 인스턴스를 생성하고 구성합니다.
    만일 사용자가 이전 대화에서 답변을 요구하면, 이 에이전트는 'load_memory' 도구를 사용하여 저장된 메모리를 기반으로 사용자에게 답변을 해야 합니다.

    반환값:
        Agent: 메모리에서 정보를 검색하여 질의에 답변하도록 구성된 Agent 인스턴스
    """

    RECALL_INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다. 
        만일 사용자가 이전 대화 내용에서 답변을 요구하면, 이 에이전트는 'load_memory' 도구를 사용하여 저장된 메모리를 기반으로 사용자에게 답변을 해야 합니다.
        """

    recall_agent = Agent(
        name = "recall_agent",
        model = os.getenv("MODEL"),
        description = "메모리에서 정보를 검색하여 사용자 질문에 답변하는 에이전트",
        instruction = RECALL_INSTRUCTION,
        tools=[load_memory],
    )
    return recall_agent

search_agent = build_search_agent()
recall_agent = build_recall_agent()
