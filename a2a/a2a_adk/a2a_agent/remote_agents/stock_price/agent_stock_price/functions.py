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

import requests
import os

async def get_stock_price(symbol: str)->dict:
    """
    Retrieves the stock price for the given symbol.
    Uses the Alphavantage API (https://www.alphavantage.co/) to fetch stock price information for the symbol.

    Args:
        symbol: Stock symbol name
    Returns:
        dict: Dictionary containing stock price information
    """

    

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={os.getenv('STOCK_API_KEY')}"
    response = requests.get(url)

    print(f"## Stock price response: {response.json()}")

    return response.json()

