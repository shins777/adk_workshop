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
    Vertex AI에 에이전트 엔진을 생성 및 배포합니다.

    이 함수는 환경 변수로 Vertex AI 환경을 초기화한 뒤,
    지정한 표시 이름과 설명으로 에이전트 엔진 인스턴스를 생성합니다.
    에이전트 엔진은 STAGING_BUCKET 환경 변수에 지정된 Google Cloud Storage 디렉토리에 저장됩니다.

    인자:
        agent_name (str): 에이전트 엔진의 표시 이름
        description (str, optional): 에이전트 엔진 설명

    반환값:
        agent_engines.AgentEngine: 생성된 에이전트 엔진 인스턴스
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
    
    print(""" 사용법 : uv run -m agent_session.engine --agent_name forusone """)
    
    parser = argparse.ArgumentParser(description="사용자 쿼리로 ADK 에이전트를 실행합니다.")
    
    parser.add_argument("--agent_name",type=str)
    
    args = parser.parse_args()

    agent_engine = create_agent_engine(agent_name=args.agent_name)
    print(f"Agent Engine created : {agent_engine}")

