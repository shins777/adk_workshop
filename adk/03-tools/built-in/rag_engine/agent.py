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
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

load_dotenv()

def buid_rag_tool():
    
    rag_engine_tool = VertexAiRagRetrieval(
        name='retrieve_rag_documentation',
        description=(
            'Use this tool to retrieve documentation and reference materials for the question from the RAG corpus,'
        ),
        rag_resources=[
            rag.RagResource(
                rag_corpus=os.environ.get("RAG_CORPUS")
            )
        ],
        similarity_top_k=10,
        vector_distance_threshold=0.3,
    )
    return rag_engine_tool


def build_agent() -> Agent:
    """
    Creates and configures an Agent instance with Google Search tool support.

    This function loads environment variables, sets up the agent's instruction template,
    and initializes the Agent with a name, model, description, instruction, and the Google Search tool.
    The agent is designed to answer user inquiries using both its own knowledge and search capabilities.

    Returns:
        Agent: A configured Agent instance ready to process user queries.
    """

    INSTRUCTION = """
        You are an agent who provides answers to users' questions.
        When a user enters a question, you should perform a rag_engine_tool for that question and provide an answer based on the results.
        When you provide an answer, you have to follow the below format exactly:

        1. Question: 
        2. Citations: 
        3. Answer: 

        Note : When answering, Must be sure to use the same language the user used when asking the question. 

    """
    rag_engine_tool = buid_rag_tool()

    agent = Agent(
        name = "search_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
        tools=[rag_engine_tool],

    )
    return agent

root_agent = build_agent()