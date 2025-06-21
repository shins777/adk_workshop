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

from .critic import CriticAgent

load_dotenv()

def build_agent() -> Agent:
    """Initializes and returns a CriticAgent.

    The CriticAgent is configured with a positive critic sub-agent
    (positive_critic_agent) and a negative critic sub-agent
    (negative_critic_agent), which are imported from the .sub_agent module.

    Returns:
        Agent: An instance of the CriticAgent.
    """

    agent = CriticAgent(
        name = "critic_agent",
        positive_critic_agent = positive_critic_agent,
        negative_critic_agent = negative_critic_agent,
    )
    return agent

root_agent = build_agent()