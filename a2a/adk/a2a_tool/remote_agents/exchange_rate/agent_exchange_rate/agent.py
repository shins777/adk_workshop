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

from .functions import get_exchange_rate

root_agent = Agent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name='agent_exchange_rate',
    description='An agent specialized in checking exchange rate via an external API. ',
    instruction="""
        You are a master AI agent providing exchange rate for the given currencies.
        ## Goal: Fetch a currency exchange rate and return the data to the orchestrator agent.
        ## Execution Plan: Call the get_exchange_rate tool with the two specified currencies.

    """,
    tools=[
        get_exchange_rate,
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
