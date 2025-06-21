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
from google.adk.code_executors import BuiltInCodeExecutor

load_dotenv()

def build_agent() -> Agent:

    """
    Creates and configures an Agent instance with built-in code execution tool support.

    This function loads environment variables, defines the agent's instruction template,
    and initializes the Agent with a name, model, description, instruction, and the built-in
    code execution tool. The agent is designed to solve mathematical expressions by writing
    and executing Python code, returning both the code and the result as plain text.

    Returns:
        Agent: A configured Agent instance ready to process code execution queries.
    """

    INSTRUCTION = """
        You are a calculator agent.
        Given a mathematical expression, you write and execute Python code to calculate the result.
        The response is returned as plain text, both the Python code and the final numerical result of the execution.

        Note : When answering, Must be sure to use the same language the user used when asking the question. 

        """

    code_execution_agent = Agent(
        name = "code_execution_agent",
        model = os.getenv("MODEL"),
        description = "Performs calculations by running Python code.",
        instruction = INSTRUCTION,
        tools=[BuiltInCodeExecutor],
    )

    return code_execution_agent

root_agent = build_agent()