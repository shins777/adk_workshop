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
from google.adk.agents import SequentialAgent

from .sub_agent import positive_critic, negative_critic, review_critic

load_dotenv()

def build_agent():
    """
    Creates and configures a SequentialAgent for a multi-step workflow.

    This function initializes a SequentialAgent named 'pipeline_agent' that executes
    a sequence of sub-agents: positive_critic, negative_critic, and review_critic.
    The agent is designed to process user queries by running each sub-agent in order,
    enabling a structured workflow for critique and review.

    Returns:
        SequentialAgent: A configured agent ready to process user queries through a sequential workflow.
    """

    pipeline_agent = SequentialAgent(
        name="pipeline_agent",
        sub_agents=[positive_critic, negative_critic, review_critic],
        description="Executes a sequence of positive_critic, negative_critic, and review_critic.",
    )
    return pipeline_agent

root_agent = build_agent()
