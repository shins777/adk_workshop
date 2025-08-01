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

from .callback import callback_before_agent
from .callback import callback_after_agent

load_dotenv()

#--------------------------------[build_agent]----------------------------------

def build_agent()->Agent:
    """
    사용자 질문에 답변하도록 설정된 AI 에이전트를 생성해 반환합니다.
    이 에이전트는 환경 변수 'MODEL'에 지정된 모델을 사용하며,
    간결하고 구조화된 답변을 보장하는 지시문 템플릿으로 초기화됩니다.
    또한 추가 처리를 위한 전/후처리 콜백도 연결됩니다.

    반환값:
        Agent: 사용자 질문을 처리할 준비가 된 Agent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변하는 AI 에이전트입니다.
        답변을 제공할 때는 아래와 같은 구조로 간결하고 명확하게 작성해 주세요:
        - 질문 내용:
        - 질문 의도:
        - 답변 내용:
        참고: 일상적인 대화성 질문에는 별도의 형식 없이 자연스럽게 답변하세요.
    """

    agent = Agent(
        name = "root_agent",
        model = os.getenv("GOOGLE_GENAI_MODEL"),
        description = "사용자 문의에 대해 답변하는 에이전트입니다.",
        instruction = INSTRUCTION,
        before_agent_callback=callback_before_agent,
        after_agent_callback=callback_after_agent 
    )
    return agent

root_agent = build_agent()
