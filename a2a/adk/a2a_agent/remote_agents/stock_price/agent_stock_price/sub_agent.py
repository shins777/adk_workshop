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
from google.adk.tools import google_search
from google.genai import types
import os 

company_info_agent = Agent(
    name="company_info_agent",
    model=os.getenv("GOOGLE_GENAI_MODEL"),

    description="A agent that can provide information about companies by searching the web.",
    instruction="""
      You are a helpful assistant that provides information about companies by searching the web.
      When asked to provide a given company's information, you must perform a web search using the google_search tool to proivide accurate and up-to-date information in temrs of the company's stock price, market cap, and recent news. you must use the google_search tool to find the most relevant and recent information about the company.
    """,

    tools=[google_search],

    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)

summarizer_agent = Agent(
    name="summarizer_agent",
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    description="A agent that can summarize the information from other agents and tools.",
    instruction="""
      You are a helpful assistant that summarizes the information from other agents and tools.
      When asked, you must summarize the information with the given format.

      -   **Output Format:**
        ```
        **Company Name**

        **Overall company information**
        [Insert full output from @company_info_tool here]

        **Stock Price:**
        [Insert full output from @get_stock_price here]
        ```

    """,
)    