import os
from dotenv import load_dotenv

from google.adk.sessions import InMemorySessionService
from google.adk.sessions import DatabaseSessionService
from google.adk.sessions import VertexAiSessionService

from session import runner

if __name__ == "__main__":
    import asyncio
    import argparse

    load_dotenv()

    print("Running the agent...")
    print("Usage : uv run -m session.main --type <session_type> --app_name <app_name> --user_id <user_id> --session_id <session_id>")
    print("Usage : session type : in_memory, database, vertexai")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--type",type=str,help="The type of session",)
    parser.add_argument("--app_name",type=str,help="The application name of this agent.",)
    parser.add_argument("--user_id",type=str,help="The user name interacting with this agent",)
    parser.add_argument("--session_id",type=str,help="The session id to identify the session of this agent",)
    args = parser.parse_args()

    session_service = None
    agent_engine_app_name = None
    
    if args.type == "in_memory":
        session_service = InMemorySessionService()
    
    elif args.type == "database":
        db_url = "sqlite:///./agent_session.db"
        session_service = DatabaseSessionService(db_url=db_url)
    
    elif args.type == "vertexai":
        PROJECT_ID = os.environ['PROJECT_ID']
        LOCATION = os.environ['LOCATION']
        AGENT_ENGINE_ID = os.environ['AGENT_ENGINE_ID']
        
        agent_engine_app_name = f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{AGENT_ENGINE_ID}"
        session_service = VertexAiSessionService(project=PROJECT_ID, location=LOCATION)    
    
    else:
        raise ValueError("Invalid session type. Choose 'in_memory' or 'database' or 'vertexai'.")

    asyncio.run(runner.run_agent(session_service = session_service, 
                                 app_name = args.app_name, 
                                 user_id = args.user_id, 
                                 session_id = args.session_id,
                                 agent_engine_app_name = agent_engine_app_name))
    