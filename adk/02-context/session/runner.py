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
from dotenv import load_dotenv

from google.adk.sessions import InMemorySessionService
from google.adk.sessions import DatabaseSessionService
from google.adk.sessions import VertexAiSessionService

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
    session_id: str = None,
):
    """
    Run the agent in a session-aware interactive loop.

    This function checks whether an existing session for the user and application exists.
    If a session exists, it continues the most recent session; otherwise it creates a new one.
    Then it enters a loop that reads user input, forwards the input to the agent, and prints agent responses.
    After each interaction it prints the session state and events.

    Args:
        session_service (BaseSessionService): The session service that manages user sessions.
        app_name (str): The application name.
        user_id (str): The identifier for the user.
        session_id (str): The identifier for the session.

    Returns:
        None
    """

    # Query existing sessions from the session service for the given app_name and user_id.
    existing_sessions = await session_service.list_sessions(
        app_name=app_name,
        user_id=user_id,
    )
    
    # Check if a session with the given session_id exists. If session_id is None, this will be None.
    session_id = next((session_id for session in existing_sessions.sessions if session.id == session_id), None)
    
    if session_id is None:
        # No existing session found, create a new session.
        
        if isinstance(session_service, VertexAiSessionService): 
            # If using VertexAiSessionService, do not pass session_id to create_session. ( google-adk==1.12.0 As of August 2025 )        
            new_session = await session_service.create_session(
                app_name=app_name,
                user_id=user_id,
                state=None)        
            
        else:
            # For other session services, you can pass session_id to create_session to set a specific session id.
            new_session = await session_service.create_session(
                app_name=app_name,
                user_id=user_id,
                state=None,
                session_id=session_id, )
        
        session_id = new_session.id
        print(f"Created new session: {session_id}")

    else:
        print(f"Using existing session: {session_id}")

    # Initialize the agent runner.
    runner = Runner(agent=agent.root_agent,
                    app_name=app_name,
                    session_service=session_service)

    while True:

        query = input("\n 👤 User: ")
        if query.strip().lower() in ["exit", "quit"]:
            break

        content = types.Content(role='user', parts=[types.Part(text=query)])

        # Execute agent events asynchronously using the agent runner.
        # Provide the user_id and session_id to maintain the session. Only one session is used per conversation.
        # To force creation of a new session, pass session_id=None.
        events = runner.run_async(user_id=user_id,
                                session_id=session_id,
                                new_message=content, )

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
    Retrieve and print session properties.

    This function gets the session object from the session service using the provided
    application name, user id, and session id. It then prints key session attributes
    (id, app_name, user_id, state, events, last update time).

    Args:
        app_name (str): The application name.
        user_id (str): The user id.
        session_id (str): The session id.
        session_service (BaseSessionService): The session service instance.

    Returns:
        None
    """

    # Fetch the session from the session service using app_name, user_id, and session_id.
    session  = await session_service.get_session(app_name=app_name,
                                user_id=user_id,
                                session_id=session_id,)

    print(f"--- Examining Session Properties ---")
    print(f"ID (`id`):                {session.id}")
    print(f"Application Name (`app_name`): {session.app_name}")
    print(f"User ID (`user_id`):         {session.user_id}")
    print(f"State (`state`):           {session.state}") # Note: Only shows initial state here
    # print(f"Events (`events`):         {session.events}") # Initially empty
    print(f"Last Update (`last_update_time`): {session.last_update_time:.2f}")
    print(f"---------------------------------")

#--------------------------------[Main entry point function ]----------------------------------

if __name__ == "__main__":
    import asyncio
    import argparse

    """This script is the main entry point to run an ADK agent.
    It selects the appropriate session service based on the provided session type
    and launches the interactive agent loop.

    Args:
        --type (str): Session type. Choose 'in_memory', 'database', or 'agent_engine'.
        --app_name (str): The application name used by the agent.
        --user_id (str): The user identifier interacting with the agent.
        --session_id (str): The session identifier interacting with the agent.

    Raises:
        ValueError: If an invalid session type is provided.
    """

    load_dotenv()

    print("Running the agent...")
    print("Usage : uv run -m session.runner --type [in_memory|database|agent_engine] --app_name <app_name> --user_id <user_id> --session_id <session_id>")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--type",type=str,help="The type of session",)
    parser.add_argument("--app_name",type=str,help="The application name of this agent.",)
    parser.add_argument("--user_id",type=str,help="The user name interacting with this agent",)
    parser.add_argument("--session_id",type=str,help="The session id interacting with this agent",)

    args = parser.parse_args()

    session_service = None
    agent_engine_resource_name = None

    if args.type == "in_memory":
        session_service = InMemorySessionService()
    
    elif args.type == "database":
        db_url = "sqlite:///./adk_session.db"
        session_service = DatabaseSessionService(db_url=db_url)
    
    elif args.type == "agent_engine":
        PROJECT_ID = os.environ['GOOGLE_CLOUD_PROJECT']
        AGENT_LOCATION = os.environ['GOOGLE_CLOUD_LOCATION']
        AGENT_ENGINE_ID = os.environ['AGENT_ENGINE_ID']

        session_service = VertexAiSessionService(project=PROJECT_ID, 
                                                 location=AGENT_LOCATION,
                                                 agent_engine_id = AGENT_ENGINE_ID)
    else:
        raise ValueError("Invalid session type. Choose 'in_memory' or 'database' or 'agent_engine'.")

    asyncio.run(run_agent(session_service = session_service, 
                                 app_name = args.app_name, 
                                 user_id = args.user_id, 
                                 session_id = args.session_id ) )
