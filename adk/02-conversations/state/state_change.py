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
    Demonstrates explicit state change in a session using the ADK event system.

    This function creates a session with an initial state, appends a system event to
    update the session state (such as adding a timestamp), and prints the state before
    and after the event to show how the session state changes over time.

    Args:
        app_name (str): The name of the application.
        user_id (str): The user identifier.
        session_id (str): The session identifier.

    Returns:
        None
    """

    session_service = InMemorySessionService()

    # define init state.
    init_state = {
        "task_status": "active", 
    }

    session = await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id,
        state=init_state
    )
    
    print(f"1. Initial state: {session.state}")

    # change the state
    state_changes = {
        "task_status": "active", 
        "timestamp": time.time(),   
    }

    system_event = Event(
        invocation_id = "change-state",
        author = "system", # Or 'agent', 'tool' etc.
        actions = EventActions(state_delta=state_changes),
        timestamp = time.time()
    )

    # change the state with append_event
    await session_service.append_event(session, system_event)

    print("2. Append new changed event to explicit state delta.")

    updated_session = await session_service.get_session(app_name=app_name,
                                                user_id=user_id, 
                                                session_id=session_id)
    
    print(f"3. State after event sent: {updated_session.state}")

if __name__ == "__main__":

    load_dotenv()

    print("Running the agent...")
    print("Usage : python main.py --app_name <app_name> --user_id <user_id> --session_id <session_id>")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--app_name",type=str,help="The application name of this agent.",)
    parser.add_argument("--user_id",type=str,help="The user name interacting with this agent",)
    parser.add_argument("--session_id",type=str,help="The session id to identify the session of this agent",)
    args = parser.parse_args()

    asyncio.run(run_agent(app_name = args.app_name, 
                          user_id = args.user_id, 
                          session_id = args.session_id,))
    