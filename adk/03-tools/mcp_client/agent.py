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
    Creates and configures an MCPToolset for file system operations via Model Context Protocol (MCP).
    This function sets up an MCPToolset instance using the given target folder path,
    allowing the agent to interact with the file system through an MCP server.
    The server is configured to connect using npx and the @modelcontextprotocol/server-filesystem package.

    Args:
        target_folder_path (str): Absolute path to the target folder for file system operations

    Returns:
        MCPToolset: Configured MCPToolset instance for file management operations
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


INSTRUCTION = """
    You are an agent that helps manage files within a given folder.
    When a user enters a question, you must use 'file_system_toolset' to provide an answer based on the results.
"""

target_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/")
file_system_toolset = mcp_toolset(target_folder_path=target_folder_path)

root_agent = LlmAgent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agents that answer questions about user query",
    instruction = INSTRUCTION,
    tools=[file_system_toolset],
)