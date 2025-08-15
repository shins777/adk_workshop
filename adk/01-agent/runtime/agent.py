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
from .sub_agent import positive_critic, negative_critic

load_dotenv()

INSTRUCTION = """
You are an helpful agent that answers users' questions.
You must provide answers using sub-agents, as follows:

1. If the user requests a positive review, use the positive_critic agent.
2. If the user requests a negative review, use the negative_critic agent.

"""

root_agent = Agent(
    name = "root_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agents that answer user questions",
    instruction = INSTRUCTION,
    sub_agents = [positive_critic, negative_critic],
)
