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

import contextlib
import logging
import asyncio
from collections.abc import AsyncIterator
from typing import Any

import requests
import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.types import Receive, Scope, Send

logger = logging.getLogger(__name__)

#-----------------------[get_exchange_rate]-----------------------
def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "KRW",
    currency_date: str = "latest", )->dict:
    """
    Retrieves the exchange rate between two currencies for a specified date.

    Uses the Frankfurter API (https://api.frankfurter.app/) to fetch exchange rate data.

    Args:
        currency_from: Base currency (3-letter currency code). Default is "USD" (US Dollar).
        currency_to: Target currency (3-letter currency code). Default is "KRW" (Korean Won).
        currency_date: Date for which to query the exchange rate. Default is "latest" for the most recent rate.
            For historical rates, specify in YYYY-MM-DD format.

    Returns:
        dict: Dictionary containing exchange rate information.
            Example: {"amount": 1.0, "base": "USD", "date": "2023-11-24", "rates": {"EUR": 0.95534}}
    """
    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()

#-----------------------[create_mcp_server]-----------------------
def create_mcp_server():
    """
    Create and configure an MCP Server instance exposing tools over the Model Context Protocol (MCP).

    This function builds and returns a `Server` named "adk-mcp-streamable-server" and registers the following handlers:

    - call_tool: asynchronous handler invoked when a client requests tool execution. The example implementation
      supports a `get_exchange_rate` tool which performs a blocking HTTP request to an external API using
      `asyncio.to_thread()` to avoid blocking the event loop, and returns the result wrapped as MCP TextContent.
    - list_tools: returns the list of available tools and their input schemas (the example advertises `get_exchange_rate`).

    The returned `Server` is intended to be used with a StreamableHTTPSessionManager (or other MCP transports)
    to accept client connections over Streamable HTTP.

    Returns:
        Server: A configured MCP Server instance.
    """

    app = Server("adk-mcp-streamable-server")


    @app.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any]) -> list[types.ContentBlock]:
        """
        Handle tool execution requests from MCP clients.

        This asynchronous handler is invoked when an MCP client requests execution of a named tool.
        The function should inspect the `name` parameter, execute the corresponding tool logic,
        and return a list of MCP ContentBlock objects (e.g., TextContent, ImageContent).

        Supported tools in this example:
        - "get_exchange_rate": expects the arguments `currency_from`, `currency_to`, and `currency_date`.
          The handler will perform a blocking HTTP request to the Frankfurter API to retrieve exchange rates
          and uses `asyncio.to_thread()` to run the blocking call off the event loop.

        Parameters:
            name (str): Tool identifier requested by the client.
            arguments (dict[str, Any]): Arguments supplied by the client for tool execution.

        Returns:
            list[types.ContentBlock]: A list containing the tool output formatted as MCP content blocks.

        On errors, the handler returns a TextContent block describing the failure rather than raising,
        so that MCP clients receive a machine-readable error message.
        """

        print(f"### Tool called: {name} with arguments: {arguments}")

        if name == "get_exchange_rate":
            
            print(f"### Tool {name} is chosen with arguments: {arguments}")

            currency_from = arguments.get("currency_from", "USD")
            currency_to = arguments.get("currency_to", "KRW")
            currency_date = arguments.get("currency_date", "latest")

            # Execute the blocking HTTP call in a thread to avoid blocking the async event loop
            try:
                result = await asyncio.to_thread(get_exchange_rate, currency_from, currency_to, currency_date)
                print("### Tool %s execution results: %s", name, result)
                return [
                    types.TextContent(
                        type="text",
                        text=f"The exchange rate is : {result}"
                    )
                ]
            except Exception as e:
                print("### Error while executing tool %s: %s", name, e)
                # Return an error message back to the client in MCP TextContent format
                return [
                    types.TextContent(
                        type="text",
                        text=f"Error executing tool '{name}': {str(e)}"
                    )
                ]
        else:
            raise ValueError(f"Unknown tool: {name}")

    @app.list_tools()
    async def list_tools() -> list[types.Tool]:
        """
        Return the list of tools exposed by this MCP server.

        MCP clients call this handler to discover which tools are available on the server and
        to obtain each tool's description and input schema. The returned list should contain
        `mcp.types.Tool` objects describing the tool name, description, and JSON Schema for inputs.

        In this example the server advertises a single tool:
        - "get_exchange_rate": requires `currency_from`, `currency_to`, and `currency_date` input fields.

        Returns:
            list[types.Tool]: A list of tool descriptors that MCP clients can use for discovery and validation.
        """

        return [
            types.Tool(
                name="get_exchange_rate",
                description="Retrieves the exchange rate between two currencies for a specified date.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "currency_from": {
                            "type": "string",
                            "description": "Base currency (3-letter currency code). Default is 'USD' (US Dollar)"
                        },
                        "currency_to": {
                            "type": "string",
                            "description": "Target currency (3-letter currency code). Default is 'KRW' (Korean Won"
                        },                        
                        "currency_date": {
                            "type": "string",
                            "description": "Date for which to query the exchange rate. Default is 'latest' for the most recent rate. For historical rates, specify in YYYY-MM-DD format."
                        },                        
                    },
                    "required": ["currency_from", "currency_to", "currency_date"],
                }
            )
        ]

    return app

#-----------------------[main]-----------------------

def main(json_response: bool = False):
    """
    Run the MCP Streamable HTTP server.

    This function configures logging, creates the MCP `Server` (via
    `create_mcp_server()`), and wraps it with a `StreamableHTTPSessionManager`.
    It defines an ASGI handler for Streamable HTTP requests, a lifespan
    context manager to manage the session manager lifecycle, mounts the
    handler at the `/mcp` path on a Starlette application, and launches the
    application using `uvicorn` on `0.0.0.0:8080`.

    Parameters:
        json_response (bool): When True, the StreamableHTTPSessionManager will
            return responses formatted as JSON. This can be useful for testing
            or debugging. Defaults to False.

    Notes:
        - The server is configured in stateless mode for better scalability on
          serverless platforms (e.g., Cloud Run).
        - Required dependencies include: `mcp`, `starlette`, `uvicorn`, and
          `requests` (for the example tool implementation).
        - Intended to be used as the module entry point (`if __name__ == "__main__"`).

    Returns:
        None
    """

    logging.basicConfig(level=logging.INFO)

    app = create_mcp_server()

    # Create session manager with stateless mode for scalability
    session_manager = StreamableHTTPSessionManager(
        app=app,
        event_store=None,
        json_response=json_response,
        stateless=True,  # Important for Cloud Run scalability
    )

    async def handle_streamable_http(scope: Scope, receive: Receive, send: Send) -> None:
        await session_manager.handle_request(scope, receive, send)

    @contextlib.asynccontextmanager
    async def lifespan(app: Starlette) -> AsyncIterator[None]:
        """Manage session manager lifecycle."""
        async with session_manager.run():
            logger.info("MCP Streamable HTTP server started!")
            try:
                yield
            finally:
                logger.info("MCP server shutting down...")

    # Create ASGI application
    starlette_app = Starlette(
        debug=False,  # Set to False for production
        routes=[
            Mount("/mcp", app=handle_streamable_http),
        ],
        lifespan=lifespan,
    )

    import uvicorn
    uvicorn.run(starlette_app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()