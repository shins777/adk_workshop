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

from . import instruction

load_dotenv()

def build_agent() -> Agent:
    """
    Creates and configures an Agent instance with Google Search tool support.

    This function loads environment variables, sets up the agent's instruction template,
    and initializes the Agent with a name, model, description, instruction, and the Google Search tool.
    The agent is designed to answer user inquiries using both its own knowledge and search capabilities.

    Returns:
        Agent: A configured Agent instance ready to process user queries.
    """

    agent = Agent(
        name = "search_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = instruction.INSTRUCTION,
        tools=[google_search],

    )
    return agent

root_agent = build_agent()