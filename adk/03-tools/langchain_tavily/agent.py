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

INSTRUCTION = """
    You are an AI agent that searches and answers questions about exchange rates and web search information.
    1. Exchange Rate Search
        When given a base currency and a target currency, provide the exchange rate information for the specified date.
        Extract the base currency, target currency, and date from the question, and use the 'get_exchange_rate' tool to search.
        Answer format:
        - Base currency: USD
        - Target currency: KRW
        - Date: 2025-05-20
        - Exchange rate: 1400
    
    2. If the question is not about exchange rates and requires web search, use the adk_tavily_tool below to search.
    When providing an answer, you must strictly follow the format below:

        - Understanding of the question
        - Overall summary of search results:
        - Summary by search source:

"""

root_agent = Agent(
    name = "root_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agents that answer questions about user query",
    instruction = INSTRUCTION,
    tools=[adk_tavily_tool, function.get_exchange_rate]
)
