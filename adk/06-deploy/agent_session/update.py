import os 
import argparse
import asyncio
from dotenv import load_dotenv

from vertexai import agent_engines
import vertexai

from agent_session import agent

from .agent_mgmt import get_agent_engine

load_dotenv()

#-----------------------------[update_remote_agent]-----------------------------

def update_remote_agent(resource_name:str):

    """
    Updates a remote agent engine on Vertex AI with the latest agent configuration.

    This function initializes the Vertex AI environment, retrieves the remote agent engine
    using the provided resource name, and updates the agent engine with the current agent,
    description, requirements, and other configuration options.

    Args:
        resource_name (str): The resource name of the agent engine to update.

    Returns:
        None
    """

    # Initialize Vertex AI to deploy Agent Engine. 
    vertexai.init(
        project=os.getenv("PROJECT_ID"),
        location=os.getenv("LOCATION"),
        staging_bucket=os.getenv("STAGING_BUCKET"),
    )

    requirements = [
        "google-adk[vertexai]",
        "google-cloud-aiplatform[adk,agent-engines]",
        "cloudpickle==3.0",
        "python-dotenv",
    ]
    print(f"\n Resource Name : {resource_name}\n")
    remote_agent_engine = get_agent_engine(resource_name = resource_name)
    print(f"\n Remote Agent Engine : {remote_agent_engine}\n")
    
    agent_engines.update(resource_name=remote_agent_engine.name, 
                         agent_engine=agent.root_agent, 
                         gcs_dir_name = os.getenv("STAGING_BUCKET"),
                         description = "AI information search assistant to user's question",                        
                         requirements=requirements)

#-----------------------------[__main__]-----------------------------

if __name__ == "__main__":
    
    print(""" Usage : uv run -m agent_session.update --agent_engine_id 4971736494105427968 """)
    
    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")    
    parser.add_argument("--agent_engine_id",type=str)

    args = parser.parse_args()

    agent_engine_id = args.agent_engine_id
 
    resource_name = f"projects/{os.getenv('PROJECT_NUMBER')}/locations/{os.getenv('LOCATION')}/reasoningEngines/{agent_engine_id}"

    update_remote_agent(resource_name=resource_name)
                        
                        