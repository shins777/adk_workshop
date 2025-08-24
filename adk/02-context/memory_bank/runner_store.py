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

async def run_search_agent( session_service: BaseSessionService,
                            memory_service: BaseMemoryService,
                            app_name: str,
                            user_id: str,):

    search_runner = Runner(
        agent=agent.search_agent,
        app_name=app_name,
        session_service=session_service,
        memory_service=memory_service,
    )

    session = await search_runner.session_service.create_session(
        app_name=app_name,
        user_id=user_id,)

    while True:

        user_input = input("\n 👤 User: ")
        
        if user_input.lower().strip() in ["exit", "quit", "bye"]:
                    break
        
        content = types.Content(role='user', parts=[types.Part(text=user_input)])

        async for event in search_runner.run_async(user_id = session.user_id, 
                                session_id = session.id, 
                                new_message = content):
            
            if event.is_final_response():
                final_response_text = event.content.parts[0].text
                print(f"\n 🤖 AI Assistant: {final_response_text}")


    completed_session = await search_runner.session_service.get_session(app_name=app_name, 
                                                    user_id=session.user_id, 
                                                    session_id=session.id)

    print("\n-- Adding search session to Memory ---")
    await memory_service.add_session_to_memory(completed_session)
    
    print("\t Session added to memory.")


#--------------------------------[__name__]----------------------------------

if __name__ == "__main__":

    load_dotenv()

    print("Running the agent...")
    print("Usage: uv run -m memory_bank.runner_store --app_name <app_name> --user_id <user_id>")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--app_name",type=str,help="The application name for this agent.",)
    parser.add_argument("--user_id",type=str,help="The user interacting with this agent.",)    
    args = parser.parse_args()
    
    session_service = InMemorySessionService()

    memory_service = VertexAiMemoryBankService(
        project  = os.environ['GOOGLE_CLOUD_PROJECT'],
        location = os.environ['GOOGLE_CLOUD_LOCATION'],
        agent_engine_id = os.environ['MEMORY_BANK_ID']
    )

    asyncio.run(run_search_agent(session_service = session_service, 
                                 memory_service = memory_service,
                                 app_name = args.app_name, 
                                 user_id = args.user_id, ))
