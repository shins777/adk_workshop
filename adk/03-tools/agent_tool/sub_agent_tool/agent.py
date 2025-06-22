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

def build_agent() -> Agent:
    """
    긍정/부정 비평 작업을 위한 서브 에이전트 도구가 포함된 루트 Agent 인스턴스를 생성하고 구성합니다.

    이 함수는 환경 변수를 로드하고, 에이전트의 안내 템플릿을 정의하며,
    이름, 모델, 설명, 안내문을 포함하여 Agent를 초기화합니다. 또한 긍정/부정 비평을 위한
    서브 에이전트 도구를 연결하여, 루트 에이전트가 사용자 요청에 따라 적절한 도구로
    비평 작업을 위임할 수 있도록 합니다.

    반환값:
        Agent: 서브 에이전트 도구가 포함되어 사용자 질의 처리가 가능한 구성된 Agent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        답변 시 반드시 사용자가 질문에 사용한 언어로 답변해야 합니다.
        
        아래의 흐름에 따라 답변을 제공하세요.

        1. 사용자가 질문을 입력하면, 먼저 질문의 의도를 정리해야 합니다. 반드시 "질문 의도:"라고 말한 뒤 질문의 의도를 정리하세요.

        2. 사용자의 질문에 따라 다음과 같이 도구를 활용해 답변을 제공해야 합니다.
            2-1. 사용자가 긍정적 비평을 요청하면 positive_critic 도구를 사용해 긍정적 비평을 작성하세요.
            2-2. 사용자가 부정적 비평을 요청하면 negative_critic 도구를 사용해 부정적 비평을 작성하세요.
            2-3. 사용자가 긍정적/부정적 비평을 모두 요청하면 두 도구(positive_critic, negative_critic)를 모두 사용해 각각의 비평을 작성하세요.
        
    """

    agent = Agent(
        name = "root_agent",
        model = os.getenv("MODEL"),
        description = "사용자 질의에 답변하는 에이전트",
        instruction = INSTRUCTION,
        tools = [AgentTool(agent=positive_critic),
                AgentTool(agent=negative_critic)]
    )

    return agent

root_agent = build_agent()
