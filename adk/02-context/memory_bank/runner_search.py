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
from google.adk.memory import VertexAiMemoryBankService
from google.adk.memory import InMemoryMemoryService 

#from google.adk.memory import VertexAiRagMemoryService
from google.adk.memory import InMemoryMemoryService 

from google.adk.runners import Runner

from memory_bank import agent

#--------------------------------[run_search_agent]----------------------------------

async def run_search_agent(
                            session_service: BaseSessionService,
                            memory_service: BaseMemoryService,
                            app_name: str,
                            user_id: str,
):

    search_runner = Runner(
        agent=agent.search_agent,
        app_name=app_name,
        session_service=session_service,
        memory_service=memory_service,
    )


    session_id = "search_session_id"

    search_session = await search_runner.session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id,
    )

    while True:

        query = input("\n 👤 User: ")
        
        if query.lower() == "exit": break
        
        content_search = types.Content(role='user', parts=[types.Part(text=query)])

        async for event in search_runner.run_async(user_id=user_id, 
                                session_id=session_id, 
                                new_message=content_search):
            
            if event.is_final_response():
                final_response_text = event.content.parts[0].text
                print(f"Agent 1 Final Response: {final_response_text}")


    completed_session = await search_runner.session_service.get_session(app_name=app_name, 
                                                    user_id=user_id, 
                                                    session_id=session_id)

    print("\n--- Adding search session to Memory ---")
    await memory_service.add_session_to_memory(completed_session)
    
    print("Session added to memory.")


#--------------------------------[__name__]----------------------------------

if __name__ == "__main__":

    load_dotenv()

    print("에이전트를 실행합니다...")
    print("사용법 : uv run -m memory_bank.runner")

    parser = argparse.ArgumentParser(description="사용자 질의와 함께 ADK 에이전트를 실행합니다.")
    args = parser.parse_args()
    
    session_service = InMemorySessionService()

    PROJECT_ID = os.environ['GOOGLE_CLOUD_PROJECT']
    LOCATION = os.environ['GOOGLE_CLOUD_LOCATION']
    MEMORY_BANK_ID = os.environ['MEMORY_BANK_ID']

    memory_service = VertexAiMemoryBankService(
        project  =PROJECT_ID,
        location = LOCATION,
        agent_engine_id = MEMORY_BANK_ID
    )

    app_name = "AI_assistant"
    user_id = "Forusone"

    asyncio.run(run_search_agent(session_service = session_service, 
                                 memory_service = memory_service,
                                 app_name = app_name, 
                                 user_id = user_id, 
                                 ))
