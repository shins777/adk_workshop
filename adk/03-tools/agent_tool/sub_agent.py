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

load_dotenv()

#--------------------------------[positive_critic]----------------------------------

positive_critic = Agent(
    name = "positive_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자의 질문에 긍정적으로 답변하는 에이전트.",
    instruction = """
                    당신은 주어진 주제에 대해 긍정적인 리뷰를 작성하는 에이전트입니다.
                    사용자가 주제를 입력하면, 해당 주제의 긍정적인 측면을 찾아 긍정적인 리뷰를 작성해야 합니다. 답변을 제공할 때는 최대한 간결하고 명확하게 작성하며, 반드시 '긍정적 리뷰:'라는 말로 시작하세요.
                    답변 시 반드시 사용자가 질문에 사용한 언어로 답변해야 합니다.
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
                    답변 시 반드시 사용자가 질문에 사용한 언어로 답변해야 합니다.
                  """,
)    

