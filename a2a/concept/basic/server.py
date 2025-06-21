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

import uvicorn

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)

from .executor import EchoAgentExecutor

def run_a2a_server():
    """
    Starts the A2A server with an EchoAgentExecutor.

    This function sets up the agent's skill and card, initializes the request handler and task store,
    and launches the A2AStarletteApplication using Uvicorn. The server listens for incoming requests
    and processes them using the EchoAgentExecutor, which responds to user input by echoing it in uppercase.

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

    request_handler = DefaultRequestHandler(
        agent_executor=EchoAgentExecutor(),
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        agent_card=agent_card,
        http_handler=request_handler,
    )

    uvicorn.run(server.build(), host='0.0.0.0', port=7777,)

if __name__ == '__main__':

    run_a2a_server()