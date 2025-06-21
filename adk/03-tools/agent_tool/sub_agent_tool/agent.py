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
from google.adk.tools.agent_tool import AgentTool

from .sub_agent import positive_critic, negative_critic

load_dotenv()

def build_agent() -> Agent:
    """
    Creates and configures a root Agent instance with sub-agent tools for critique tasks.

    This function loads environment variables, defines the agent's instruction template,
    and initializes the Agent with a name, model, description, and instruction. It attaches
    sub-agent tools for positive and negative critique, allowing the root agent to delegate
    specific critique tasks to the appropriate tool based on user requests.

    Returns:
        Agent: A configured Agent instance with sub-agent tools ready to process user queries.
    """

    INSTRUCTION = """
        You are an agent that provides answers to users' questions 
        When replying, you must answer based on the language the user used. 
        
        Provide answers in the following flow.

        1. When a user enters a question, you must first organize the intent of the question. Again, say "Question intent" and organize the intent of the question.

        2. Depending on the user's question, you must provide an answer using tools as follows.
            2-1. If the user requests a positive critique, use the positive_critic tool to write a positive critique.
            2-2. If the user requests a negative critique, use the negative_critic tool to write a negative critique.
            2-3. If the user requests both a positive and a negative critique, use both tools (positive_critic, negative_critic) to write each critique.
        
    """

    agent = Agent(
        name = "root_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
        tools = [AgentTool(agent=positive_critic),
                AgentTool(agent=negative_critic)]
    )

    return agent

root_agent = build_agent()
