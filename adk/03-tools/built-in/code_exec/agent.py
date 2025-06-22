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
        You are a calculator agent.
        Given a mathematical expression, you write and execute Python code to calculate the result.
        The response is returned as plain text, both the Python code and the final numerical result of the execution.

        Note : When answering, Must be sure to use the same language the user used when asking the question. 

        """

    code_execution_agent = Agent(
        name = "code_execution_agent",
        model = os.getenv("MODEL"),
        description = "Performs calculations by running Python code.",
        instruction = INSTRUCTION,
        tools=[BuiltInCodeExecutor],
    )

    return code_execution_agent

root_agent = build_agent()