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

import asyncio
from google.genai import types
from google.adk.sessions import BaseSessionService
from google.adk.runners import Runner

from session import agent

#--------------------------------[run_agent]----------------------------------

async def run_agent(
    session_service: BaseSessionService,
    app_name: str,
    user_id: str,
    agent_engine_app_name: str = None
):
    """
    세션 인식 대화 루프에서 에이전트를 실행합니다.
    이 함수는 사용자와 애플리케이션에 대한 기존 세션이 있는지 확인합니다. 세션이 있으면
    가장 최근의 세션을 이어가고, 없으면 새 세션을 생성합니다. 이후 루프에 진입하여
    사용자 입력을 받고, 입력을 에이전트에 전달하며, 에이전트의 응답을 출력합니다.
    각 상호작용 후 세션 상태와 이벤트를 출력합니다.

    인자:
        session_service (BaseSessionService): 사용자 세션을 관리하는 세션 서비스
        app_name (str): 애플리케이션 이름
        user_id (str): 사용자 식별자
        agent_engine_app_name (str, optional): 에이전트 엔진의 앱 이름(해당되는 경우)

    반환값:
        없음
    """

    # 만약 agent_engine_app_name이 제공되면 해당 앱 이름을 사용합니다.
    if agent_engine_app_name != None:
        app_name = agent_engine_app_name

    # 세션 서비스가 제공하는 앱 이름과 사용자 ID를 사용하여 기존 세션을 조회합니다.
    existing_sessions = await session_service.list_sessions(
        app_name=app_name,
        user_id=user_id,
    )

    if existing_sessions and len(existing_sessions.sessions) > 0:
        # 기존 세션이 있다면 가장 최근의 세션을 사용합니다.
        session_id = existing_sessions.sessions[0].id
        print(f"Using existing session: {session_id}")
        
    else:
        # 만약 세션이 없다면 새 세션을 생성합니다.
        new_session = await session_service.create_session(
            app_name=app_name,
            user_id=user_id,
            state=None,
        )
        session_id = new_session.id
        print(f"Created new session: {session_id}")
    
    # 에이전트 러너를 초기화합니다.
    runner = Runner(agent=agent.root_agent,
                    app_name=app_name,
                    session_service=session_service)

    while True:

        query = input("\n 👤 User: ")
        if query.strip().lower() in ["exit", "quit"]:
            break

        content = types.Content(role='user', parts=[types.Part(text=query)])

        # 에이전트 러너를 사용하여 비동기적으로 이벤트를 실행합니다.
        # 이때 사용자 ID와 세션 ID를 전달하여 세션을 유지합니다. 한번의 대화에서는 기존의 세션 1개만 사용합니다.
        # 만약 새로운 세션을 생성하고 싶다면, session_id를 None으로 설정
        events = runner.run_async(user_id=user_id,
                                session_id=session_id,
                                new_message=content,
                                )

        async for event in events:
            await asyncio.create_task(print_session(app_name = app_name,
                                                    user_id = user_id,
                                                    session_id = session_id,
                                                    session_service = session_service))
            if event.is_final_response():
                final_response = event.content.parts[0].text            
                print("\n 🤖 AI Assistant: " + final_response)

#--------------------------------[print_session]----------------------------------

async def print_session(app_name: str,
                        user_id: str,
                        session_id: str,
                        session_service: BaseSessionService):
    """
    세션의 속성을 조회하고 출력합니다.

    이 함수는 주어진 애플리케이션 이름, 사용자 ID, 세션 ID를 사용하여
    세션 서비스에서 세션 객체를 가져옵니다. 이후 세션의 주요 속성(세션 ID, 앱 이름, 사용자 ID, 상태, 이벤트, 마지막 업데이트 시간)을 출력합니다.

    인자:
        app_name (str): 애플리케이션 이름
        user_id (str): 사용자 ID
        session_id (str): 세션 ID
        session_service (BaseSessionService): 세션 서비스 인스턴스

    반환값:
        없음
    """

    # 세션 서비스에서 세션을 조회합니다.
    # 이때 app_name, user_id, session_id를 사용하여 특정 세션을 가져옵니다.
    session  = await session_service.get_session(app_name=app_name,
                                user_id=user_id,
                                session_id=session_id,)
    

    print(f"--- Examining Session Properties ---")
    print(f"ID (`id`):                {session.id}")
    print(f"Application Name (`app_name`): {session.app_name}")
    print(f"User ID (`user_id`):         {session.user_id}")
    print(f"State (`state`):           {session.state}") # Note: Only shows initial state here
    print(f"Events (`events`):         {session.events}") # Initially empty
    print(f"Last Update (`last_update_time`): {session.last_update_time:.2f}")
    print(f"---------------------------------")

