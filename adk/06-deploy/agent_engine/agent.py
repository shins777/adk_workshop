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
from google.adk.agents import SequentialAgent
from google.adk.agents import Agent

load_dotenv()

#--------------------------------[positive_critic]----------------------------------
positive_critic = Agent(
    name = "positive_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자의 질문에 긍정적으로 답변하는 에이전트.",
    instruction = """
                    당신은 주어진 주제에 대해 긍정적인 리뷰를 작성하는 에이전트입니다.
                    사용자가 주제를 입력하면, 해당 주제의 긍정적인 측면을 찾아 긍정적인 리뷰를 작성해야 합니다. 답변을 제공할 때는 최대한 간결하고 명확하게 작성하며, 반드시 '긍정적 리뷰:'라는 말로 시작하세요.
                  
                  """,
)    

#--------------------------------[negative_critic]----------------------------------
negative_critic = Agent(
    name = "negative_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 질문에 부정적인 측면으로 답변하는 에이전트.",
    instruction = """
                    당신은 주어진 주제에 대해 부정적인 리뷰를 작성하는 에이전트입니다.
                    사용자가 주제를 입력하면, 해당 주제의 부정적인 측면을 찾아 부정적인 리뷰를 작성해야 합니다. 답변을 제공할 때는 최대한 간결하고 명확하게 작성하며, 반드시 '부정적 리뷰:'라는 말로 시작하세요.
                  
                  """,
)    

#--------------------------------[review_critic]----------------------------------
review_critic = Agent(
    name = "review_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 질문에 대한 긍정적/부정적 측면을 요약하는 에이전트.",
    instruction = """
                    당신은 주어진 주제에 대한 긍정적, 부정적 비평을 바탕으로 최종 요약과 결론을 설명하는 에이전트입니다. 답변 시 반드시 '최종 요약:'이라는 말로 시작하여 답변하세요.
                """,
)

#--------------------------------[build_agent]----------------------------------
def build_agent() -> Agent:
    """
    여러 서브 에이전트로 구성된 SequentialAgent를 생성하고 설정합니다.

    이 함수는 'pipeline_agent'라는 SequentialAgent를 초기화하며,
    positive_critic, negative_critic, review_critic 서브 에이전트들을 순차적으로 실행합니다.
    각 서브 에이전트는 전체 작업의 특정 부분을 담당하며,
    SequentialAgent가 이들의 실행을 순서대로 조율합니다.

    반환값:
        Agent: 사용자 질의를 처리할 준비가 된 SequentialAgent 인스턴스
    """

    # 순차 에이전트는 각 하위 에이전트가 자체 지침을 가지고 있기 때문에 지침이 필요하지 않습니다.
    agent = SequentialAgent(
        name="pipeline_agent",
        sub_agents=[positive_critic, negative_critic, review_critic],
        description="Executes a sequence of positive_critic, negative_critic, and review_critic.",
    )

    return agent

root_agent = build_agent()
