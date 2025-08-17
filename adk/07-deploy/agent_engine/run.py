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
import argparse

from .util import get_agent_engine
from .util import show_agents

load_dotenv()

if __name__ == "__main__":

    print(""" Usage : uv run -m agent_engine.query --engine_id 2231366489594658816 --user_id forus --query 'What is the Generative AI?' """)
    
    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--engine_id",type=str,help="The engin id of agent",)
    parser.add_argument("--user_id",type=str,help="The user id",)
    parser.add_argument("--query",type=str,help="The application name of this agent.",)
    
    args = parser.parse_args()
    engine_id = args.engine_id.strip()
    user_id = args.user_id.strip()
    query = args.query.strip()

    #1. 등록된 모든 에이전트를 인쇄하세요.
    show_agents()

    #2. 원격 에이전트 엔진 인스턴스를 가져옵니다.
    
    # resource name example : PROJECT_NUMBER와 LOCATION 환경 변수를 설정해야 합니다.
    project_number = os.getenv("AGENT_ENGINE_PROJECT_NUMBER")
    location = os.getenv("GOOGLE_CLOUD_LOCATION")
    resource_name = f"projects/{project_number}/locations/{location}/reasoningEngines/{engine_id}"

    remote_agent_engine = get_agent_engine(resource_name = resource_name)

    #3. 쿼리를 실행합니다.
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