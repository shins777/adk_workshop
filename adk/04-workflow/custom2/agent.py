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

from .sub_agent import positive_critic_agent
from .sub_agent import negative_critic_agent

from .critic import CriticAgent

load_dotenv()

def build_agent() -> Agent:
    """
    CriticAgent를 초기화하여 반환합니다.

    CriticAgent는 .sub_agent 모듈에서 import한 긍정 비평 서브 에이전트(positive_critic_agent)와
    부정 비평 서브 에이전트(negative_critic_agent)를 함께 구성하여 동작합니다.

    반환값:
        Agent: CriticAgent 인스턴스
    """

    agent = CriticAgent(
        name = "critic_agent",  # 전체 비평 워크플로우를 담당하는 에이전트 이름
        positive_critic_agent = positive_critic_agent,  # 긍정 비평 서브 에이전트
        negative_critic_agent = negative_critic_agent,  # 부정 비평 서브 에이전트
    )
    return agent

root_agent = build_agent()