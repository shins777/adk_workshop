# Copyright 2025 Forusone(forusone777@gmail.com)
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

from .callback import callback_before_tool
from .callback import callback_after_tool
from .callback import get_capital_city

load_dotenv()

#--------------------------------[build_agent]----------------------------------

def build_agent() -> Agent:
    """
    Creates and configures an Agent instance with a tool and callback support.

    This function loads environment variables, defines the agent's instruction template,
    and initializes the Agent with a name, model, description, instruction, and a tool for
    retrieving capital city information. It also attaches pre- and post-processing callbacks
    for tool execution, allowing custom logic before and after tool calls.

    Returns:
        Agent: A configured Agent instance ready to process user queries with tool and callback support.
    """

    INSTRUCTION = """
        You are an AI agent who provides answers to users' questions.
        When providing answers, please respond concisely and clearly in the following structure:
        - Question content:
        - Question intent:
        - Answer content:

        Note: Answer casual conversation questions natually without any special format.

    """

    agent = Agent(
        name = "root_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user inquiries",
        instruction = INSTRUCTION,
        tools = [get_capital_city],
        before_tool_callback=callback_before_tool,
        after_tool_callback=callback_after_tool
    )

    return agent

# Set the agent as a root_agent which could be imported from runner. 
root_agent = build_agent()