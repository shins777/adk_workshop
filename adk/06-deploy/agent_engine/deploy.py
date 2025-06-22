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
    주어진 에이전트와 사용자 쿼리로 ADK 애플리케이션을 초기화하고 실행합니다.

    이 함수는 Vertex AI 환경을 설정하고, 주어진 에이전트로 AdkApp 인스턴스를 생성한 뒤,
    사용자 쿼리에 대한 에이전트의 응답을 스트리밍하여 콘솔에 출력합니다.

    인자:
        root_agent (Agent): ADK 애플리케이션에 사용할 루트 에이전트
        user_id (str): 쿼리 세션의 사용자 식별자
        query (str): 에이전트가 처리할 사용자 입력 또는 질문

    반환값:
        AdkApp: 초기화된 AdkApp 인스턴스
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
    
    print(""" 사용법 : uv run -m agent_engine.deploy --query 'What is the Generative AI?' """)
    parser = argparse.ArgumentParser(description="사용자 쿼리로 ADK 에이전트를 실행합니다.")
    parser.add_argument("--query",type=str,help="이 에이전트의 애플리케이션 이름.",)
    parser.add_argument("--agent_name",type=str,help="에이전트 이름.",)
    parser.add_argument("--user_id",type=str,help="사용자 ID.",)
    parser.add_argument("--session_id",type=str,help="세션 ID.",)

    args = parser.parse_args()
    query = args.query
    agent_name = args.agent_name
    user_id = args.user_id
    session_id = args.session_id

    #1. 등록된 모든 에이전트 출력
    show_agents()

    #2. adk_app 빌드
    adk_app = build_adk_app(root_agent, user_id, query)

    #3. Agent Engine에 adk_app 배포
    display_name = agent_name
    gcs_dir_name = os.getenv("STAGING_BUCKET")
    description = "사용자 질문에 대한 AI 정보 검색 어시스턴트"
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


