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

from .sub_agent import positive_critic, negative_critic

load_dotenv()

def build_agent():
    """
    Creates and configures an Agent instance with sub-agents for positive and negative critique.

    This function defines the agent's instruction template and initializes the Agent with a name,
    model, description, instruction, and sub-agents for positive and negative critique. The agent
    is designed to answer user questions by delegating critique tasks to the appropriate sub-agent
    and formatting the response according to the specified structure.

    Returns:
        Agent: A configured Agent instance ready to process user queries with critique sub-agents.
    """

    SYSTEM_INSTRUCTION = """
        When answering, Must be sure to use the same language the user used when asking the question. 
    """

    INSTRUCTION = """
        You are an agent that provides answers to users' questions 
        Provide answers in the following flow.

        1. When a user enters a question, you must first organize the intent of the question. Again, say "Question intent" and organize the intent of the question.

        2. Depending on the user's question, you must provide an answer using sub_agents as follows.
            2-1. If the user requests a positive critique, use the positive_critic agent to write a positive critique.
            2-2. If the user requests a negative critique, use the negative_critic agent to write a negative critique.
            2-3. If the user requests both a positive and a negative critique, use both agents(positive_critic, negative_critic) to write each critique.
    """

    agent = Agent(
        name = "Search_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        global_instruction = SYSTEM_INSTRUCTION,
        instruction = INSTRUCTION,
        sub_agents = [positive_critic, negative_critic],
    )        
    return agent

root_agent = build_agent()
