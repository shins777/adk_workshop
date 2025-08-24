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
from google.adk.runners import Runner

from memory_bank import agent


#--------------------------------[run_recall_agent]----------------------------------

async def run_recall_agent(
                            session_service: BaseSessionService,
                            memory_service: BaseMemoryService,
                            app_name: str,
                            user_id: str,

):

    recall_runner = Runner(
        agent=agent.recall_agent,
        app_name=app_name,
        session_service=session_service,
        memory_service=memory_service,
    )


    session_id = "recall_session_id"

    recall_session = await recall_runner.session_service.create_session(app_name=app_name, 
                                                    user_id=user_id, 
                                                    session_id=session_id)

    while True:

        recall_instruction = input("\n 👤 User: ")
        if recall_instruction.strip().lower() in ["exit", "quit"]:
            break
        
        content_recall = types.Content(role='user', parts=[types.Part(text=recall_instruction)])

        async for event in recall_runner.run_async(user_id=user_id, 
                                    session_id=session_id, 
                                    new_message=content_recall):

            if event.is_final_response():
                final_response_text_2 = event.content.parts[0].text
                print(f"\n 🤖 AI Assistant: {final_response_text_2}")
                break

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

    asyncio.run(run_recall_agent(session_service = session_service, 
                                 memory_service = memory_service,
                                 app_name = app_name, 
                                 user_id = user_id, 
                                 ))
