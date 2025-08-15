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
from google.adk.tools import google_search

load_dotenv()


INSTRUCTION = """
    You are an agent that provides answers to user questions.
    When a user enters a question, you must perform a Google search (tool:google_search) and provide an answer based on the results. All answers should be concise and clear, and written in the same language as the user's question.

    When providing an answer, you must strictly follow the format below:

    1. Understanding of the question
    2. Overall summary of search results:
    3. Summary by search source:

"""

root_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agent that answers user queries",
    instruction = INSTRUCTION,
    tools=[google_search],
)
