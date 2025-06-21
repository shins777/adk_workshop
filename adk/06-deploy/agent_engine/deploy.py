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

import os
from dotenv import load_dotenv
import argparse
import asyncio

import vertexai
from vertexai.preview.reasoning_engines import AdkApp
from google.adk.agents import Agent

from .agent import root_agent
from .agent_mgmt import deploy_agent
from .agent_mgmt import get_agent_engine
from .agent_mgmt import show_agents
from .agent_mgmt import delete_agent

load_dotenv()

def build_adk_app(root_agent:Agent,
              user_id:str,
              query:str,):
    """
    Initializes and runs an ADK application with the provided agent and user query.

    This function sets up the Vertex AI environment, creates an AdkApp instance with the given agent,
    and streams the agent's response to the provided user query. It prints each response outcome to the console.

    Args:
        root_agent (Agent): The root agent to be used in the ADK application.
        user_id (str): The user identifier for the query session.
        query (str): The user's input or question to be processed by the agent.

    Returns:
        AdkApp: The initialized AdkApp instance.
    """

    print("### Agent LOCAL unit test")
    print(f"\n 👤 User: {query}\n")

    # Initialize Vertex AI to deploy Agent Engine. 
    vertexai.init(
        project=os.getenv("PROJECT_ID"),
        location=os.getenv("LOCATION"),
        staging_bucket=os.getenv("STAGING_BUCKET"),
    )
    # Create a adk_app with root_agent. 
    adk_app = AdkApp(agent=root_agent)

    #Create a event for unit test.    
    events = adk_app.stream_query(user_id=user_id,
                                  message=query)
    for event in events:
        response = event['content']['parts'][0]['text']
        print(f"\n 🤖 Local AI Assistant: {response}\n")

    return adk_app

if __name__ == "__main__":
    
    print(""" Usage : uv run -m agent_engine.deploy --query 'What is the Generative AI?' """)
    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--query",type=str,help="The application name of this agent.",)
    parser.add_argument("--agent_name",type=str,help="The name of agent",)
    parser.add_argument("--user_id",type=str,help="The user id",)
    parser.add_argument("--session_id",type=str,help="The session_id",)

    args = parser.parse_args()
    query = args.query
    agent_name = args.agent_name
    user_id = args.user_id
    session_id = args.session_id

    #1. Print all registered agents.
    show_agents()

    #2. Build a adk_app.
    adk_app = build_adk_app(root_agent, user_id, query)

    #3. Deploy the adk_app on Agent Engine.
    display_name = agent_name
    gcs_dir_name = os.getenv("STAGING_BUCKET")
    description = "AI information search assistant to user's question"
    requirements = [
        "google-adk[vertexai]",
        "google-cloud-aiplatform[adk,agent-engines]",
        "cloudpickle==3.0",
        "python-dotenv",
    ]

    extra_packages = []
    remote_agent = deploy_agent(agent = adk_app, 
                                display_name = display_name, 
                                gcs_dir_name = gcs_dir_name,
                                description = description,
                                requirements = requirements,
                                extra_packages = extra_packages)


