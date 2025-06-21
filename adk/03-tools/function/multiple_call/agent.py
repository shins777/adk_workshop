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

from . import function

load_dotenv()

def build_agent() -> Agent:
    """
    Creates and configures an Agent instance with multiple function tool support.

    This function loads environment variables, defines the agent's instruction template,
    and initializes the Agent with a name, model, description, instruction, and tools for
    retrieving exchange rate and stock price information. The agent is designed to answer
    user queries by calling the appropriate function tool and formatting the response accordingly.

    Returns:
        Agent: A configured Agent instance ready to process exchange rate and stock information queries.
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

        2. Search for stock information
            For stock information, tell me the stock price as of today based on the given symbol.
            Please find the symbol for the given company name and pass it to the 'get_stock_price' tool to search.
            The answer format is as follows.
            - Stock information: Google
            - Date: 2025-05-20
            - Stock price: $200

        Note : When answering, Must be sure to use the same language the user used when asking the question. 

                    
    """

    agent = Agent(
        name = "basic_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
        tools=[function.get_exchange_rate, function.get_stock_price],

    )

    return agent

root_agent = build_agent()