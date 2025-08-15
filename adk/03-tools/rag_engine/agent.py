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
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

load_dotenv()

def buid_rag_tool():
    
    rag_engine_tool = VertexAiRagRetrieval(
        name='retrieve_rag_documentation',
        description=(
            'Use this tool to search for documents and references related to questions in the RAG Engine corpus.'
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

INSTRUCTION = """
    You are an agent that provides answers to user questions.
    When a user asks a question, you must use the rag_engine_tool to provide an answer based on the results.
    When providing an answer, you must strictly follow the format below:

    1. Identify the user's question intent:
    2. Reference documents:
    3. Answer summary:

    Note: Always respond in the same language as the user's question.
"""

rag_engine_tool = buid_rag_tool()

root_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agent that answers user queries",
    instruction = INSTRUCTION,
    tools=[rag_engine_tool],
)