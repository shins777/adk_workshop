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
    Creates and configures an MCPToolset for exchange rate operations using Model Context Protocol (MCP).
    This function sets up an MCPToolset instance that connects to a custom exchange rate server using the specified command and arguments. This allows the agent to query exchange rate information.

    Returns:
        MCPToolset: A configured MCPToolset instance for exchange rate operations.
    """

    mcp_toolset = MCPToolset(
            connection_params=StdioServerParameters(
                command='python3', 
                args=[
                      "-m"
                      "local_server.exchange_rate"
                      ],
            )
    )    
            
            
    return mcp_toolset

INSTRUCTION = """
    You are an agent that provides answers to user questions.
    When a user asks a exchange rates to the specific currency, you must use the 'exchange_rate_tool' to provide an answer based on the results.
"""

exchange_rate_tool = mcp_toolset()

root_agent = LlmAgent(
    name = "Exchange_Rate_Agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agents that answer exchange rates",
    instruction = INSTRUCTION,
    tools=[exchange_rate_tool],
)
