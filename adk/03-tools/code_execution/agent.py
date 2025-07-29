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
from google.adk.code_executors import BuiltInCodeExecutor

load_dotenv()

def build_agent() -> Agent:

    """
    내장 코드 실행 툴이 포함된 Agent 인스턴스를 생성하고 설정합니다.

    이 함수는 환경 변수를 불러오고, 에이전트의 지시문 템플릿을 정의하며,
    이름, 모델, 설명, 지시문, 내장 코드 실행 툴을 포함해 Agent를 초기화합니다.
    이 에이전트는 수학식을 받아 파이썬 코드로 계산하고, 코드와 결과를 평문으로 반환하도록 설계되었습니다.

    반환값:
        Agent: 코드 실행 질의를 처리할 준비가 된 설정된 Agent 인스턴스
    """

    INSTRUCTION = """
        당신은 계산기 에이전트입니다.
        수학식이 주어지면, 결과를 계산하는 Python 코드를 작성하고 Built-In Code Executor 을 통해서 실행합니다.
        응답은 Python 코드와 실행의 최종 수치 결과 모두 일반 텍스트로 반환됩니다.
        
        참고: 답변 시에는 사용자가 질문할 때 사용한 것과 동일한 언어를 사용해야 합니다.

        """

    code_execution_agent = Agent(
        name = "code_execution_agent",
        model = os.getenv("GOOGLE_GENAI_MODEL"),
        description = "프로그램 코드를 실행하여 계산을 수행후 결과를 반환하는 에이전트",
        instruction = INSTRUCTION,
        code_executor=BuiltInCodeExecutor(),   
    )   

    return code_execution_agent

root_agent = build_agent()