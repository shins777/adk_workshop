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

from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.tools import TavilySearchResults

from . import function

load_dotenv()

# Instantiate the LangChain tool
tavily_tool_instance = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True,
)

# Wrap it with LangchainTool for ADK
adk_tavily_tool = LangchainTool(tool=tavily_tool_instance)

def build_agent():
    """
    Creates and configures an Agent instance with LangChain Tavily search and exchange rate tools.

    This function defines the agent's instruction template and initializes the Agent with a name,
    model, description, instruction, and tools for both web search (using the Tavily search tool)
    and exchange rate lookup. The agent is designed to answer user queries by calling the appropriate
    tool and formatting the response according to the specified structure.

    Returns:
        Agent: A configured Agent instance ready to process web search and exchange rate queries.
    """

    INSTRUCTION = """ 

        You are an AI Agent that searches for exchange rate information and stock information and answers.
        
        1. Search for exchange rate information
            If you tell me the base exchange rate and the target exchange rate, I will tell you the exchange rate information based on the given date.
            Please find the target exchange rate, target exchange rate, and date information from the given question and pass them to the 'get_exchange_rate' tool to search.
            The answer format is as follows.
            - Base exchange rate: USD
            - Target exchange rate: KRW
            - Date: 2025-05-20
            - Exchange rate information: 1400
        
        2. If you need to search the web rather than ask a question about exchange rates, please use the adk_tavily_tool tool below to search.
        
        When you provide an answer, you have to follow the below format exactly:

        1. Question: 
        2. Reference sources: 
        3. Answer: 

        Note : When answering, Must be sure to use the same language the user used when asking the question. 

    """

    agent = Agent(
        name = "root_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
        tools=[adk_tavily_tool, function.get_exchange_rate]
    )
    return agent

root_agent = build_agent()