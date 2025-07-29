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
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

load_dotenv()

def mcp_toolset():
    """
    Model Context Protocol(MCP)를 통해 환율 작업을 위한 MCPToolset을 생성하고 구성합니다.

    이 함수는 지정된 명령어와 인자를 사용해 커스텀 환율 서버에 연결하는 MCPToolset 인스턴스를 설정합니다.
    이를 통해 에이전트가 환율 정보를 조회할 수 있습니다.

    반환값:
        MCPToolset: 환율 작업을 위한 구성된 MCPToolset 인스턴스
    """

    mcp_toolset = MCPToolset(
            connection_params=StdioServerParameters(
                command='python3', 
                args=[
                      "-m"
                      "server_exchange_rate.exchange_rate_server"
                      ],
            )
    )    
            
            
    return mcp_toolset

def build_agent() -> LlmAgent:
    """
    환율 정보 조회를 위한 MCPToolset이 포함된 LlmAgent 인스턴스를 생성하고 구성합니다.

    이 함수는 에이전트의 안내 템플릿을 정의하고, 이름, 모델, 설명, 안내문,
    MCP를 통한 환율 정보 조회 도구를 포함하여 LlmAgent를 초기화합니다.
    이 에이전트는 사용자의 질문에 답변하고, 'exchange_rate_tool'을 활용해 최신 환율 정보를 제공합니다.

    반환값:
        LlmAgent: MCPToolset을 활용해 환율 질의를 처리할 수 있는 구성된 LlmAgent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        사용자가 질문을 입력하면, 해당 질문에 대해 'exchange_rate_tool'을 사용해 결과를 바탕으로 답변을 제공해야 합니다.

        참고: 답변 시 반드시 사용자가 질문에 사용한 언어와 동일한 언어로 답변해야 합니다.
    """

    exchange_rate_tool = mcp_toolset()

    agent = LlmAgent(
        name = "search_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
        tools=[exchange_rate_tool],
    )
    return agent

root_agent = build_agent()