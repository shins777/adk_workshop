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

# Module purpose:
# This module defines a custom CriticAgent that composes three sub-agents:
# - positive_critic_agent: produces positive feedback and highlights strengths
# - negative_critic_agent: produces constructive negative feedback or weaknesses
# - review_critic_agent: aggregates critiques and produces a final review
#
# The CriticAgent coordinates these sub-agents to produce structured critiques
# and an overall evaluation for a given input or document.

root_agent = CriticAgent(
    name = "critic_agent",
    positive_critic_agent = positive_critic_agent,
    negative_critic_agent = negative_critic_agent,
    review_critic_agent = review_critic_agent,        
)

# The `root_agent` can be used directly by the ADK runtime or wired into
# higher-level workflows where a combined critique and review is required.
