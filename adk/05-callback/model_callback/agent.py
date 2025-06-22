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

from .callback import callback_before_model
from .callback import callback_after_model

load_dotenv()

#--------------------------------[build_agent]----------------------------------

def build_agent() -> Agent:
    """
    사용자 질문에 답변하는 에이전트 인스턴스를 생성하고 설정합니다.

    이 함수는 환경 변수를 불러오고, 한글로 된 에이전트 지시문을 정의하며,
    이름, 모델, 설명, 지시문을 포함해 Agent를 초기화합니다. 또한 모델 실행 전/후 콜백도 연결합니다.

    반환값:
        Agent: 사용자 질문을 처리할 준비가 된 설정된 Agent 인스턴스
    """

    INSTRUCTION = """
        You are an AI agent who provides answers to users' questions.
        When providing answers, please respond concisely and clearly in the following structure:
        - Question content:
        - Question intent:
        - Answer content:

        Note: Answer casual conversation questions natually without any special format.

    """

    agent = Agent(
        name = "root_agent",
        model = os.getenv("MODEL"),
        description = "Agents that answer questions about user inquiries",
        instruction = INSTRUCTION,
        before_model_callback=callback_before_model,
        after_model_callback=callback_after_model 
    )

    return agent

# Set the agent as a root_agent which could be imported from runner. 
root_agent = build_agent()