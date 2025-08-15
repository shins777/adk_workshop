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
from google.adk.tools import VertexAiSearchTool
import vertexai

load_dotenv()

def get_vertex_search_tool():
    """
    Creates and configures a Vertex AI Search tool instance.

    This function loads the required environment variables for project, location, project number, and datastore ID,
    initializes the Vertex AI environment, constructs the datastore resource path, and returns a VertexAiSearchTool instance linked to the specified datastore.

    Returns:
        VertexAiSearchTool: An instance connected to the specified Vertex AI Search datastore.
    """

    # Vertex AI Search is available in the global location, so set VERTEXAI_LOCATION to "global".
    # When constructing data_store_id, use the project number and datastore ID to build the full path.
    VAIS_PROJECT_NUMBER = os.getenv('VAIS_PROJECT_NUMBER')
    VAIS_LOCATION = os.getenv('VAIS_LOCATION')  # Vertex AI Search는 글로벌 위치에서 사용 가능
    VAIS_DATASTORE_ID = os.getenv('VAIS_DATASTORE_ID')

    data_store_id = f"projects/{VAIS_PROJECT_NUMBER}/locations/{VAIS_LOCATION}/collections/default_collection/dataStores/{VAIS_DATASTORE_ID}"
    print("Vertex AI Search : Data store ID : \n", data_store_id)

    vertex_search_tool = VertexAiSearchTool(data_store_id=data_store_id)
    print("Vertex AI Search : vertex_search_tool : \n", vertex_search_tool)

    return vertex_search_tool


INSTRUCTION = """
    You are an agent that provides answers to user questions.
    When a user asks a question, you must use the 'vertex_search_tool' to perform a search and provide an answer based on the results.
"""

vertex_search_tool = get_vertex_search_tool()
print("Vertex AI Search : vertex_search_tool : \n", vertex_search_tool)

root_agent = Agent(
    name = "vertexai_search",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agent that answers user queries",
    instruction = INSTRUCTION,
    tools=[vertex_search_tool],
)