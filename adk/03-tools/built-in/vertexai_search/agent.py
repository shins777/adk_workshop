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
    Vertex AI Search 툴 인스턴스를 생성하고 설정합니다.

    이 함수는 프로젝트, 위치, 프로젝트 번호, 데이터스토어 ID에 필요한 환경 변수를 불러오고,
    Vertex AI 환경을 초기화한 뒤, 데이터스토어 리소스 경로를 구성해 해당 데이터스토어와 연동되는 VertexAiSearchTool 인스턴스를 반환합니다.

    반환값:
        VertexAiSearchTool: 지정한 Vertex AI Search 데이터스토어와 연동되는 인스턴스
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
    Vertex AI Search 툴이 포함된 Agent 인스턴스를 생성하고 설정합니다.

    이 함수는 환경 변수를 불러오고, 에이전트의 지시문 템플릿을 정의하며,
    이름, 모델, 설명, 지시문, Vertex AI Search 툴을 포함해 Agent를 초기화합니다.
    이 에이전트는 Vertex AI Search를 활용해 검색을 수행하고, 질문, 출처 정보, 답변을 구조화된 형식으로 제공합니다.

    반환값:
        Agent: Vertex AI Search 기반 질의 처리가 가능한 설정된 Agent 인스턴스
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