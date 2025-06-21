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
    Entry point for the A2A client example.

    This function initializes an HTTP client, resolves the public agent card from a remote agent,
    and creates an A2AClient instance. It then enters a loop to accept user input, sends messages
    to the agent (both non-streaming and streaming), and prints the agent's responses to the console.

    Returns:
        None
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
            print(f'Attempting to fetch public agent card from: {base_url}{AGENT_CARD_PATH}')

            public_agent_card = await resolver.get_agent_card()

            print('Successfully fetched public agent card:')
            print(public_agent_card.model_dump_json(indent=2, exclude_none=True))

        except Exception as e:
            print(f'Critical error fetching agent card: {e}')

        client = A2AClient(httpx_client=httpx_client, agent_card=public_agent_card)
        print('A2AClient initialized.')

        while True:

            user_input = input("\n 👤 User: ")
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
            print(f"\n 🤖 [No Streaming] AI Assistant: {response.model_dump(mode='json', exclude_none=True)}")

            #----------------------[Streaming]----------------------
            streaming_request = SendStreamingMessageRequest(
                id=str(uuid4()), params=MessageSendParams(**send_message_payload)
            )
            stream_response = client.send_message_streaming(streaming_request)
            async for chunk in stream_response:
                print(f"\n 🤖 [Streaming] AI Assistant: {chunk.model_dump(mode='json', exclude_none=True)}")

if __name__ == '__main__':
    import asyncio

    asyncio.run(main())