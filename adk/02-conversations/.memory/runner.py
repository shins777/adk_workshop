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
import asyncio
import argparse
from dotenv import load_dotenv

from google.genai import types
from google.adk.sessions import BaseSessionService
from google.adk.sessions import InMemorySessionService

from google.adk.memory import BaseMemoryService
from google.adk.memory import VertexAiRagMemoryService
from google.adk.memory import InMemoryMemoryService 

from google.adk.runners import Runner

from memory import agent

#--------------------------------[orchestrate_search_and_recall]----------------------------------

async def orchestrate_search_and_recall(
    session_service: BaseSessionService,
    memory_service: InMemoryMemoryService,
    app_name: str,
    user_id: str,
):
    """
    먼저 검색 에이전트를 실행한 후 리콜 에이전트를 실행하는 워크플로우를 오케스트레이션합니다.

    이 함수는 주어진 세션 및 메모리 서비스를 사용하여 Runner를 초기화하고,
    전용 세션에서 검색 에이전트를 실행한 뒤, 세션 결과를 메모리에 저장합니다.
    이후 별도의 세션에서 리콜 에이전트를 실행하여 메모리에서 정보를 조회합니다.

    인자:
        session_service (BaseSessionService): 사용자 세션을 관리하는 세션 서비스
        memory_service (BaseMemoryService): 세션 데이터를 저장/조회하는 메모리 서비스
        app_name (str): 애플리케이션 이름
        user_id (str): 사용자 식별자

    반환값:
        없음
    """

    search_runner = Runner(
        agent=agent.search_agent,
        app_name=app_name,
        session_service=session_service,
        memory_service=memory_service,
    )

    recall_runner = Runner(
        agent=agent.recall_agent,
        app_name=app_name,
        session_service=session_service,
        memory_service=memory_service,
    )

    search_session_id = "search_session_id"
    await run_search_agent(search_runner, memory_service, app_name, user_id, search_session_id)

    recall_session_id = "recall_session_id"
    await run_recall_agent(recall_runner, app_name, user_id, recall_session_id)

#--------------------------------[run_search_agent]----------------------------------

async def run_search_agent(
    runner: Runner, memory_service, app_name: str, user_id: str, session_id: str
):
    """
    전용 세션에서 검색 에이전트를 실행하고 세션 결과를 메모리에 저장합니다.

    이 함수는 검색 에이전트를 위한 새 세션을 생성하고, 사용자에게 입력을 요청하며,
    에이전트에 쿼리를 전송하고 에이전트의 최종 응답을 출력합니다.
    상호작용 후, 완료된 세션은 나중에 검색할 수 있도록 메모리 서비스에 추가됩니다.

    인자:
        runner (Runner): 에이전트 실행을 관리하는 Runner 인스턴스
        app_name (str): 애플리케이션 이름
        user_id (str): 사용자 식별자
        session_id (str): 검색 에이전트를 위한 세션 식별자

    반환값:
        없음
    """
    search_session = await runner.session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id,
    )

    query = input("\n 👤 User: ")
    
    if query.lower() == "exit": return
    
    content_search = types.Content(role='user', parts=[types.Part(text=query)])

    async for event in runner.run_async(user_id=user_id, 
                            session_id=session_id, 
                            new_message=content_search):
        
        if event.is_final_response():
            final_response_text = event.content.parts[0].text
            print(f"Agent 1 Final Response: {final_response_text}")


    completed_session = await runner.session_service.get_session(app_name=app_name, 
                                                      user_id=user_id, 
                                                      session_id=session_id)

    print("\n--- Adding search session to Memory ---")
    await memory_service.add_session_to_memory(completed_session)
    
    print("Session added to memory.")

#--------------------------------[run_recall_agent]----------------------------------

async def run_recall_agent(
    runner: Runner, app_name: str, user_id: str, session_id: str
):
    """
    메모리에서 정보를 검색하기 위해 전용 세션에서 리콜 에이전트를 실행합니다.

    이 함수는 리콜 에이전트를 위한 새 세션을 생성하고, 사용자에게 입력을 요청하며,
    에이전트에 쿼리를 전송하고 에이전트의 최종 응답을 출력합니다.
    리콜 에이전트는 메모리 서비스를 사용하여 이전에 저장된 세션을 기반으로 답변을 제공해야 합니다.

    인자:
        runner (Runner): 에이전트 실행을 관리하는 Runner 인스턴스
        app_name (str): 애플리케이션 이름
        user_id (str): 사용자 식별자
        session_id (str): 리콜 에이전트를 위한 세션 식별자

    반환값:
        없음
    """

    recall_session = await runner.session_service.create_session(app_name=app_name, 
                                                    user_id=user_id, 
                                                    session_id=session_id)

    while True:

        recall_instruction = input("\n 👤 User: ")
        if recall_instruction.strip().lower() in ["exit", "quit"]:
            return
        
        content_recall = types.Content(role='user', parts=[types.Part(text=recall_instruction)])

        async for event in runner.run_async(user_id=user_id, 
                                    session_id=session_id, 
                                    new_message=content_recall):

            print(f"  Event: {event.author} - Type: {'Text' if event.content and event.content.parts and event.content.parts[0].text else ''}"
                f"{'FuncCall' if event.get_function_calls() else ''}"
                f"{'FuncResp' if event.get_function_responses() else ''}")
            if event.get_function_calls():
                print(f"  Function Calls: {event.get_function_calls()}")
            
            if event.is_final_response():
                final_response_text_2 = event.content.parts[0].text
                print(f"\n 🤖 AI Assistant: {final_response_text_2}")
                break

#--------------------------------[__name__]----------------------------------

if __name__ == "__main__":

    load_dotenv()

    print("에이전트를 실행합니다...")
    print("사용법 : uv run -m memory.runner --memory_type [in_memory|rag_corpus]")

    parser = argparse.ArgumentParser(description="사용자 질의와 함께 ADK 에이전트를 실행합니다.")
    parser.add_argument("--memory_type",type=str,help="세션의 유형",)
    args = parser.parse_args()
    
    session_service = InMemorySessionService()

    if args.memory_type == "in_memory":
        memory_service = InMemoryMemoryService()
    
    elif args.memory_type == "rag_corpus":

        PROJECT_ID = os.environ['PROJECT_ID']
        LOCATION = os.environ['LOCATION']
        CORPUS_ID = os.environ['CORPUS_ID']
        
        # RAG Engine 을 Memory Service로 사용하기 위한 목적으로 사용.
        RAG_CORPUS_RESOURCE_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/ragCorpora/{CORPUS_ID}"

        memory_service = VertexAiRagMemoryService(
            rag_corpus=RAG_CORPUS_RESOURCE_NAME,
            similarity_top_k=10,
            vector_distance_threshold=0.2
        )
    
    else:
        raise ValueError("유효하지 않은 메모리 유형입니다. 'in_memory' 또는 'rag_corpus' 중에서 선택하세요.")
    
    # 실제는 app_name과 user_id는 환경변수나 설정 파일에서 가져오는 것이 좋습니다.
    # 여기서는 예시로 하드코딩된 값을 사용합니다.
    app_name = "AI_assistant"
    user_id = "Forusone"

    asyncio.run(orchestrate_search_and_recall(session_service = session_service, 
                                 memory_service = memory_service,
                                 app_name = app_name, 
                                 user_id = user_id, 
                                 ))
