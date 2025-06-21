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

load_dotenv()

#--------------------------------[positive_critic]----------------------------------

positive_critic = Agent(
    name = "positive_critic",
    model = os.getenv("MODEL"),
    description = "An agent that answers the user's questions in a positive way.",
    instruction = """
                    You are an agent who writes a positive review on a given topic.
                    When a user inputs a topic, you have to search for positive aspects of that topic and write a positive review. When providing an answer, you should write it as concisely and clearly as possible, and start with the words "positive review."
                    When replying, you must answer based on the language the user used. 

                  """,
)    

#--------------------------------[negative_critic]----------------------------------

negative_critic = Agent(
    name = "negative_critic",
    model = os.getenv("MODEL"),
    description = "Agents that answer questions about users' questions with negative aspects",
    instruction = """
                    You are an agent who writes a negative review on a given topic.
                    When a user inputs a topic, you have to search for negative aspects of that topic and write a negative review. When providing an answer, you should write it as concisely and clearly as possible, and start with the words "negative review."
                    When replying, you must answer based on the language the user used. 

                  """,
)    

