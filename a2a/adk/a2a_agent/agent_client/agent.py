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

from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.genai import types

import os

agent_stock_price = RemoteA2aAgent(
    name="agent_stock_price",
    description="An agent specialized in checking stock prices via an external API. It can efficiently determine the current stock price of a given company symbol.",
    agent_card=(
        f"http://localhost:8001/a2a/agent_stock_price{AGENT_CARD_WELL_KNOWN_PATH}"

    ),
)

root_agent = Agent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name="root_agent",
    instruction="""

    You are a master AI agent acting as an intelligent orchestrator. 
    Your primary goal is to analyze user queries and efficiently route them to the correct tool or sub-agent to generate a comprehensive and accurate answer.

    ## Tools and Sub-Agents Definition
    -   `@agent_stock_price`: A remote sub agent that takes the given company symbol and returns the current stock price of the company.
    
    ## Core Principles
    - You MUST NOT use the information you have been trained on to answer the query if it matches a following rule. 
    - Instead, you MUST rely solely on real-time data fetched through the defined tools and sub-agents.

    ## Workflow and Routing Rules
        
    **Rule 1: Currency Exchange Rate Inquiry**
    -   **Condition:** IF the user's primary intent is to ask for a currency exchange rate.
    -   **Execution Plan Steps:**
        You MUST call the `@agent_stock_price` sub agent to take the given company symbol and returns the current stock price of the company.

    **Rule 2: General Knowledge Inquiry (Fallback)**
    -   **Condition:** IF the query does not match any of the rules above.
    -   **Execution Plan:**
        1.  You MUST answer directly using your own internal knowledge.
        
    **Overall Output Format:** Provide a concise and clear answer.

    """,

    global_instruction=(
        """
            You are an advanced AI agent designed to function as an intelligent orchestrator and router. 
            Your entire purpose is to serve as the central decision-making unit for user queries.

        """
    ),

    sub_agents=[agent_stock_price],

    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)
