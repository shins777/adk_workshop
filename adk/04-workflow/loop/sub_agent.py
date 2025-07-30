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
from google.adk.tools import ToolContext
from google.adk.tools import google_search

load_dotenv()

COMPLETION_PHRASE = "전체적으로 답변이 괜찮습니다."

#--------------------------------[exit_loop]----------------------------------

def exit_loop(tool_context: ToolContext):
    """
    루프 에이전트에게 현재 루프 반복을 종료하도록 신호를 보냅니다.

    이 함수는 루프 내 에이전트가 툴로서 호출되도록 의도되었습니다.
    툴 컨텍스트의 'escalate' 액션을 True로 설정하여,
    루프 에이전트가 루프를 벗어나 워크플로우의 다음 단계로 진행하도록 지시합니다.

    인자:
        tool_context (ToolContext): 에이전트 및 액션 정보를 담은 컨텍스트 객체

    반환값:
        dict: 추가 출력이 필요 없으므로 빈 딕셔너리 반환
    """
  
    print(f"[Tool Call] exit_loop triggered by {tool_context.agent_name}")
    
    # 루프 에이전트에게 현재 루프 반복을 종료하도록 신호를 보냅니다.
    # 툴 컨텍스트의 'escalate' 액션을 True로 설정하여,
    # 루프 에이전트가 루프를 벗어나 워크플로우의 다음 단계로 진행하도록 지시합니다.
    tool_context.actions.escalate = True

    return {}

#--------------------------------[research_agent]----------------------------------

research_agent = Agent(
    name = "research_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "주어진 주제에 대해 긍정적이고 부정적인 측면을 작성하는 에이전트입니다.",
    instruction = """
            당신은 주어진 주제에 대해 긍정적인 면과 부정적인 측면을 작성하는 에이전트입니다.
            답변을 제공할 때는 가능한 간결하고 명확하게 작성해야 하며, "### 리서치 결과 : " 라고 시작해야 합니다.
            참고: 답변 시 반드시 사용자가 질문한 언어와 동일한 언어로 답변해야 합니다.

            """,
    tools=[google_search],

    output_key="research_outcome",                
)    

#--------------------------------[critic_agent]----------------------------------

critic_agent = Agent(
    name = "critic_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "주어진 주제에 대한 답변을 검토하는 건설적인 비평 AI 에이전트입니다.",
    instruction = f"""
                    당신은 주어진 주제에 대한 답변을 검토하는 건설적인 비평 AI 에이전트입니다.
                    답변에 "### 답변 검토"라는 제목을 추가하세요.

                    **주어진 주제에 대한 답변:**
                        ```
                        {{research_outcome}}
                        ```

                    **작업:**
                        다음 기준에 따라 응답을 명확하게 검토하세요:

                        응답을 개선할 수 있는 1-2가지 *명확하고 실행 가능한* 방법을 제시하세요.
                        우리 사회와 조직에 대한 시사점을 포함해야 합니다.
                        구체적인 제안을 간결하게 제시하세요. 예를 들어: 비평 텍스트*만* 출력하세요. 문서

                    ** 답변이 괜찮다면:
                    *정확히* "{COMPLETION_PHRASE}" 문구로 응답해야 하며, 다른 문구를 출력하거나 설명을 추가하지 마세요.

                    참고: 답변 시 반드시 사용자가 질문한 언어와 동일한 언어로 답변해야 합니다.

                """,
    output_key="criticism",                
)   

#--------------------------------[refine_agent]----------------------------------

refine_agent = Agent(
    name = "refine_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자의 질문에 대한 답변을 검토하는 건설적인 비평 AI 에이전트입니다.",
    instruction = f"""
                    당신은 사용자의 질문에 대한 답변을 검토하는 건설적인 비평 AI 에이전트입니다.
                    응답에 "## 답변 검증"이라는 제목을 추가하세요.

                    **주어진 주제에 대한 답변:**
                        ```
                        {{research_outcome}}
                        ```
                    **비평/제안:**
                        ```
                        {{criticism}}
                        ```
                    **작업:**
                        '비평/제안'을 분석하세요.

                        비평이 *정확히* "{COMPLETION_PHRASE}"인 경우:
                            'exit_loop' 함수를 호출해야 합니다. 텍스트를 출력하지 마세요.
                        그렇지 않은 경우 (비평에 실행 가능한 피드백이 포함된 경우):
                            제안을 신중하게 적용하여 '현재 문서'를 개선하세요. 개선된 문서 텍스트*만* 출력하세요.
                            설명을 추가하지 마세요. 개선된 문서를 출력하거나 exit_loop 함수를 호출하세요.

                    참고: 답변 시 반드시 사용자가 질문한 언어와 동일한 언어로 답변해야 합니다.

                """,
    
    tools=[exit_loop],

)   

#--------------------------------[conclusion_agent]----------------------------------

conclusion_agent = Agent(
    name = "conclusion_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 질문의 긍정적 및 부정적 측면을 요약하는 에이전트",
    instruction = f"""
                    당신은 주어진 주제에 대한 긍정적 및 부정적 비평을 바탕으로 최종 요약 및 결론을 설명하는 에이전트입니다.
                    답변 시 아래 현재 문서와 비평/제안 섹션을 참고하여 "### 최종 요약"이라고 말하고 답변하세요.
                    
                    **주어진 주제에 대한 답변:**
                    ```
                    {{research_outcome}}
                    ```
                    **비평/제안:**
                    ```
                    {{criticism}}
                    ```
                    참고: 답변 시 반드시 사용자가 질문한 언어와 동일한 언어로 답변해야 합니다.

                """,
)