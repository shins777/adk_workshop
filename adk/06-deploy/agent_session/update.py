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
    Vertex AI의 원격 에이전트 엔진을 최신 에이전트 설정으로 업데이트합니다.

    이 함수는 Vertex AI 환경을 초기화하고, 주어진 리소스 이름으로 원격 에이전트 엔진을 조회한 뒤,
    현재 에이전트, 설명, 요구사항 등으로 에이전트 엔진을 업데이트합니다.

    인자:
        resource_name (str): 업데이트할 에이전트 엔진의 리소스 이름

    반환값:
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
    
    print(""" 사용법 : uv run -m agent_session.update --agent_engine_id 4971736494105427968 """)
    
    parser = argparse.ArgumentParser(description="사용자 쿼리로 ADK 에이전트를 실행합니다.")    
    parser.add_argument("--agent_engine_id",type=str)

    args = parser.parse_args()

    agent_engine_id = args.agent_engine_id
 
    resource_name = f"projects/{os.getenv('PROJECT_NUMBER')}/locations/{os.getenv('LOCATION')}/reasoningEngines/{agent_engine_id}"

    update_remote_agent(resource_name=resource_name)

