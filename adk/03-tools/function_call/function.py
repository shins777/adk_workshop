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

#--------------------------[get_exchange_rate]-----------------------------
def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "KRW",
    currency_date: str = "latest", )->dict:
    """
    Retrieves the exchange rate between two currencies for a specified date.
    Uses the Frankfurter API (https://api.frankfurter.app/) to fetch exchange rate data.

    Args:
        currency_from: Base currency (3-letter currency code). Default is "USD" (US Dollar).
        currency_to: Target currency (3-letter currency code). Default is "KRW" (Korean Won).
        currency_date: Date to query the exchange rate for. Default is "latest" for the most recent rate.
            For historical rates, specify in YYYY-MM-DD format.

    Returns:
        dict: Dictionary containing exchange rate information.
            Example: {"amount": 1.0, "base": "USD", "date": "2023-11-24", "rates": {"EUR": 0.95534}}
    """

    import requests
    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()

#--------------------------[get_stock_price]-----------------------------
def get_stock_price(symbol: str)->dict:
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
