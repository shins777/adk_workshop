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

import click
import uvicorn

from dotenv import load_dotenv
from google.adk.artifacts import InMemoryArtifactService
from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from starlette.routing import Route

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)

from . import agent
from .executor import ADKAgentExecutor

def run_a2a_server():
    """
    Starts the A2A server with an ADK agent executor.

    This function sets up the agent's skill and card, initializes the ADK agent and its runner,
    configures the request handler and task store, and launches the A2AStarletteApplication using Uvicorn.
    The server listens for incoming requests and processes them using the ADKAgentExecutor, enabling
    interaction with the agent via the A2A protocol.

    Returns:
        None
    """

    skill = AgentSkill(
        id='echo_agent',
        name='Response text changed with upper case',
        description='echo agent',
        tags=['echo', 'upper case'],
        examples=['Hi', 'change the text to upper case'],
        inputModes=['text/plain'],
        outputModes=['text/plain'],
    )

    agent_card = AgentCard(
        name='Echoing Agent',
        description='Eching agent resonses with upper case.',
        url='http://localhost:7777/',
        version='1.0.0',
        defaultInputModes=['text'],
        defaultOutputModes=['text'],
        capabilities=AgentCapabilities(streaming=True),
        skills=[skill],
        supportsAuthenticatedExtendedCard=True,
    )

    # crate an agent instance.
    adk_agent = agent.build_agent()
    
    runner = Runner(
        app_name=agent_card.name,
        agent=adk_agent,
        artifact_service=InMemoryArtifactService(),
        session_service=InMemorySessionService(),
        memory_service=InMemoryMemoryService(),
    )

    adk_agent_executor = ADKAgentExecutor(runner = runner , agent_card =agent_card )

    request_handler = DefaultRequestHandler(
        agent_executor= adk_agent_executor,
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        agent_card=agent_card,
        http_handler=request_handler,
    )

    uvicorn.run(server.build(), host='0.0.0.0', port=7777,)

if __name__ == '__main__':

    run_a2a_server()