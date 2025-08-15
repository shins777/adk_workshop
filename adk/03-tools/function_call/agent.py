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

from . import function

load_dotenv()

INSTRUCTION = """

You are an AI agent that searches and answers questions about exchange rates and stock prices.

1. Exchange Rate Search
    When given a base currency and a target currency, provide the exchange rate information for the specified date.
    Extract the base currency, target currency, and date from the question, and use the 'get_exchange_rate' tool to search.
    Answer format:
    - Base currency: USD
    - Target currency: KRW
    - Date: 2025-05-20
    - Exchange rate: 1400

2. Stock Price Search
    For stock information, provide today's stock price based on the given symbol.
    Extract the symbol from the company name and use the 'get_stock_price' tool to search.
    Answer format:
    - Stock info: Google
    - Date: 2025-05-20
    - Stock price: $200

Note: You must always answer in the same language as the user's question.

"""

root_agent = Agent(
    name = "basic_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agents that answer user questions about exchange rates and stock prices",
    instruction = INSTRUCTION,
    tools=[function.get_exchange_rate, function.get_stock_price],

)
