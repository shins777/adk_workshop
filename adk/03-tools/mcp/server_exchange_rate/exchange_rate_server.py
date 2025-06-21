import asyncio
import json
from dotenv import load_dotenv

# MCP Server Imports
from mcp import types as mcp_types # Use alias to avoid conflict with genai.types
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio

# ADK Tool Imports
from google.adk.tools.function_tool import FunctionTool
# ADK <-> MCP Conversion Utility
from google.adk.tools.mcp_tool.conversion_utils import adk_to_mcp_tool_type

# --- Load Environment Variables (If ADK tools need them) ---
load_dotenv()

mcp_svr_app = None
exchange_rate_tool = None 

#-----------------------[get_exchange_rate]-----------------------

def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "KRW",
    currency_date: str = "latest", )->dict:
    """Retrieves the exchange rate between two currencies on a specified date.

    Uses the Frankfurter API (https://api.frankfurter.app/) to obtain
    exchange rate data.

    Args:
        currency_from: The base currency (3-letter currency code).
            Defaults to "USD" (US Dollar).
        currency_to: The target currency (3-letter currency code).
            Defaults to "KRW" (KRW).
        currency_date: The date for which to retrieve the exchange rate.
            Defaults to "latest" for the most recent exchange rate data.
            Can be specified in YYYY-MM-DD format for historical rates.

    Returns:
        dict: A dictionary containing the exchange rate information.
            Example: {"amount": 1.0, "base": "USD", "date": "2023-11-24",
                "rates": {"EUR": 0.95534}}
    """
    import requests
    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()

#-----------------------[mcp_server_init]-----------------------

def mcp_server_init():
    """
    Initializes the MCP server and the ADK exchange rate tool.

    This function creates an ADK FunctionTool for retrieving exchange rates and prints
    initialization messages. It then creates and returns an MCP Server instance for
    exposing the tool via the Model Context Protocol (MCP).

    Returns:
        tuple: A tuple containing the MCP Server instance and the initialized exchange rate tool.
    """

    exchange_rate_tool = FunctionTool(func=get_exchange_rate)

    print("Initializing ADK exchange rate tool...")
    print(f"ADK tool '{exchange_rate_tool.name}' initialized.")

    # --- MCP Server Setup ---
    print("Creating MCP Server instance...")
    mcp_svr_app = Server("adk-exchange-rate-mcp-server") 
    print("MCP Server instance created.")

    return mcp_svr_app, exchange_rate_tool

mcp_svr_app, exchange_rate_tool = mcp_server_init()

#-----------------------[list_tools]-----------------------

@mcp_svr_app.list_tools()
async def list_tools() -> list[mcp_types.Tool]:
    """
    MCP handler to list available tools.

    This function is called by the MCP server to provide a list of available tools.
    It converts the ADK tool's definition to the MCP tool schema format and returns it
    as a list. This allows clients to discover which tools are exposed by the server.

    Returns:
        list[mcp_types.Tool]: A list containing the MCP tool schema for the available tools.
    """

    print("MCP Server: Received list_tools request.")
    # Convert the ADK tool's definition to MCP format
    mcp_tool_schema = adk_to_mcp_tool_type(exchange_rate_tool)
    print(f"MCP Server: Advertising tool: {mcp_tool_schema.name}")
    return [mcp_tool_schema]

#-----------------------[call_tool]-----------------------
@mcp_svr_app.call_tool()
async def call_tool(
    name: str, arguments: dict
) -> list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource]:
  
    """
    MCP handler to execute a tool call.

    This function is called by the MCP server when a client requests execution of a tool.
    It checks if the requested tool name matches the available ADK tool, executes the tool asynchronously,
    and returns the result formatted as MCP content. If the tool is not found or an error occurs,
    it returns an error message in MCP format.

    Args:
        name (str): The name of the tool to execute.
        arguments (dict): The arguments to pass to the tool.

    Returns:
        list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource]:
            A list containing the tool's response formatted as MCP content.
    """

    print(f"MCP Server: Received call_tool request for '{name}' with args: {arguments}")

    # Check if the requested tool name matches our wrapped ADK tool
    if name == exchange_rate_tool.name:
        try:
            # Execute the ADK tool's run_async method
            # Note: tool_context is None as we are not within a full ADK Runner invocation
            adk_response = await exchange_rate_tool.run_async(
                args=arguments,
                tool_context=None, # No ADK context available here
            )
            print(f"MCP Server: ADK tool '{name}' executed successfully.")
            # Format the ADK tool's response (often a dict) into MCP format.
            # Here, we serialize the response dictionary as a JSON string within TextContent.
            # Adjust formatting based on the specific ADK tool's output and client needs.
            response_text = json.dumps(adk_response, indent=2)
            return [mcp_types.TextContent(type="text", text=response_text)]

        except Exception as e:
            print(f"MCP Server: Error executing ADK tool '{name}': {e}")
            # Return an error message in MCP format
            # Creating a proper MCP error response might be more robust
            error_text = json.dumps({"error": f"Failed to execute tool '{name}': {str(e)}"})
            return [mcp_types.TextContent(type="text", text=error_text)]
    else:
        # Handle calls to unknown tools
        print(f"MCP Server: Tool '{name}' not found.")
        error_text = json.dumps({"error": f"Tool '{name}' not implemented."})
        # Returning error as TextContent for simplicity
        return [mcp_types.TextContent(type="text", text=error_text)]

#-----------------------[run_server]-----------------------
async def run_server():
    """
    Runs the MCP server over standard input/output.

    This function starts the MCP server using the stdio_server context manager,
    performs the handshake, and enters the main event loop to handle incoming
    requests and tool invocations. It is intended to be the main entry point
    for launching the MCP server process.

    Returns:
        None
    """
  
    # Use the stdio_server context manager from the MCP library
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        print("MCP Server starting handshake...")
        await mcp_svr_app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=mcp_svr_app.name, # Use the server name defined above
                server_version="0.1.0",
                capabilities=mcp_svr_app.get_capabilities(
                    # Define server capabilities - consult MCP docs for options
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
        print("MCP Server run loop finished.")


if __name__ == "__main__":
    print("Launching MCP Server exposing ADK tools...")
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("\nMCP Server stopped by user.")
    except Exception as e:
        print(f"MCP Server encountered an error: {e}")
    finally:
        print("MCP Server process exiting.")
