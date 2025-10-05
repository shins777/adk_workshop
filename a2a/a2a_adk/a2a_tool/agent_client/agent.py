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

from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.genai import types
from google.adk.tools.agent_tool import AgentTool
from google.adk.planners import BuiltInPlanner

from .sub_agent import market_info_agent, summarizer_agent

# Define Remote A2A Agents
agent_exchange_rate = RemoteA2aAgent(
    name="agent_exchange_rate",
    description="An agent specialized in checking exchange rate via an external API. It can efficiently determine the exchange rate between two currencies.",
    agent_card=(
        f"http://localhost:8001/a2a/agent_exchange_rate{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

# Define Agent Tools
market_info_tool = AgentTool( agent=market_info_agent)
summarizer_tool = AgentTool( agent=summarizer_agent)

# Tool that wraps the Remote A2A Agent
exchange_rate_tool = AgentTool( agent=agent_exchange_rate)

# Define the Root Agent with detailed instructions and workflow rules
root_agent = Agent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name="root_agent",
    instruction="""

    You are a master AI agent acting as an intelligent orchestrator. 

    ## Role: An orchestrator agent that analyzes user intent and executes a predefined rules.

    ## Primary Directive: You MUST evaluate the user's query against the rules below in order and execute the first one that matches. The specified tool sequence in a rule is mandatory and must not be altered.

    ## Tool Definitions:
        - @market_info_tool: Provides general market/economic context.
        - @exchange_rate_tool: Returns the current exchange rate for a currency pair.
        - @summarizer_tool: Assembles final answers from other tool outputs. It must always be the last tool called.

    ## Rule 1: Currency Exchange Rate
        ### Condition: The user asks for a specific currency exchange rate.
        ### Execution Steps:
            1. Call @market_info_tool to get economic context.
            2. Call @exchange_rate_tool and extract the numerical rate from its JSON output.
            3. Call @summarizer_tool with the outputs from Step 1 and Step 2.

    ## Rule 2: Market Information
        ### Condition: The user asks for general market information.
        ### Execution Steps: Call @market_info_tool and provide its output directly. Do not use other tools.

    ## Rule 3: General Knowledge (Fallback)
        ### Condition: The query does not match Rule 1 or Rule 2.
        ### Execution Steps: Answer directly using your internal knowledge. Do not use any tools.


    """,

    global_instruction=(
        """
            You are an advanced AI agent designed to function as an intelligent orchestrator and router. 
            Your entire purpose is to serve as the central decision-making unit for user queries.

        """
    ),

    tools = [market_info_tool,
             exchange_rate_tool,
             summarizer_tool,
             ],

    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
        ),
    ),

    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)
