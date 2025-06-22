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
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

from runtime import agent

async def run_agent():
    """
    사용자 질의와 함께 AI 에이전트를 비동기적으로 실행합니다.

    이 함수는 사용자 세션을 생성하고, 에이전트 러너를 초기화한 뒤,
    사용자의 질의를 에이전트에 전달합니다. 에이전트의 응답을 스트리밍하며,
    최종 응답을 콘솔에 출력합니다.

    인자:
        없음
    반환값:
        없음
    """

    APP_NAME = "AI_assistant"
    USER_ID = "Forusone"

    # 세션 서비스 초기화
    # InMemorySessionService는 메모리 내에서 세션을 관리합니다.
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME,
                                            user_id=USER_ID)
    
    runner = Runner(agent=agent.root_agent,
                    app_name=session.app_name,
                    session_service=session_service)
    
    while True:

        query = input("\n 👤 User: ")
        if query.strip().lower() in ["exit", "quit"]:
            break
        
        content = types.Content(role='user', parts=[types.Part(text=query)])

        events = runner.run_async(user_id=session.user_id,
                                session_id=session.id,
                                new_message=content,)

        async for event in events:
            if event.is_final_response():
                final_response = event.content.parts[0].text            
                print(f"\n 🤖 AI Assistant: {final_response}\n")

if __name__ == "__main__":
    import asyncio
    import argparse

    print("Running the agent...")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    asyncio.run(run_agent())