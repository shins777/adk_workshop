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

market_info_agent = Agent(
    name="market_info_agent",
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    description="A agent that can provide information about current current economy by Google Search",
    instruction="""
        You are a helpful assistant that provides information about current economy by Google Search.
        
        ## Role: An AI assistant specializing in real-time economic information.
        ## Task: When asked about the economy, you MUST use the `@google_search` tool to find the most current and relevant news, trends, and data.
        ## Constraint: Base your entire response on the live results from the `@google_search`  tool. Do not use internal knowledge.   

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
      You are a helpful assistant that summarizes the information from other agents or tools.
      
      ## Role: A formatting agent that assembles tool outputs.

      ## Format:
        ### Market Summary
        [Insert current market summary from @market_info_tool here]

        ### Market Analysis and Insights
        [Insert current market summary from @market_info_tool here]

        ### Exchange Rate Information:
        [Insert full output from @exchange_rate_tool here]

    """,
)    