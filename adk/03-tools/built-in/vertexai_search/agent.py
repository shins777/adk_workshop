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
from google.adk.tools import VertexAiSearchTool
import vertexai

load_dotenv()

def get_vertex_search_tool():
    """
    Creates and configures a Vertex AI Search tool instance.

    This function loads required environment variables for project, location, project number,
    and datastore ID, initializes the Vertex AI environment, constructs the data store resource path,
    and returns a VertexAiSearchTool instance configured for the specified data store.

    Returns:
        VertexAiSearchTool: An instance configured to interact with the specified Vertex AI Search data store.
    """

    PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT')
    LOCATION = os.getenv('GOOGLE_CLOUD_LOCATION')
    PROJECT_NUMBER = os.getenv('PROJECT_NUMBER')
    DATASTORE_ID = os.getenv('DATASTORE_ID')

    vertexai.init(project=PROJECT_ID, location=LOCATION)

    data_store_id = f"projects/{PROJECT_NUMBER}/locations/{LOCATION}/collections/default_collection/dataStores/{DATASTORE_ID}"
    
    print("Vertex AI Search : Data store ID : \n", data_store_id)

    vertex_search_tool = VertexAiSearchTool(data_store_id=data_store_id)
    print("Vertex AI Search : vertex_search_tool : \n", vertex_search_tool)

    return vertex_search_tool


def build_agent() -> Agent:
    """
    Creates and configures an Agent instance with Vertex AI Search tool support.

    This function loads environment variables, defines the agent's instruction template,
    and initializes the Agent with a name, model, description, instruction, and the Vertex AI Search tool.
    The agent is designed to answer user questions by performing a search using Vertex AI Search
    and providing answers in a structured format including the question, source information, and answer.

    Returns:
        Agent: A configured Agent instance ready to process user queries using Vertex AI Search.
    """

    INSTRUCTION = """
        You are an agent that provides answers to users' questions.
        When a user enters a question, you must perform a search on the 'vertex_search_tool' for that question and provide an answer based on the results.

        Note : When answering, Must be sure to use the same language the user used when asking the question. 
        
    """
    
    vertex_search_tool = get_vertex_search_tool()

    vertexai_search = Agent(
        name = "vertexai_search",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user query",
        instruction = INSTRUCTION,
        tools=[vertex_search_tool],
    )
    return vertexai_search

root_agent = build_agent()