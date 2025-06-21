import os
import argparse
from dotenv import load_dotenv

import vertexai
from vertexai import agent_engines

load_dotenv()

#-----------------------------[create_agent_engine]-----------------------------

def create_agent_engine(agent_name:str,
                        description:str=None):
    """
    Creates and deploys an agent engine on Vertex AI.

    This function initializes the Vertex AI environment using environment variables,
    then creates an agent engine instance with the specified display name and description.
    The agent engine is stored in the Google Cloud Storage directory specified by the
    STAGING_BUCKET environment variable.

    Args:
        agent_name (str): The display name for the agent engine.
        description (str, optional): A description for the agent engine.

    Returns:
        agent_engines.AgentEngine: The created agent engine instance.
    """

    # Initialize Vertex AI to deploy Agent Engine. 
    vertexai.init(
        project=os.getenv("PROJECT_ID"),
        location=os.getenv("LOCATION"),
        staging_bucket=os.getenv("STAGING_BUCKET"),
    )

    # Create an agent engine instance
    agent_engine = agent_engines.create(
        display_name=agent_name,
        gcs_dir_name=os.getenv("STAGING_BUCKET"),
        description=description,
    )

    return agent_engine

#-----------------------------[__main__]-----------------------------

if __name__ == "__main__":
    
    print(""" Usage : uv run -m agent_session.engine --agent_name forusone """)
    
    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    
    parser.add_argument("--agent_name",type=str)
    
    args = parser.parse_args()

    agent_engine = create_agent_engine(agent_name=args.agent_name)
    print(f"Agent Engine created : {agent_engine}")
    
