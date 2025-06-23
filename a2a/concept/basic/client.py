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

from typing import Any
from uuid import uuid4
import httpx

from a2a.client import A2ACardResolver, A2AClient
from a2a.types import  (AgentCard,
                        MessageSendParams,
                        SendMessageRequest,
                        SendStreamingMessageRequest,)

async def main() -> None:
    """
    A2A 클라이언트 예제의 진입점입니다.

    이 함수는 HTTP 클라이언트를 초기화하고, 원격 에이전트로부터 공개 에이전트 카드를 조회한 뒤,
    A2AClient 인스턴스를 생성합니다. 이후 사용자 입력을 받아 에이전트에게 메시지를 전송(스트리밍/비스트리밍 모두)
    하고, 에이전트의 응답을 콘솔에 출력하는 루프를 실행합니다.

    반환값:
        없음
    """

    base_url = 'http://localhost:7777'
    AGENT_CARD_PATH = '/.well-known/agent.json'

    async with httpx.AsyncClient() as httpx_client:
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=base_url,
        )
        public_agent_card: AgentCard | None = None

        try:
            print(f'공개 에이전트 카드를 가져오는 중: {base_url}{AGENT_CARD_PATH}')

            public_agent_card = await resolver.get_agent_card()

            print('공개 에이전트 카드 조회 성공:')
            print(public_agent_card.model_dump_json(indent=2, exclude_none=True))

        except Exception as e:
            print(f'에이전트 카드 조회 중 치명적 오류 발생: {e}')

        client = A2AClient(httpx_client=httpx_client, agent_card=public_agent_card)
        print('A2AClient가 초기화되었습니다.')

        while True:

            user_input = input("\n 👤 사용자: ")
            if user_input.lower() == "exit":
                break

            send_message_payload: dict[str, Any] = {
                'message': {
                    'role': 'user',
                    'parts': [
                        {'kind': 'text', 'text': user_input }
                    ],
                    'messageId': uuid4().hex,
                },
            }
            
            request = SendMessageRequest(
                id=str(uuid4()), params=MessageSendParams(**send_message_payload)
            )

            #----------------------[No streaming]----------------------
            response = await client.send_message(request)
            print(f"\n 🤖 [비스트리밍] AI 어시스턴트: {response.model_dump(mode='json', exclude_none=True)}")

            #----------------------[Streaming]----------------------
            streaming_request = SendStreamingMessageRequest(
                id=str(uuid4()), params=MessageSendParams(**send_message_payload)
            )
            stream_response = client.send_message_streaming(streaming_request)
            async for chunk in stream_response:
                print(f"\n 🤖 [스트리밍] AI 어시스턴트: {chunk.model_dump(mode='json', exclude_none=True)}")

if __name__ == '__main__':
    import asyncio

    asyncio.run(main())