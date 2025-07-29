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
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

load_dotenv()

def mcp_toolset(target_folder_path: str):
    """
    Model Context Protocol(MCP)를 통해 파일 시스템 작업을 위한 MCPToolset을 생성하고 구성합니다.

    이 함수는 주어진 대상 폴더 경로를 사용하여 MCPToolset 인스턴스를 설정하며,
    에이전트가 MCP 서버를 통해 파일 시스템과 상호작용할 수 있도록 합니다.
    
    npx와 @modelcontextprotocol/server-filesystem 패키지를 사용해 서버에 연결하도록 구성됩니다.

    인자:
        target_folder_path (str): 파일 시스템 작업을 위한 대상 폴더의 절대 경로

    반환값:
        MCPToolset: 파일 관리 작업을 위한 구성된 MCPToolset 인스턴스
    """

    file_system_toolset = MCPToolset(
                connection_params=StdioServerParameters(
                    command='npx',
                    args=[
                        "-y",  # Argument for npx to auto-confirm install
                        "@modelcontextprotocol/server-filesystem",
                        # IMPORTANT: This MUST be an ABSOLUTE path to a folder the
                        # npx process can access.
                        # Replace with a valid absolute path on your system.
                        # For example: "/Users/youruser/accessible_mcp_files"
                        # or use a dynamically constructed absolute path:
                        os.path.abspath(target_folder_path),
                    ],
                ),
                # Optional: Filter which tools from the MCP server are exposed
                # tool_filter=['list_directory', 'read_file']
            )
    return file_system_toolset

def build_agent() -> LlmAgent:
    """
    파일 시스템 관리를 위한 MCPToolset이 포함된 LlmAgent 인스턴스를 생성하고 구성합니다.

    이 함수는 에이전트의 안내 템플릿을 정의하고, 이름, 모델, 설명, 안내문,
    MCP를 통한 지정 폴더 파일 관리 도구를 포함하여 LlmAgent를 초기화합니다.
    이 에이전트는 사용자가 파일을 관리하고 파일 시스템 도구셋을 활용해 질문에 답변할 수 있도록 설계되었습니다.

    반환값:
        LlmAgent: MCPToolset을 활용해 파일 관리 질의를 처리할 수 있는 구성된 LlmAgent 인스턴스
    """

    INSTRUCTION = """
        당신은 주어진 폴더 내 파일 관리를 도와주는 에이전트입니다.
        사용자가 질문을 입력하면, 해당 질문에 대해 'file_system_toolset'을 사용해 결과를 바탕으로 답변을 제공해야 합니다.

        참고: 답변 시 반드시 사용자가 질문에 사용한 언어와 동일한 언어로 답변해야 합니다.
    """

    target_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/")
    file_system_toolset = mcp_toolset(target_folder_path=target_folder_path)

    agent = LlmAgent(
        name = "search_agent",
        model = os.getenv("GOOGLE_GENAI_MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
        tools=[file_system_toolset],
    )
    return agent

root_agent = build_agent()