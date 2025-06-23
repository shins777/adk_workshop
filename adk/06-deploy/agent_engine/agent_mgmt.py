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

from vertexai import agent_engines
from google.adk.agents import Agent

"""
이 소스는 API를 활용한 에이전트 엔진 관리와 관련되어 있습니다.
코드 참조는 다음 URL을 기반으로 합니다:
   https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/manage/overview
"""

#--------------------------------[deploy_agent]----------------------------------

def deploy_agent(agent: Agent,
                 display_name: str, 
                 gcs_dir_name: str,
                 description: str = None,
                 requirements: list = None,
                 extra_packages: list = None) -> agent_engines.AgentEngine:
    """
    에이전트를 Vertex AI Agent Engine에 배포합니다.

    이 함수는 주어진 에이전트와 설정 옵션을 사용해 에이전트 엔진을 생성 및 배포합니다.
    표시 이름, GCS 디렉토리, 설명, 파이썬 요구사항, 추가 패키지 등을 지정할 수 있습니다.

    인자:
        agent (Agent): 배포할 에이전트 인스턴스
        display_name (str, optional): 에이전트 엔진의 표시 이름
        gcs_dir_name (str, optional): 에이전트 파일을 저장할 Google Cloud Storage 디렉토리
        description (str, optional): 에이전트 엔진 설명
        requirements (list, optional): 파이썬 패키지 요구사항 리스트
        extra_packages (list, optional): 추가로 설치할 파이썬 패키지 리스트

    반환값:
        agent_engines.AgentEngine: 배포된 AgentEngine 인스턴스
    """

    print("\n\n### Start to deploy agent engine. \n\n")
    remote_agent = agent_engines.create(
                agent,
                display_name=display_name,
                gcs_dir_name = gcs_dir_name,
                description=description,
                requirements=requirements,
                extra_packages = extra_packages
    )
    return remote_agent


#--------------------------------[get_agent_engine]----------------------------------

def get_agent_engine(display_name = None,
                     resource_name = None) -> agent_engines.AgentEngine:
    """
    display_name 또는 resource_name 으로 AgentEngine 인스턴스를 조회합니다.

    이 함수는 사용 가능한 에이전트 엔진을 순회하며, 주어진 display_name 또는 resource_name 과 일치하는 엔진을 반환합니다. 일치하는 엔진이 없으면 에러 메시지를 출력합니다.

    인자:
        display_name (str, optional): 조회할 에이전트 엔진의 display_name
        resource_name (str, optional): 조회할 에이전트 엔진의 resource_name

    반환값:
        agent_engines.AgentEngine: 일치하는 AgentEngine 인스턴스(없으면 None)
    """
    
    print("\n\n### Get a agent engines with display name or resource name. \n\n")

    try:
        for agent in agent_engines.list():
            
            print(f"Agents List : {agent.display_name}:{agent.resource_name}")
            
            if agent.display_name != None and agent.display_name == display_name:
                print(f"Agent found a engine with {display_name}")

                return agent_engines.get(agent.name)

            elif agent.resource_name != None and agent.resource_name == resource_name:
                print(f"Agent found a engine with resource name {resource_name}")

                return agent_engines.get(agent.resource_name)

            else:
                print("No such reasoning engine or invalid display name or resouce name")
    except Exception as e:
        print(e)

#--------------------------------[show_agents]----------------------------------

def show_agents():
    """
    사용 가능한 모든 에이전트 엔진 목록을 출력합니다.

    이 함수는 각 에이전트 엔진의 표시 이름, 이름, 생성 시간, 리소스 이름 정보를 출력합니다.
    에이전트 엔진이 없으면 관련 메시지를 출력합니다.

    반환값:
        None
    """

    print("\n\n### Show agent engines. \n\n")

    try:
        if not agent_engines.list():
            print("No reasoning engines")

        for idx, agent in enumerate(agent_engines.list()):
            print(f"Agent {idx}: \n\tDisplay Name [{agent.display_name}] \n\tName [{agent.name}] \n\tCreation Time [{agent.create_time}] \n\tResource Name [{agent.resource_name}]\n")

    except Exception as e:
        print(e)


#--------------------------------[delete_agent]----------------------------------

def delete_agent(name):
    """
    이름으로 에이전트 엔진을 삭제합니다.

    이 함수는 지정한 이름의 에이전트 엔진을 조회하여 Vertex AI Agent Engine에서 삭제합니다.
    삭제가 성공하면 확인 메시지를 출력하고, 에러 발생 시 에러를 출력합니다.

    인자:
        name (str): 삭제할 에이전트 엔진의 이름

    반환값:
        None
    """

    print("\n\n### Delete agent engines. \n\n")

    try:
        re = agent_engines.get(name)
        re.delete()
        print(f"Agent Engine deleted {name}")
    except Exception as e:
        print(e)

