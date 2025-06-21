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
from google.adk.tools import google_search
from google.adk.tools import load_memory # Tool to query memory

load_dotenv()

#--------------------------------[build_search_agent]----------------------------------

def build_search_agent() -> Agent:
    """
    Creates and configures an Agent instance with Google Search tool support.

    This agent is designed to answer user questions by performing a Google search using the
    google_search tool and providing an answer based on the search results. The response
    follows a structured format including the question, source information, and answer.

    Returns:
        Agent: An Agent instance configured to answer queries using Google Search.
    """

    SEARCH_INSTRUCTION = """
            You are an agent who provides answers to users' questions.
            When a user enters a question, you should perform a Google search(tool:google_search) for that question and provide an answer based on the results.
            When you provide an answer, you have to follow the below format exactly:

            1. Question: 
            2. Source information: 
            3. Answer: 

            Note : When answering, Must be sure to use the same language the user used when asking the question. 

        """

    search_agent = Agent(
        name = "search_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = SEARCH_INSTRUCTION,
        tools=[google_search],
    )
    return search_agent

#--------------------------------[build_recall_agent]----------------------------------

def build_recall_agent() -> Agent:
    """
    Creates and configures an Agent instance with memory recall capabilities.

    This agent is designed to answer user questions by querying stored memory using the
    'load_memory' tool. The agent retrieves relevant information from memory and provides
    answers based on the results.

    Returns:
        Agent: An Agent instance configured to answer queries by retrieving information from memory.
    """

    RECALL_INSTRUCTION = """
            You are an agent that provides answers to users' questions. When a user asks a question, 
            You should use the 'load_memory' tool to query the memory and provide an answer based on the results.
        """

    recall_agent = Agent(
        name = "recall_agent",
        model = os.getenv("MODEL"),
        description = "An agent that answers users' questions by retrieving them from memory.",
        instruction = RECALL_INSTRUCTION,
        tools=[load_memory],
    )
    return recall_agent

search_agent = build_search_agent()
recall_agent = build_recall_agent()
