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


from google.adk import Agent
from google.genai import types
import requests
import os

import random

from google.adk import Agent
from google.adk.tools.tool_context import ToolContext
from google.genai import types

#--------------------------[get_stock_price]-----------------------------
async def get_stock_price(symbol: str)->dict:
    """
    Retrieves the stock price for the given symbol.
    Uses the Alphavantage API (https://www.alphavantage.co/) to fetch stock price information for the symbol.

    Args:
        symbol: Stock symbol name
    Returns:
        dict: Dictionary containing stock price information
    """

    import requests

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={os.getenv('STOCK_API_KEY')}"
    
    response = requests.get(url)
    
    return response.json()


root_agent = Agent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name='agent_stock_price',
    description='An agent specialized in checking stock prices via an external API. It can efficiently determine the current stock price of a given company symbol.',
    instruction="""
      You should reponse to the stock price corresponding to the given company symbol.
      When checking the stock price of the company, call the get_stock_price tool with the company's symbol.
      You should not rely on the previous trained information.
    """,
    tools=[
        get_stock_price,
    ],
    # planner=BuiltInPlanner(
    #     thinking_config=types.ThinkingConfig(
    #         include_thoughts=True,
    #     ),
    # ),
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)
