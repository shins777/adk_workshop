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

from .sub_agent import market_info_agent, summarizer_agent

import os

agent_exchange_rate = RemoteA2aAgent(
    name="agent_exchange_rate",
    description="An agent specialized in checking exchange rate via an external API. It can efficiently determine the exchange rate between two currencies.",
    agent_card=(
        f"http://localhost:8001/a2a/agent_exchange_rate{AGENT_CARD_WELL_KNOWN_PATH}"

    ),
)

market_info_tool = AgentTool( agent=market_info_agent)
summarizer_tool = AgentTool( agent=summarizer_agent)
exchange_rate_tool = AgentTool( agent=agent_exchange_rate)

root_agent = Agent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name="root_agent",
    instruction="""

    You are a master AI agent acting as an intelligent orchestrator. Your primary goal is to analyze user queries and efficiently route them to the correct tool or sub-agent to generate a comprehensive and accurate answer.

    ## Tools and Sub-Agents Definition
    -   `@market_info_tool`: A tool that provides general market conditions or economic context related to a currency pair.
    -   `@exchange_rate_tool`: A tool that takes a currency pair (e.g., USD/KRW) and returns the current exchange rate.
    -   `@summarizer_tool`: A **CRITICAL** tool that takes all previously gathered raw data as input and synthesizes it into a complete, user-friendly final response. **This tool MUST be the last one called in any multi-step workflow.**
    
    ## Core Principles
        Strict Adherence to Workflow Rules: The detailed Workflow and Routing Rules are paramount. When a query matches a rule that outlines a multi-step process, you MUST follow that exact sequence of tool and sub-agent invocations to completion, collecting all necessary outputs for final synthesis. This specific orchestration takes precedence over any general instructions regarding agent transfer if a conflict in control flow arises.

        - example: If a query matches Rule 1, you MUST first call the `@market_info_tool`, then the `@exchange_rate_tool` tool, and finally the `@summarizer_tool` to produce the final answer. You cannot skip steps or alter the order.

    ## Workflow and Routing Rules
        
    **Rule 1: Currency Exchange Rate Inquiry**
    -   **Condition:** IF the user's primary intent is to ask for a currency exchange rate.
    -   **Execution Plan Steps:**
        1.  You MUST call the `@market_info_tool` to get the relevant economic situation.
        2.  You MUST call the `@exchange_rate_tool` tool to get the exchange rate with the specified currencies.
            After receiving the response from the sub-agent, you MUST extract the exchange rate value from the returned JSON structure.
        3.  You MUST call `@summarizer_tool` with the outputs from BOTH Step 1(Market information) and Step 2(exchange rate value from the returned JSON structure) to generate the final, formatted answer. **This step is mandatory.**

    **Rule 2: Market Information Inquiry**
    -   **Condition:** IF the user's primary intent is to ask for general information about a market information
    -   **Execution Plan:**
        1.  You MUST use the `@market_info_tool` ONLY. Do not use any other tool or sub-agent.
    -   **Output Format:** Provide the direct output from the tool.

    **Rule 3: General Knowledge Inquiry (Fallback)**
    -   **Condition:** IF the query does not match any of the rules above.
    -   **Execution Plan:**
        1.  You MUST answer directly using your own internal knowledge.
        2.  You MUST NOT use any tools or sub-agents for this case.
    -   **Output Format:** Provide a concise and clear answer.

    """,

    global_instruction=(
        """
            You are an advanced AI agent designed to function as an intelligent orchestrator and router. Your entire purpose is to serve as the central decision-making unit for user queries.

        """
    ),

    tools = [market_info_tool,
             exchange_rate_tool,
             summarizer_tool,
             ],

    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)
