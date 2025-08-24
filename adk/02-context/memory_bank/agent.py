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
from google.adk.tools import preload_memory_tool 
from google.adk.tools import google_search

load_dotenv()

#--------------------------------[build_search_agent]----------------------------------

SEARCH_INSTRUCTION = """
    당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
    사용자가 질문을 입력하면 Google 검색(도구:google_search)을 수행하고, 그 결과를 바탕으로 답변을 제공해야 합니다.
    
"""

search_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 질의에 답변하는 에이전트",
    instruction = SEARCH_INSTRUCTION,
    # tools=[google_search],
    tools=[preload_memory_tool.PreloadMemoryTool()],
)

#--------------------------------[build_recall_agent]----------------------------------

RECALL_INSTRUCTION = """
    당신은 사용자의 질문에 답변을 제공하는 에이전트입니다. 
    만일 사용자가 이전 대화 내용에서 답변을 요구하면, 당신은 등록된 도구를 통해서 저장된 메모리를 기반으로 사용자에게 답변을 해야 합니다.
    """

recall_agent = Agent(
    name = "recall_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "메모리에서 정보를 검색하여 사용자 질문에 답변하는 에이전트",
    instruction = RECALL_INSTRUCTION,
    tools=[preload_memory_tool.PreloadMemoryTool()],
)
