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
from google.adk.agents import LoopAgent

from .sub_agent import research_agent
from .sub_agent import critic_agent
from .sub_agent import refine_agent
from .sub_agent import conclusion_agent

load_dotenv()

def build_agent():
    """
    Creates and configures a workflow Agent using LoopAgent and SequentialAgent.

    This function defines a loop agent for iterative critique and refinement, and a sequential agent
    that orchestrates research, critique/refinement, and conclusion sub-agents. The resulting agent
    executes a workflow where research is followed by a loop of critique/refinement, and finally a conclusion.

    Returns:
        SequentialAgent: A configured agent ready to process user queries through a multi-step workflow.
    """

    critics_loop = LoopAgent(
        name="critics_loop",
        sub_agents=[
            critic_agent,
            refine_agent,
        ],
        max_iterations=3
    )

    confirmation_agent = SequentialAgent(
        name="confirmation_agent",
        sub_agents=[
            research_agent, 
            critics_loop,
            conclusion_agent
        ],
        description="Executes a sequence of research_agent and critics_loop.",
    )
    return confirmation_agent

root_agent = build_agent()
