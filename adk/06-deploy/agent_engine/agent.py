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
from google.adk.agents import SequentialAgent
from google.adk.agents import Agent

from .sub_agent import positive_critic, negative_critic, review_critic

load_dotenv()

#--------------------------------[build_agent]----------------------------------

def build_agent() -> Agent:
    """
    Creates and configures a SequentialAgent composed of multiple sub-agents.

    This function initializes a SequentialAgent named 'pipeline_agent' that executes
    a sequence of sub-agents: positive_critic, negative_critic, and review_critic.
    Each sub-agent is responsible for a specific part of the overall task, and the
    SequentialAgent coordinates their execution in order.

    Returns:
        Agent: A configured SequentialAgent instance ready to process user queries.
    """

    # SequentialAgent does not requrire instruction because each sub agent has their own instruction. 
    agent = SequentialAgent(
        name="pipeline_agent",
        sub_agents=[positive_critic, negative_critic, review_critic],
        description="Executes a sequence of positive_critic, negative_critic, and review_critic.",
    )

    return agent

root_agent = build_agent()
