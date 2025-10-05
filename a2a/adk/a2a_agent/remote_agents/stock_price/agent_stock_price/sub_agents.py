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
from google.adk.tools import google_search
from google.genai import types

company_info_agent = Agent(
    name="company_info_agent",
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    description="A agent that can provide information about companies by Google Search",
    instruction="""
      You are a helpful assistant that provides information about companies by Google Search.

      ## Role: An AI assistant specializing in company information.

      ## Task: When asked about a company, you MUST use the `@google_search` tool to find the most current data for the following points:
        1. Stock Price
        2. Market Cap
        3. Recent News

      ## Do not use any pre-trained knowledge. Rely only on the `@google_search` tool outputs.

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
    description="A agent that can summarize the information from other agents or tools.",
    instruction="""
      You are a helpful assistant that summarizes the information from other agents or tools.
      
      ## Role: A formatting agent that assembles tool outputs.

      ## Format:
        ### Company Name
        [Insert company name here and basic description if available]

        ### Overall company information
        [Insert full output from @company_info_tool here]

        ### Stock Price:
        [Insert full output from @get_stock_price here]

    """,
)    