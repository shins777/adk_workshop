import os 
import argparse
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.tools import google_search

from vertexai import agent_engines
import vertexai

from operation import util

load_dotenv()

#-----------------------------[update_remote_agent]-----------------------------

def build_agent() -> Agent:
    """
    이 함수는 사용자 질문에 답변하는 기본 Agent 인스턴스를 생성하고 설정하는 역할을 합니다.
    함수내에서는 환경 변수를 불러오고, 에이전트의 지시문 템플릿을 정의하며, 이름, 모델, 설명, 지시문을 포함해 Agent를 초기화합니다. 
    
    반환값:
        Agent: 사용자 질문을 처리할 준비가 된 설정된 Agent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변하는 AI 에이전트입니다.
        답변을 제공할 때는 질문에 대한 이해를 설명하고 간결하고 명확하게 응답하세요
    """

    agent = Agent(
        name = "basic_agent",
        model = os.getenv("GOOGLE_GENAI_MODEL"),
        description = "사용자 질문에 대해 답변하는 에이전트",
        instruction = INSTRUCTION,
        tools = [google_search],
    )
    return agent


def update_remote_agent(agent_engine_id:str):

    """
    Vertex AI의 원격 에이전트 엔진을 최신 에이전트 설정으로 업데이트합니다.

    이 함수는 Vertex AI 환경을 초기화하고, 주어진 리소스 이름으로 원격 에이전트 엔진을 조회한 뒤,
    현재 에이전트, 설명, 요구사항 등으로 에이전트 엔진을 업데이트합니다.

    인자:
        agent_engine_id (str): 업데이트 할 agent_engine_id

    반환값:
        None
    """

    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
    AGENT_ENGINE_BUCKET = os.getenv("AGENT_ENGINE_BUCKET")

    # Initialize Vertex AI to deploy Agent Engine. 
    vertexai.init(
        project=PROJECT_ID,
        location=LOCATION,
        staging_bucket=AGENT_ENGINE_BUCKET,
    )

    requirements = [
        "google-adk[vertexai]",
        "google-cloud-aiplatform[adk,agent-engines]",
        "cloudpickle==3.0",
        "python-dotenv",
    ]

        # resource name example : PROJECT_NUMBER와 LOCATION 환경 변수를 설정해야 합니다.
    project_number = os.getenv("AGENT_ENGINE_PROJECT_NUMBER")
    location = os.getenv("GOOGLE_CLOUD_LOCATION")
    
    resource_name = f"projects/{project_number}/locations/{location}/reasoningEngines/{agent_engine_id}"    
    print(f"\n Resource Name : {resource_name}\n")
    remote_agent_engine = util.get_agent_engine(resource_name = resource_name)
    print(f"\n Remote Agent Engine : {remote_agent_engine}\n")

    # Build the agent
    print("\n\n### Start to build agent engine. \n\n")    
    root_agent = build_agent()

    agent_engines.update(resource_name=remote_agent_engine.name, 
                         agent_engine=root_agent, 
                         gcs_dir_name = os.getenv("AGENT_ENGINE_BUCKET"),
                         description = "AI information search assistant to user's question",                        
                         requirements=requirements)

#-----------------------------[__main__]-----------------------------

if __name__ == "__main__":
    
    print(""" 사용법 : uv run -m operation.update --agent_engine_id 4971736494105427968 """)
    
    parser = argparse.ArgumentParser(description="사용자 쿼리로 ADK 에이전트를 실행합니다.")    
    parser.add_argument("--agent_engine_id",type=str)

    args = parser.parse_args()
    agent_engine_id = args.agent_engine_id
 

    update_remote_agent(agent_engine_id=agent_engine_id)

