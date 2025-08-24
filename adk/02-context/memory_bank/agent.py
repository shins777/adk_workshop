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
from google.adk.tools import preload_memory_tool 
from google.adk.tools import google_search

load_dotenv()

#--------------------------------[build_search_agent]----------------------------------

search_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agent that answers user queries",
    instruction = """
        You are an agent that provides answers to user questions.
        # When a user submits a question, perform a Google search (tool: google_search)
        # for that question and provide an answer based on the results. 
        """,
    # tools=[google_search],
    tools=[preload_memory_tool.PreloadMemoryTool()],
)

#--------------------------------[build_recall_agent]----------------------------------

RECALL_INSTRUCTION = """
    You are an agent that provides answers to user questions.
    If the user requests information from prior conversations, use the registered tool
    to retrieve stored memories and answer the user based on those memories.
"""

recall_agent = Agent(
    name = "recall_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agent that retrieves information from memory to answer user questions",
    instruction = """
        You are an agent that provides answers to user questions.
        If the user requests information from prior conversations, use the registered tool
        to retrieve stored memories and answer the user based on those memories.""",
    tools=[preload_memory_tool.PreloadMemoryTool()],
)
