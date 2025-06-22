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

import time
import asyncio
import argparse
from dotenv import load_dotenv

from google.adk.events import Event, EventActions
from google.adk.sessions import InMemorySessionService

async def run_agent( app_name: str,
                     user_id: str,
                     session_id: str,):
    """
    ADK 이벤트 시스템을 사용하여 세션에서 명시적으로 상태를 변경하는 예시를 보여줍니다.

    이 함수는 초기 상태로 세션을 생성하고, 시스템 이벤트를 추가하여
    세션 상태(예: 타임스탬프 추가)를 업데이트합니다. 이벤트 전후의 상태를 출력하여
    세션 상태가 시간에 따라 어떻게 변하는지 보여줍니다.

    인자:
        app_name (str): 애플리케이션 이름
        user_id (str): 사용자 식별자
        session_id (str): 세션 식별자

    반환값:
        없음
    """

    session_service = InMemorySessionService()

    # 초기 상태 정의
    init_state = {
        "task_status": "active", 
    }

    session = await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id,
        state=init_state
    )
    
    print(f"1. 초기 상태: {session.state}")

    # 상태 변경
    state_changes = {
        "task_status": "active", 
        "timestamp": time.time(),   
    }

    system_event = Event(
        invocation_id = "change-state",
        author = "system", # 또는 'agent', 'tool' 등
        actions = EventActions(state_delta=state_changes),
        timestamp = time.time()
    )

    # append_event로 상태 변경
    await session_service.append_event(session, system_event)

    print("2. 명시적 상태 delta에 새로운 변경 이벤트를 추가함.")

    updated_session = await session_service.get_session(app_name=app_name,
                                                user_id=user_id, 
                                                session_id=session_id)
    
    print(f"3. 이벤트 전송 후 상태: {updated_session.state}")

if __name__ == "__main__":

    load_dotenv()

    print("에이전트를 실행 중...")
    print("사용법 : python main.py --app_name <app_name> --user_id <user_id> --session_id <session_id>")

    parser = argparse.ArgumentParser(description="사용자 쿼리로 ADK 에이전트를 실행합니다.")
    parser.add_argument("--app_name",type=str,help="이 에이전트의 애플리케이션 이름입니다.",)
    parser.add_argument("--user_id",type=str,help="이 에이전트와 상호작용하는 사용자 이름입니다.",)
    parser.add_argument("--session_id",type=str,help="이 에이전트의 세션을 식별하는 세션 ID입니다.",)
    args = parser.parse_args()

    asyncio.run(run_agent(app_name = args.app_name, 
                          user_id = args.user_id, 
                          session_id = args.session_id,))
