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
    EchoAgentExecutor와 함께 A2A 서버를 시작합니다.

    이 함수는 에이전트의 스킬과 카드를 설정하고, 요청 핸들러와 태스크 저장소를 초기화한 뒤,
    Uvicorn을 사용해 A2AStarletteApplication을 실행합니다. 서버는 들어오는 요청을 수신하며,
    EchoAgentExecutor를 통해 사용자의 입력을 대문자로 변환해 응답합니다.

    반환값:
        없음
    """

    skill = AgentSkill(
        id='echo_agent',
        name='대문자로 변환된 텍스트를 반환하는 에이전트',
        description='입력받은 텍스트를 대문자로 에코하는 에이전트',
        tags=['에코', '대문자'],
        examples=['Hi', 'change the text to upper case'],
        inputModes=['text/plain'],
        outputModes=['text/plain'],
    )

    agent_card = AgentCard(
        name='에코 에이전트',
        description='입력받은 텍스트를 대문자로 응답하는 에이전트입니다.',
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