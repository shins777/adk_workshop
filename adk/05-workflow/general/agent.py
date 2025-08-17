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

from .sub_agent import positive_critic, negative_critic

load_dotenv()

SYSTEM_INSTRUCTION = """
    You are an agent that faithfully answers the user's various questions. 
"""

INSTRUCTION = """
    You are an agent that provides answers to user questions.
    Follow the flow below when composing responses:
        1. When the user submits a question, first summarize the user's intent. Begin the summary with the phrase "Question intent:" followed by the intent.
        2. Depending on the user's request, use the sub-agents as follows to produce the response:
            - If the user requests a positive critique, use the `positive_critic` sub-agent.
            - If the user requests a negative critique, use the `negative_critic` sub-agent.
"""

root_agent = Agent(
    name = "Search_agent",  
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "An agent that responds to user queries.",
    global_instruction = SYSTEM_INSTRUCTION,
    instruction = INSTRUCTION,
    sub_agents = [positive_critic, negative_critic],
)
