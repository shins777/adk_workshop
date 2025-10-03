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

import random

from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.tools.example_tool import ExampleTool
from google.genai import types
from google.adk.tools.agent_tool import AgentTool

from agent_client.sub_agent import company_info_agent, market_info_agent

import os

agent_exchange_rate = RemoteA2aAgent(
    name="agent_exchange_rate",
    description="An agent specialized in checking exchange rate via an external API. It can efficiently determine the exchange rate between two currencies.",
    agent_card=(
        f"http://localhost:8001/a2a/agent_exchange_rate{AGENT_CARD_WELL_KNOWN_PATH}"

    ),
)

agent_stock_price = RemoteA2aAgent(
    name="agent_stock_price",
    description="An agent specialized in checking stock prices via an external API. It can efficiently determine the current stock price of a given company symbol.",
    agent_card=(
        f"http://localhost:8002/a2a/agent_stock_price{AGENT_CARD_WELL_KNOWN_PATH}"

    ),
)

company_info_tool = AgentTool(agent=company_info_agent)
market_info_tool = AgentTool(agent=market_info_agent)

root_agent = Agent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name="root_agent",
    instruction="""
      You are a helpful assistant that can provide information about economy market situation, companie's information, check exchange rates between currencies, and get stock prices by delegating tasks to specialized sub-agents. you have access to the following sub-agents:

      1. If the user asks company's stock price, first use the **company_info_tool** and second, delegate to the sub agent; **agent_stock_price**, then combine the results to provide a comprehensive answer.
      2. If the user asks exchange rate, first use the **market_info_tool** and second, delegate to the sub agent;**agent_exchange_rate**, then combine the results to provide a comprehensive answer.
      3. If the user asks company's information, use the **company_info_tool** only.
      4. If the user asks something else, provide a concise and clear answer based on your knowledge.
      
      Always clarify the results before proceeding.
      Be sure to use the tools of the sub-agents to get accurate and up-to-date information.

    """,
    global_instruction=(
        """
        You should be very accurate with the latest information, Always clarify the results before proceeding. 
        Be sure to use the tools of the sub-agents to get accurate and up-to-date information.
        """
    ),

    sub_agents=[agent_exchange_rate,
                agent_stock_price],

    tools = [company_info_tool,
             market_info_tool],

    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)
