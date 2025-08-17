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
from toolbox_core import ToolboxSyncClient

load_dotenv()

def get_toolbox():
    """
    Creates and configures a ToolboxSyncClient instance.
    This function loads environment variables and initializes the ToolboxSyncClient.
    The client is used to manage synchronization with the toolbox.

    Returns:
        ToolboxSyncClient: A client instance ready to manage synchronization with the toolbox.
    """
    toolbox = ToolboxSyncClient(    
        os.getenv("TOOLBOX_SYNC_CLIENT"),
    )

    tool_set = toolbox.load_toolset('my_bq_toolset')
    print(f"Toolbox set: {tool_set}")
    
    tools = toolbox.load_tool('query_bbc'),
    print(f"Toolbox tools: {tools}")
    
    return tools

tools = get_toolbox()

INSTRUCTION = """
    You are an agent that provides answers to user questions.
    When a user asks a question, you must use the relevant tool to generate an answer.

"""

root_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Agent that answers user queries",
    instruction = INSTRUCTION,
    tools=tools,
)
