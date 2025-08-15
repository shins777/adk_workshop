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
from google.adk.code_executors import BuiltInCodeExecutor

load_dotenv()

INSTRUCTION = """
        You are an agent that executes program code to perform calculations and return results.
        When a user enters a mathematical expression, Python code is written to compute the expression and executed through the built-in code executor.
        """

root_agent = Agent(
    name = "code_execution_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "An agent that executes program code to perform calculations and return results.",
    instruction = INSTRUCTION,
    code_executor=BuiltInCodeExecutor(),   
)   
