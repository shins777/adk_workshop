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

from google.genai import types
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

from tool_callback import agent

async def run_agent(user_query: str):
    """
    Asynchronously runs the AI agent with the provided user query.

    This function creates a user session, initializes the agent runner, and sends the user's query
    to the agent. It streams the agent's responses and prints the final response to the console.

    Args:
        user_query (str): The user's input or question to be processed by the agent.

    Returns:
        None
    """

    print(f"\n 👤 User: {user_query}\n")

    APP_NAME = "AI_assistant"
    USER_ID = "Forusone"

    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME,
                                            user_id=USER_ID,
                                            )
    
    runner = Runner(agent=agent.root_agent,
                    app_name=session.app_name,
                    session_service=session_service)
    
    content = types.Content(role='user', parts=[types.Part(text=user_query)])

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

    print("Start to run the agent...")
    print(""" Usage : uv run -m tool_callback.runner --query 'What is the capital city of Korea?' """)

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--query",type=str,help="The application name of this agent.",)

    args = parser.parse_args()
    asyncio.run(run_agent(user_query=args.query))