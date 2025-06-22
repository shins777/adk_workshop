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

from .sub_agent import positive_critic, negative_critic

load_dotenv()

def build_agent():
    """
    긍정 및 부정 비평을 위한 서브 에이전트와 함께 Agent 인스턴스를 생성하고 설정합니다.

    이 함수는 에이전트의 instruction 템플릿을 정의하고, 이름, 모델, 설명, instruction,
    그리고 긍정/부정 비평용 서브 에이전트로 Agent를 초기화합니다.
    에이전트는 사용자 질문에 대해 적절한 서브 에이전트에 비평 작업을 위임하고,
    지정된 구조에 따라 답변을 포맷하도록 설계되어 있습니다.

    반환값:
        Agent: 비평 서브 에이전트와 함께 사용자 질의 처리가 가능한 설정된 Agent 인스턴스
    """

    SYSTEM_INSTRUCTION = """
        답변 시 반드시 사용자가 질문할 때 사용한 언어로 답변해야 합니다.
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        아래의 흐름에 따라 답변을 작성하세요.
          1. 사용자가 질문을 입력하면, 먼저 질문의 의도를 정리해야 합니다. 반드시 \"질문 의도:\"라고 말한 뒤 질문의 의도를 정리하세요.
          2. 사용자의 질문에 따라 다음과 같이 서브 에이전트를 활용해 답변을 작성해야 합니다.
             2-1. 사용자가 긍정적 비평을 요청하면 positive_critic 에이전트를 사용해 긍정적 비평을 작성하세요.
             2-2. 사용자가 부정적 비평을 요청하면 negative_critic 에이전트를 사용해 부정적 비평을 작성하세요.
             2-3. 사용자가 긍정/부정 비평 모두를 요청하면 두 에이전트(positive_critic, negative_critic)를 모두 사용해 각각의 비평을 작성하세요. """

    agent = Agent(
        name = "Search_agent",  # 사용자 질의에 답변하는 에이전트 이름
        model = os.getenv("MODEL"),
        description = "사용자 질의에 대해 답변하는 에이전트입니다.",
        global_instruction = SYSTEM_INSTRUCTION,
        instruction = INSTRUCTION,
        sub_agents = [positive_critic, negative_critic],
    )        
    return agent

root_agent = build_agent()
