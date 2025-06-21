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
    session_id: str,
    agent_engine_app_name: str = None
):
    """
    Runs the agent in a session-aware conversational loop.

    This function checks for existing sessions for the user and application. If a session exists,
    it continues the most recent session; otherwise, it creates a new session. The function then
    enters a loop, prompting the user for input, sending the input to the agent, and printing the
    agent's response. Session state and events are printed after each interaction.

    Args:
        session_service (BaseSessionService): The session service for managing user sessions.
        app_name (str): The name of the application.
        user_id (str): The user identifier.
        session_id (str): The session identifier.
        agent_engine_app_name (str, optional): The app name for the agent engine, if applicable.

    Returns:
        None
    """

    # Check if the session service is vertex ai agent engine.
    if agent_engine_app_name != None:
        app_name = agent_engine_app_name

    existing_sessions = await session_service.list_sessions(
        app_name=app_name,
        user_id=user_id,
    )

    if existing_sessions and len(existing_sessions.sessions) > 0:
        # Use the most recent session
        session_id = existing_sessions.sessions[0].id
        print(f"Continuing existing session: {session_id}")
    else:
        # Create a new session with initial state
        new_session = await session_service.create_session(
            app_name=app_name,
            user_id=user_id,
            state=None,
        )
        session_id = new_session.id
        print(f"Created new session: {session_id}")

    
    runner = Runner(agent=agent.root_agent,
                    app_name=app_name,
                    session_service=session_service)

    while True:

        query = input("\n 👤 User: ")
        if query.lower() == "exit":
            break

        content = types.Content(role='user', parts=[types.Part(text=query)])

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
    Retrieves and prints the properties of a session.

    This function fetches the session object from the session service using the provided
    application name, user ID, and session ID. It then prints key session properties,
    including the session ID, application name, user ID, state, events, and last update time.

    Args:
        app_name (str): The name of the application.
        user_id (str): The ID of the user.
        session_id (str): The ID of the session.
        session_service (BaseSessionService): The session service instance.

    Returns:
        None
    """

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

