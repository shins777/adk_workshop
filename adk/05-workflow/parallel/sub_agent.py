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
from google.adk.tools import google_search

load_dotenv()

#--------------------------------[positive_critic]----------------------------------
positive_critic = Agent(
    name = "positive_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "An agent that answers only the positive aspects of a user's questions.",
    instruction = """You are an agent who writes positive reviews on the topic of a user's inquiry. 
                      When providing your response, be as concise and clear as possible in 3 lines.
                      and always begin with the phrase "Positive review results:" """,
    tools=[google_search],
    output_key="positive_critic_output",                      
)    

#--------------------------------[negative_critic]----------------------------------
negative_critic = Agent(
    name = "negative_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "An agent who answers only the negative aspects of user questions.",
    instruction = """You are an agent writing a negative review on the topic of a user's question.
                      When providing your response, be as concise and clear as possible in 3 lines.
                      and always begin with the phrase "Negative review results:" """,
    tools=[google_search],
    output_key="negative_critic_output",                       
)    

#--------------------------------[review_critic]----------------------------------
review_critic = Agent(
    name = "review_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "An agent that reviews the positive and negative aspects of a user's question and summarizes it overall.",
    instruction = f"""
            You are an agent who provides a final summary and conclusion based on positive and negative criticism of a given topic.
            Your response must be based on the following two pieces of information:

            * Positive aspects: ```{{positive_critic_output}}```
            * Negative aspects: ```{{negative_critic_output}}```

            When responding, always state ### Final Summary:.
            When providing your response, be as concise and clear as possible in 3 lines.   
        """,
)  
