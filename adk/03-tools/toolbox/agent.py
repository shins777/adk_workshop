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
from toolbox_core import ToolboxSyncClient

load_dotenv()

def get_toolbox():
    """
    ToolboxSyncClient 인스턴스를 생성하고 설정합니다.

    이 함수는 환경 변수를 불러오고, ToolboxSyncClient를 초기화합니다.
    이 클라이언트는 툴박스와의 동기화를 관리하는 데 사용됩니다.

    반환값:
        ToolboxSyncClient: 툴박스와의 동기화를 관리할 준비가 된 클라이언트 인스턴스
    """
    toolbox = ToolboxSyncClient(    
        os.getenv("TOOLBOX_SYNC_CLIENT"),
        
    )

    tool_set = toolbox.load_toolset('my_bq_toolset')
    print(f"Toolbox set: {tool_set}")
    
    tools = toolbox.load_tool('query_bbc'),
    print(f"Toolbox tools: {tools}")
    
    return tools


def build_agent() -> Agent:
    """
    Agent 인스턴스를 생성하고 설정합니다.

    반환값:
        Agent: 사용자 질의를 처리할 준비가 된 설정된 Agent 인스턴스
    """


    tools = get_toolbox()

    INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        사용자가 질문을 입력하면, 관련된 tool을 사용하여 답변을 생성해야 합니다.
        전체적으로 답변은 간결하고 명확해야 하며, 사용자가 질문한 언어로 작성되어야 합니다.

        답변을 제공할 때는 반드시 아래 형식을 정확히 따라야 합니다. 

        1. 질문에 대한 이해
        2. 검색 결과 전체 요약: 
        3. 검색 소스 별 요약:

    """

    agent = Agent(
        name = "search_agent",
        model = os.getenv("GOOGLE_GENAI_MODEL"),
        description = "사용자 질의에 답변하는 에이전트",
        instruction = INSTRUCTION,
        tools=tools,
    )
    return agent

root_agent = build_agent()