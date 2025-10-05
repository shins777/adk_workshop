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

from google.adk import Agent
from google.genai import types
from google.adk.tools.agent_tool import AgentTool

from .sub_agents import company_info_agent, summarizer_agent
from .functions import get_stock_price

# Make the sub-agents into tools
company_info_tool = AgentTool( agent=company_info_agent)
summarizer_tool = AgentTool( agent=summarizer_agent)

# Define root agent as an orchestrator
root_agent = Agent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name='company_stock_price_agent',
    description="An agent specialized in providing company's information and stock prices",
    instruction="""

        You are an orchestrator agent that provides comprehensive information about a company, including its stock price and latest news.
        
        ## Goal : Provide the stock price and latest news for a given company symbol.

        ## Execution Steps:
            1. Get the stock price using the @get_stock_price tool.
            2. Find the latest news using the @company_info_tool.
            3. MANDATORY: Call the @summarizer_tool with the outputs from both Step 1 and Step 2 to generate the final answer.
        
        ## Constraint: Do not use any pre-trained knowledge. Rely only on the tool outputs.

    """,
    
    tools=[
        get_stock_price,
        company_info_tool, 
        summarizer_tool        
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
