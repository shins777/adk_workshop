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

from google.genai import types
from google.adk.sessions import BaseSessionService
from google.adk.runners import Runner
from google.adk.memory import BaseMemoryService

from memory import agent

#--------------------------------[orchestrate_search_and_recall]----------------------------------

async def orchestrate_search_and_recall(
    session_service: BaseSessionService,
    memory_service: BaseMemoryService,
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

    runner = Runner(agent=agent.search_agent,
                    app_name=app_name,
                    session_service=session_service,
                    memory_service=memory_service)

    # Use different session. 
    search_session_id = "search_session_id"
    await run_search_agent(runner,app_name,user_id,search_session_id,)

    recall_session_id = "recall_session_id"
    await run_recall_agent(runner,app_name,user_id,recall_session_id,)

#--------------------------------[run_search_agent]----------------------------------

async def run_search_agent(runner:Runner,
                     app_name,
                     user_id,
                     session_id,):    

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
    if query.lower() == "exit":
        return
    
    content_search = types.Content(role='user', parts=[types.Part(text=query)])

    async for event in runner.run_async(user_id=search_session.user_id, 
                            session_id=search_session.id, 
                            new_message=content_search):
        
        if event.is_final_response():
            final_response_text = event.content.parts[0].text
            print(f"Agent 1 Final Response: {final_response_text}")


    completed_session_1 = await runner.session_service.get_session(app_name=search_session.app_name, 
                                                      user_id=search_session.user_id, 
                                                      session_id=search_session.id)

    print("\n--- Adding search session to Memory ---")
    await runner.memory_service.add_session_to_memory(completed_session_1)
    print("Session added to memory.")

#--------------------------------[run_recall_agent]----------------------------------

async def run_recall_agent(runner:Runner,
                           app_name,
                           user_id,
                           session_id,): 
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

    runner.agent = agent.recall_agent
    
    recall_instruction = input("\n 👤 User: ")
    if recall_instruction.lower() == "exit":
        return
    
    content_recall = types.Content(role='user', parts=[types.Part(text=recall_instruction)])

    async for event in runner.run_async(user_id=recall_session.user_id, 
                                  session_id=recall_session.id, 
                                  new_message=content_recall):

        print(f"  Event: {event.author} - Type: {'Text' if event.content and event.content.parts and event.content.parts[0].text else ''}"
            f"{'FuncCall' if event.get_function_calls() else ''}"
            f"{'FuncResp' if event.get_function_responses() else ''}")
        
        if event.is_final_response():
            final_response_text_2 = event.content.parts[0].text
            print(f"\n 🤖 AI Assistant: {final_response_text_2}")
            break
