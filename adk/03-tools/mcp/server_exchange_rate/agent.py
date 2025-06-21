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

def mcp_toolset():
    """
    Creates and configures an MCPToolset for exchange rate operations via Model Context Protocol (MCP).

    This function sets up an MCPToolset instance that connects to a custom exchange rate server
    using the specified command and arguments. The toolset enables the agent to interact with
    the exchange rate server for retrieving exchange rate information.

    Returns:
        MCPToolset: A configured MCPToolset instance for exchange rate tasks.
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
    Creates and configures an LlmAgent instance with an MCPToolset for exchange rate retrieval.

    This function defines the agent's instruction template and initializes the LlmAgent with a name,
    model, description, instruction, and a tool for retrieving exchange rate information via MCP.
    The agent is designed to answer user questions and use the 'exchange_rate_tool' to provide up-to-date information.

    Returns:
        LlmAgent: A configured LlmAgent instance ready to process exchange rate queries using MCPToolset.
    """
    # ...existing code...

    INSTRUCTION = """
        You are an agent who provides answers to users' questions.
        When a user enters a question, you should perform a 'exchange_rate_tool' for that question and provide an answer based on the results.

        Note: When answering, Must be sure to use the same language the user used when asking the question. 
                
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