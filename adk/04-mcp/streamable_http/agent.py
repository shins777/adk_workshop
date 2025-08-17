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
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams

load_dotenv()

def mcp_streamable_http_tool():
    """
    Create and configure an MCPToolset that connects to a remote MCP Streamable HTTP server.

    This helper constructs an MCPToolset using StreamableHTTPConnectionParams with the
    provided service URL. The returned toolset can be used by an LLM agent to call
    remote MCP tools exposed by the Streamable HTTP server.

    Returns:
        MCPToolset: a configured MCPToolset instance using Streamable HTTP connection parameters.
    """

    mcp_toolset = MCPToolset(
        connection_params=StreamableHTTPConnectionParams(
            url="https://mcp-streamable-http-721521243942.us-central1.run.app/mcp/",
        ),
    )
            
    return mcp_toolset

INSTRUCTION = """
    You are an agent that provides answers to user questions.
    When a user asks a question related to exchange rate, you must use the 'get_exchange_rate' to provide an answer based on the results.
"""

get_exchange_rate = mcp_streamable_http_tool()

root_agent = LlmAgent(
    name = "get_exchange_rate_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agents that answer questions about user query",
    instruction = INSTRUCTION,
    tools=[get_exchange_rate],
)
