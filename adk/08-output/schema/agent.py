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

import os
from dotenv import load_dotenv
from google.adk.agents import Agent

from .schema import SearchResult

load_dotenv()

def build_agent() -> Agent:
    """
    Google Search 도구 지원이 포함된 Agent 인스턴스를 생성하고 구성합니다.

    이 함수는 환경 변수를 로드하고, 에이전트의 안내 템플릿을 설정하며,
    이름, 모델, 설명, 안내문, 출력 스키마를 포함하여 Agent를 초기화합니다.
    이 에이전트는 자체 지식과 검색 기능을 모두 활용하여 사용자 문의에 답변하도록 설계되었습니다.

    반환값:
        Agent: 사용자 질의 처리가 가능한 구성된 Agent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        답변을 제공할 때는 반드시 output_schema를 정확히 따라야 합니다.
        참고: 답변 시 반드시 사용자가 질문에 사용한 언어와 동일한 언어로 답변해야 합니다.

    """

    agent = Agent(
        name = "search_agent",
        model = os.getenv("MODEL"),
        description = "사용자 질의에 답변하는 에이전트",
        instruction = INSTRUCTION,
        output_schema = SearchResult,
    )
    return agent

root_agent = build_agent()