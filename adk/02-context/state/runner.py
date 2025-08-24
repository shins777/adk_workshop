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

from google.genai import types
from google.adk.runners import Runner
from google.adk.events import Event, EventActions
from google.adk.sessions import InMemorySessionService

from state import agent

async def run_agent( app_name: str,
                     user_id: str, ):
    """
    Example showing how to explicitly modify session state using the ADK event system.

    This function creates a session with an initial state, then demonstrates updating
    the session state (e.g., adding a timestamp) by appending a system event. It prints
    the session state before and after the change to show how state evolves over time.

    Args:
        app_name (str): The application name.
        user_id (str): The user identifier.

    Returns:
        None
    """

    session_service = InMemorySessionService()

    # Define initial state
    init_state = {
        "task_status": "No answer yet",
        "timestamp": time.time(),
    }

    session = await session_service.create_session(
        app_name= app_name,
        user_id=user_id,
        state=init_state
    )
    
    print(f"\n\n1. Initial session state: {session.state}")

    runner = Runner(agent=agent.root_agent,
                    app_name=app_name,
                    session_service=session_service)

    while True:

        user_input = input("\n 👤 User: ")
        if user_input.lower().strip() in ["exit", "quit", "bye"]:
            break

        query = user_input
        content = types.Content(role='user', parts=[types.Part(text=query)])

        # Execute agent events asynchronously using the agent runner.
        # Session information is passed via user_id and session_id.
        events = runner.run_async(user_id=session.user_id,
                                session_id=session.id,
                                new_message=content,)

        async for event in events:
            if event.is_final_response():
                final_response = event.content.parts[0].text            
                print("\n 🤖 AI Assistant: " + final_response)

        updated_session = await session_service.get_session(app_name = session.app_name, 
                                                     user_id = session.user_id, 
                                                     session_id = session.id)

        # Display the 'last_turn' from the updated session state
        print(f"\n\n output_key - last_turn : {updated_session.state['last_turn']}")

    # Prepare state changes
    state_changes = {
        "task_status": f"Answered to : {query}",
        "timestamp": time.time(),
        "last_turn": updated_session.state['last_turn']
    }

    system_event = Event(
        invocation_id = "change-state",
        author = "system", # or 'agent', 'tool', etc.
        actions = EventActions(state_delta=state_changes),
        timestamp = time.time()
    )

    # Append the state-change event
    await session_service.append_event(session, system_event)

    print("\n\n2. Appended a new explicit state-delta event.")

    updated_session = await session_service.get_session(app_name=session.app_name,
                                                user_id=session.user_id, 
                                                session_id=session.id)
    
    print(f"\n\n3. Session state after sending the event: {updated_session.state}")

if __name__ == "__main__":

    load_dotenv()

    print("Running the agent...")
    print("Usage : uv run -m state.runner --app_name <app_name> --user_id <user_id> ")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--app_name",type=str,help="The application name for this agent.",)
    parser.add_argument("--user_id",type=str,help="The user interacting with this agent.",)
    args = parser.parse_args()
    
    asyncio.run(run_agent(app_name = args.app_name, 
                          user_id = args.user_id,))
