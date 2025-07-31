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

from dotenv import load_dotenv

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

import litellm
litellm._turn_on_debug()

load_dotenv()


def build_agent(model_name: str) -> LlmAgent:
    """
    Ollama 모델과 Google Search 툴을 지원하는 LlmAgent 인스턴스를 생성하고 설정합니다.

    이 함수는 전달받은 model_name에 따라 적절한 Ollama 모델을 선택하고,
    에이전트의 instruction 템플릿을 정의한 뒤, 이름, 모델, 설명, instruction, 툴을 포함해 LlmAgent를 초기화합니다.
    에이전트는 사용자 질문에 답변하며, 필요 시 툴을 활용해 최신 정보를 제공하고, 명확하고 구조화된 답변을 생성합니다.

    인자:
        model_name (str): 사용할 Ollama 모델 이름 ("llama" 또는 "gemma")

    반환값:
        LlmAgent: 사용자 질의 처리가 가능한 설정된 LlmAgent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변하는 AI 에이전트입니다.
        답변을 제공할 때는 아래와 같은 구조로 간결하고 명확하게 작성해 주세요:
            - 질문 내용:
            - 질문 의도:
            - 답변 내용:
        일상적인 대화성 질문에는 별도의 형식 없이 자연스럽게 답변하세요.
        참고: 답변 시 반드시 사용자가 질문할 때 사용한 언어로 답변해야 합니다.
        """

    if model_name == "llama":
        MODEL ="ollama_chat/llama3.2"
    elif model_name == "gemma":
        MODEL="ollama/gemma3"
    else:
        MODEL="ollama_chat/llama3.2"    

    ollama_agent = LlmAgent(
        model=LiteLlm(model=MODEL),
        name="agent",
        description=(
            "사용자 질문에 답변하는 에이전트입니다."
        ),
        instruction = INSTRUCTION,

    )

    return ollama_agent


root_agent = build_agent("gemma") # gemma 또는 llama
