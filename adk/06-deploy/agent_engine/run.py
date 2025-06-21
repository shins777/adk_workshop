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

from .agent_mgmt import get_agent_engine
from .agent_mgmt import show_agents

load_dotenv()

if __name__ == "__main__":
    
    # resource name example : 
    #   "projects/7215332243942/locations/us-central1/reasoningEngines/112774723411728768"

    print(""" Usage : uv run -m agent_engine.run --resource_name projects/721521243942/locations/us-central1/reasoningEngines/112774708637728768 --user_id forus --session_id 8517270617299353600 --query 'What is the Generative AI?' """)
    
    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    
    parser.add_argument("--resource_name",type=str,help="The resource_name of agent",)

    parser.add_argument("--user_id",type=str,help="The user id",)
    parser.add_argument("--session_id",type=str,help="The session_id",)
    parser.add_argument("--query",type=str,help="The application name of this agent.",)
    
    args = parser.parse_args()
    query = args.query
    resource_name = args.resource_name
    user_id = args.user_id
    session_id = args.session_id

    #1. Print all registered agents.
    show_agents()

    #2. Get the remote agent engine instance.
    remote_agent_engine = get_agent_engine(resource_name = resource_name)

    #3. Execute the query.
    print("### Agent REMOTE unit test")

    if remote_agent_engine is not None:
        
        print(f"\n Display name : {remote_agent_engine.display_name}\n")
        print(f"\n Reource name : {remote_agent_engine.resource_name}\n")

        print(f"\n 👤 User: {query}\n")
        
        #Create a event for unit test.    
        events = remote_agent_engine.stream_query(user_id=user_id, 
                                                  message=query)
        for event in events:
            response = event['content']['parts'][0]['text']
            print(f"\n 🤖 Local AI Assistant: {response}\n")


    else:
        print("None of agent found.")