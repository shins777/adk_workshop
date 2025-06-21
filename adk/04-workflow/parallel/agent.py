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
from google.adk.agents import ParallelAgent

from .sub_agent import positive_critic, negative_critic, review_critic

load_dotenv()

def build_agent():
    """
    Creates and configures a workflow Agent using ParallelAgent and SequentialAgent.

    This function defines a parallel agent for running positive and negative critics in parallel,
    and a sequential agent that first executes the parallel research agent and then the review critic.
    The resulting agent executes a workflow where multiple research agents run in parallel, followed by a review step.

    Returns:
        SequentialAgent: A configured agent ready to process user queries through a parallel and sequential workflow.
    """

    parallel_research_agent = ParallelAgent(
        name="parallel_research_agent",
        sub_agents=[positive_critic, negative_critic],
        description="Runs multiple research agents in parallel to gather information."
    )

    pipeline_agent = SequentialAgent(
        name="pipeline_agent",
        sub_agents=[parallel_research_agent, review_critic],
        description="Executes a sequence of parallel_research_agent, and review_critic.",
    )
    return pipeline_agent

root_agent = build_agent()
