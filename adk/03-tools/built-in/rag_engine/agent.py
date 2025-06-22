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
            '이 도구를 사용하여 RAG Engine 코퍼스에서 질문에 대한 문서 및 참고 자료를 검색합니다.'
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
    Google Search 툴이 포함된 Agent 인스턴스를 생성하고 설정합니다.

    이 함수는 환경 변수를 불러오고, 에이전트의 지시문 템플릿을 설정하며,
    이름, 모델, 설명, 지시문, Google Search 툴을 포함해 Agent를 초기화합니다.
    이 에이전트는 자체 지식과 검색 기능을 활용해 사용자 질문에 답변하도록 설계되었습니다.

    반환값:
        Agent: 사용자 질의를 처리할 준비가 된 설정된 Agent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        사용자가 질문을 입력하면, 해당 질문에 대해 rag_engine_tool을 사용하여 결과를 바탕으로 답변을 제공해야 합니다.
        답변을 제공할 때는 반드시 아래 형식을 정확히 따라야 합니다:

        1. 사용자 질문 의도 파악: 
        2. 참조 문서: 
        3. 답변 요약: 

        참고: 답변 시 반드시 사용자가 질문에 사용한 언어와 동일한 언어로 답변해야 합니다.
    """
    rag_engine_tool = buid_rag_tool()

    agent = Agent(
        name = "search_agent",
        model = os.getenv("MODEL"),
        description = "사용자 질의에 답변하는 에이전트",
        instruction = INSTRUCTION,
        tools=[rag_engine_tool],

    )
    return agent

root_agent = build_agent()