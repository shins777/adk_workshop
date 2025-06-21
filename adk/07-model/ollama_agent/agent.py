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

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

import litellm
litellm._turn_on_debug()

load_dotenv()


def build_agent(model_name: str) -> LlmAgent:
    """
    Creates and configures an LlmAgent instance with Ollama model and Google Search tool support.

    This function selects the appropriate Ollama model based on the provided model_name,
    defines the agent's instruction template, and initializes the LlmAgent with a name,
    model, description, instruction, and the Google Search tool. The agent is designed
    to answer user questions, optionally using the tool for up-to-date information, and
    to format responses in a clear and structured way.

    Args:
        model_name (str): The name of the Ollama model to use ("llama" or "gemma").

    Returns:
        LlmAgent: A configured LlmAgent instance ready to process user queries.
    """

    INSTRUCTION = """
        You are an AI agent who provides answers to users' questions.
        When providing answers, please respond concisely and clearly in the following structure:
        - Question content:
        - Question intent:
        - Answer content:

        Answer casual conversation questions natually without any special format.
        
        Note : When answering, Must be sure to use the same language the user used when asking the question. 

    """

    if model_name == "llama":
        MODEL ="ollama_chat/llama3.2"
    elif model_name == "gemma":
        MODEL="ollama/gemma3"
    else:
        MODEL="ollama_chat/llama3.2"    

    ollama_agent = LlmAgent(
        model=LiteLlm(model=MODEL),
        name="agent",
        description=(
            "Answer to a user's question"
        ),
        instruction = INSTRUCTION,

    )

    return ollama_agent


root_agent = build_agent("gemma") # gemma or llama 
