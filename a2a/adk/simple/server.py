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
    ADK 에이전트 실행기와 함께 A2A 서버를 시작합니다.

    이 함수는 에이전트의 스킬 및 카드를 설정하고, ADK 에이전트와 러너를 초기화하며,
    요청 핸들러와 태스크 스토어를 구성한 뒤, Uvicorn을 통해 A2AStarletteApplication을 실행합니다.
    서버는 외부 요청을 수신하여 ADKAgentExecutor를 통해 A2A 프로토콜 기반 에이전트 상호작용을 지원합니다.

    반환값:
        None
    """

    skill = AgentSkill(
        id='echo_agent',
        name='대답 텍스트를 대문자로 변환',
        description='에코 에이전트',
        tags=['echo', 'upper case'],
        examples=['Hi', 'change the text to upper case'],
        inputModes=['text/plain'],
        outputModes=['text/plain'],
    )

    agent_card = AgentCard(
        name='Echoing Agent',
        description='대답을 대문자로 반환하는 에코 에이전트.',
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