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

from .sub_agent import positive_critic_agent
from .sub_agent import negative_critic_agent
from .sub_agent import review_critic_agent

from .critic import CriticAgent

load_dotenv()

def build_agent() -> Agent:
    """
    긍정, 부정, 종합 비평 서브 에이전트가 포함된 CriticAgent 인스턴스를 생성하고 구성합니다.

    이 함수는 긍정 비평, 부정 비평, 종합 리뷰를 위한 서브 에이전트들을 지정하여 CriticAgent를 초기화합니다.
    결과적으로 생성된 에이전트는 각 서브 에이전트에 작업을 위임하여 다단계 비평 워크플로우를 오케스트레이션할 수 있습니다.

    반환값:
        CriticAgent: 사용자 질의 처리가 가능한 구성된 CriticAgent 인스턴스
    """

    agent = CriticAgent(
        name = "critic_agent",
        positive_critic_agent = positive_critic_agent,
        negative_critic_agent =negative_critic_agent,
        review_critic_agent = review_critic_agent,        
    )
    return agent

root_agent = build_agent()