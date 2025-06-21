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

load_dotenv()

def build_agent() -> Agent:
    """
    Creates and configures a basic Agent instance for answering user questions.

    This function loads environment variables, defines the agent's instruction template,
    and initializes the Agent with a name, model, description, and instruction. The agent
    is designed to provide concise and structured answers to user inquiries.

    Returns:
        Agent: A configured Agent instance ready to process user queries.
    """

    INSTRUCTION = """
        You are an AI agent who provides answers to users' questions.
        When providing answers, please respond concisely and clearly in the following structure:
        - Question content:
        - Question intent:
        - Answer content:

        Please answer everyday conversation questions without any special format.
        Note : When answering, Must be sure to use the same language the user used when asking the question. 
    """

    agent = Agent(
        name = "basic_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
    )
    return agent

root_agent = build_agent()
