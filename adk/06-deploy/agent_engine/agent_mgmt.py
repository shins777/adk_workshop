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

from vertexai import agent_engines
from google.adk.agents import Agent

"""
This sources are related to agent engine managment with APIs. 
The code references is the following url:
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
    Retrieves an AgentEngine instance by display name or resource name.

    This function searches through the available agent engines and returns the engine
    that matches the provided display name or resource name. If no matching engine is found,
    it prints an error message.

    Args:
        display_name (str, optional): The display name of the agent engine to retrieve.
        resource_name (str, optional): The resource name of the agent engine to retrieve.

    Returns:
        agent_engines.AgentEngine: The matching AgentEngine instance if found, otherwise None.
    """
    
    # print("\n\n### Get a agent engines with display name or resource name. \n\n")

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
    Displays a list of all available agent engines.

    This function retrieves and prints information about each agent engine, including
    its display name, name, creation time, and resource name. If no agent engines are found,
    it prints a message indicating that no reasoning engines are available.

    Returns:
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
    Deletes an agent engine by its name.

    This function retrieves the agent engine with the specified name and deletes it from Vertex AI Agent Engine.
    If the deletion is successful, it prints a confirmation message. If an error occurs, it prints the error.

    Args:
        name (str): The name of the agent engine to delete.

    Returns:
        None
    """

    print("\n\n### Delete agent engines. \n\n")

    try:
        re = agent_engines.get(name)
        re.delete()
        print(f"Agent Engine deleted {name}")
    except Exception as e:
        print(e)

