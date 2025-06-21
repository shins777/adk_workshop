import asyncio
import time
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from state import agent

#--------------------------------[run_agent]----------------------------------

async def run_agent( app_name: str,
                     user_id: str,
                     session_id: str,):

    """
    Runs the agent in a conversational loop while displaying session state changes.

    This function creates a session for the user and application, then enters a loop
    where it prompts the user for input, sends the input to the agent, and prints the
    agent's response. After each interaction, it retrieves and displays the updated
    session state to show how the agent's state evolves over time.

    Args:
        app_name (str): The name of the application.
        user_id (str): The user identifier.
        session_id (str): The session identifier.

    Returns:
        None
    """

    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=app_name, 
                                            user_id=user_id, 
                                            session_id=session_id)

    runner = Runner(agent=agent.root_agent,
                    app_name=app_name,
                    session_service=session_service)
    
    print(f"Initial state: {session.state}")

    while True:

        user_input = input("\n 👤 User: ")
        if user_input.lower().strip() in ["exit", "quit", "bye"]:
            break

        content = types.Content(role='user', parts=[types.Part(text=user_input)])

        events = runner.run_async(user_id=user_id,
                                session_id=session_id,
                                new_message=content,)

        async for event in events:
            if event.is_final_response():
                final_response = event.content.parts[0].text            
                print("\n 🤖 AI Assistant: " + final_response)

        updated_session = await session_service.get_session(app_name = app_name, 
                                                     user_id = user_id, 
                                                     session_id = session_id)

        print(f"\nState after agent run: {updated_session.state}")
        print(f"\nState after agent run - last_turn : {updated_session.state['last_turn']}")

#--------------------------------[__main__]----------------------------------

if __name__ == "__main__":
    import asyncio
    import argparse

    print("Running the agent...")
    print("Usage : uv run -m state.output_key --app_name <app_name> --user_id <user_id> --session_id <session_id>")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--app_name",type=str,help="The application name of this agent.",)
    parser.add_argument("--user_id",type=str,help="The user name interacting with this agent",)
    parser.add_argument("--session_id",type=str,help="The session id to identify the session of this agent",)
    args = parser.parse_args()

    asyncio.run(run_agent(app_name = args.app_name, 
                          user_id = args.user_id, 
                          session_id = args.session_id,))
    