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

from .callback import callback_before_agent
from .callback import callback_after_agent

load_dotenv()

#--------------------------------[build_agent]----------------------------------

def build_agent()->Agent:
    """
    Builds and returns an AI agent configured to answer user questions.
    The agent uses the model specified in the environment variable 'MODEL' and is initialized
    with a specific instruction template to ensure concise and structured responses. 
    It also attaches pre- and post-processing callbacks for additional handling.

    Returns:
        Agent: An instance of the Agent class, ready to process user inquiries.
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
        before_agent_callback=callback_before_agent,
        after_agent_callback=callback_after_agent 
    )
    return agent

# Set the agent as a root_agent which could be imported from runner. 
root_agent = build_agent()

