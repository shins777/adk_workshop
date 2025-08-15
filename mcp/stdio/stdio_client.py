import os
import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from google import genai
from google.genai import types
from google.genai.types import HttpOptions

# from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env

class MCPClient:

    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()

        self.client = genai.Client(
            vertexai=os.getenv("GOOGLE_GENAI_VERTEXAI"),
            project=os.getenv("GOOGLE_GENAI_PROJECT"),
            location=os.getenv("GOOGLE_CLOUD_LOCATION"),)

    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server

        Args:
            server_script_path: Path to the server script (.py or .js)
        """

        server_params = StdioServerParameters(
            command="python",
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])


    async def process_query(self, query: str) -> str:
        """Process a query using Claude and available tools"""

        mcp_tools = await self.session.list_tools()

        tools = [
            types.Tool(
                function_declarations=[
                    {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": {
                            k: v
                            for k, v in tool.inputSchema.items()
                            if k not in ["additionalProperties", "$schema"]
                        },
                    }
                ]
            )
            for tool in mcp_tools.tools
        ]

        print(f"\nAvailable tools: {tools}")

        generate_content_config = types.GenerateContentConfig(
            system_instruction ="You are a helpful assistant.",
            temperature=0,
            thinking_config= types.ThinkingConfig(thinking_budget=0,),
            tools = tools,
        )

        response = self.client.models.generate_content(
            model=os.getenv("GOOGLE_GENAI_MODEL"),
            contents=[
                types.Content(
                    role="user",
                    parts=[
                    types.Part.from_text(text=query)
                    ]
                )
            ],
            config = generate_content_config,
            
        )
        return response.text

    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            query = input("\nQuery: ").strip()

            if query.lower() == 'quit':
                break

            response = await self.process_query(query)
            print(f"\nResponse:\n {response}")

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()


async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_server_script>")
        sys.exit(1)

    client = MCPClient()

    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())    