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

"""
This module provides an example workflow composition using agents.
The workflow includes research, critique, refinement, and conclusion steps.
"""

from dotenv import load_dotenv
from google.adk.agents import SequentialAgent
from google.adk.agents import LoopAgent

from .sub_agent import research_agent
from .sub_agent import critic_agent
from .sub_agent import refine_agent
from .sub_agent import conclusion_agent

load_dotenv()

# Loop workflow example: `critics_loop` performs iterative critique and refinement.
# The loop alternates between a critic step and a refine step to improve outputs.
critics_loop = LoopAgent(
    name="critics_loop",
    sub_agents=[
        critic_agent,
        refine_agent,
    ],
    max_iterations=3  # Maximum number of iterations for the critique/refinement loop
)

# Root agent composes the workflow as a sequence of steps:
# 1) research_agent: gathers or generates initial content
# 2) critics_loop: iteratively critiques and refines the content
# 3) conclusion_agent: produces the final output based on refined results
root_agent = SequentialAgent(
    name="confirmation_agent",
    sub_agents=[
        research_agent, 
        critics_loop,
        conclusion_agent
    ],
    description="Agent that runs the research agent, then an iterative critics/refinement loop, and finally a conclusion agent.",
)
