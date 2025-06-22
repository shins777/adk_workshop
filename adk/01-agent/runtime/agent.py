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
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agent import positive_critic, negative_critic

load_dotenv()

def build_agent(type:str = "agent") -> Agent:
    """
    비평 작업을 위한 서브 에이전트를 포함하는 루트 Agent 인스턴스를 생성하고 설정합니다.

    이 함수는 환경 변수를 불러오고, 에이전트의 지시문 템플릿을 정의하며,
    이름, 모델, 설명, 지시문을 포함해 Agent를 초기화합니다. 또한
    긍정 및 부정 비평을 위한 서브 에이전트를 연결하여 루트 에이전트가
    사용자 요청에 따라 특정 비평 작업을 위임할 수 있도록 합니다.

    반환값:
        Agent: 사용자 질의를 처리할 준비가 된 서브 에이전트가 포함된 설정된 Agent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        다음 흐름에 따라 답변을 제공하세요.

        1. 사용자가 질문을 입력하면, 먼저 질문의 의도를 정리해야 합니다. 다시 한번 "질문 의도"라고 말하고 질문의 의도를 정리하세요.

        2. 사용자의 질문에 따라 다음과 같이 서브 에이전트를 사용하여 답변을 제공해야 합니다.
            2-1. 사용자가 긍정적인 비평을 요청하면, positive_critic 에이전트(또는 툴)를 사용하여 긍정적인 비평을 작성하세요.
            2-2. 사용자가 부정적인 비평을 요청하면, negative_critic 에이전트(또는 툴)를 사용하여 부정적인 비평을 작성하세요.
            2-3. 사용자가 긍정적 비평과 부정적 비평을 모두 요청하면, 두 에이전트(또는 툴) (positive_critic, negative_critic)를 모두 사용하여 각 비평을 작성하세요.

        참고: 답변 시 반드시 사용자가 질문한 언어와 동일한 언어로 답변해야 합니다.
        
    """

    if type == "agent":
        agent = Agent(
            name = "root_agent",
            model = os.getenv("MODEL"),
            description = "Agents that answer questions about user query",
            instruction = INSTRUCTION,
            sub_agents = [positive_critic, negative_critic],
        )        
        return agent
    
    elif type == "agent_tool":
        agent_tool = Agent(
            name = "root_agent_tool",
            model = os.getenv("MODEL"),
            description = "Agents that answer questions about user query",
            instruction = INSTRUCTION,
            tools = [AgentTool(agent=positive_critic), AgentTool(agent=negative_critic)]
        )        
        return agent_tool
    else:
        print("type : 'agent' or 'agent_tool'")
    
type = "agent" # type : "agent" or "agent_tool"

root_agent = build_agent(type)