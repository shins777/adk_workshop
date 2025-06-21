
import os 
import argparse
import asyncio
from dotenv import load_dotenv

from google.genai import types
from google.adk.sessions import VertexAiSessionService
from google.adk.runners import Runner

from agent_session import agent

load_dotenv()

#-----------------------------[call_agent]-----------------------------

def call_agent(runner, 
               user_id:str,
               session_id:str,
               query:str):
    """
    Sends a user query to the agent and prints the agent's response.

    This function constructs a message from the user's input, sends it to the agent using the provided
    runner, and iterates through the response events. When a final response is received, it prints
    the agent's answer to the console.

    Args:
        runner: The Runner instance used to execute the agent.
        user_id (str): The user identifier.
        session_id (str): The session identifier.
        query (str): The user's input or question to be processed by the agent.

    Returns:
        None
    """

    content = types.Content(role='user', parts=[types.Part(text=query)])
    
    events = runner.run(
        user_id=user_id, session_id=session_id, new_message=content)

    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print(f"\n 🤖 AI Assistant: {final_response}\n")

#-----------------------------[run_agent]-----------------------------

def run_agent(agent_engine_id:str,
                    user_id:str,
                    query:str,
                    session_id:str = None,):

    """
    Runs the agent in a conversational loop using the specified agent engine and session.

    This function creates a session for the user and application, then enters a loop
    where it prompts the user for input, sends the input to the agent, and prints the
    agent's response. The conversation continues until the user types "exit".

    Args:
        agent_engine_id (str): The identifier for the agent engine (app name).
        user_id (str): The user identifier.
        query (str): The initial user query (not used in the loop).
        session_id (str, optional): The session identifier. If not provided, a new session is created.

    Returns:
        None
    """

    # Create the ADK runner with VertexAiSessionService
    session_service = VertexAiSessionService(os.getenv("PROJECT_ID"), os.getenv("LOCATION"))

    runner = Runner(
        agent=agent.root_agent,
        app_name=agent_engine_id,
        session_service=session_service)

    # Create a session
    session = session_service.create_session(
        app_name=agent_engine_id,
        user_id=user_id,
        session_id=session_id)

    while True:
        query = input("\n 👤 User: ")
        if query.lower() == "exit":
            break

        call_agent(runner, 
                   user_id = user_id, 
                   session_id = session.id, 
                   query = query)

#-----------------------------[__main__]-----------------------------

if __name__ == "__main__":
    
    print(""" Usage : uv run -m agent_session.session --agent_engine_id 112774708637728768 --user_id forus --session_id 8517270617299353600 """)
    
    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    
    parser.add_argument("--agent_engine_id",type=str)
    parser.add_argument("--user_id",type=str)
    parser.add_argument("--session_id",type=str)
    parser.add_argument("--query",type=str)
    
    args = parser.parse_args()

    agent_engine_id = args.agent_engine_id
    query = args.query
    user_id = args.user_id
    session_id = args.session_id

    run_agent(agent_engine_id=args.agent_engine_id,
                          user_id=args.user_id,
                          session_id=args.session_id,
                          query=args.query)
    
