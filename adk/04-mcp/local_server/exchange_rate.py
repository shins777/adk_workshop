import asyncio
import json
from dotenv import load_dotenv

from mcp import types as mcp_types 
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio

from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.mcp_tool.conversion_utils import adk_to_mcp_tool_type

load_dotenv()

mcp_svr_app = None
exchange_rate_tool = None 

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
    import requests
    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()

#-----------------------[mcp_server_init]-----------------------

def mcp_server_init():
    """
    Initializes the MCP server and ADK exchange rate tool.
    This function creates the ADK FunctionTool for exchange rate queries and prints initialization messages.
    Then, it creates an MCP server instance and returns it along with the initialized tool for exposure via MCP.

    Returns:
        tuple: A tuple containing the MCP server instance and the initialized exchange rate tool.
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
    MCP handler that returns the list of available tools.

    This function is called when the MCP server needs to provide the list of available tools.
    It converts the ADK tool definition to the MCP tool schema format and returns it as a list.
    This allows clients to see which tools are exposed by the server.

    Returns:
        list[mcp_types.Tool]: List of available MCP tool schemas.
    """

    print("MCP Server: Received list_tools request.")
    # ADK 도구의 정의를 MCP 형식으로 변환
    mcp_tool_schema = adk_to_mcp_tool_type(exchange_rate_tool)
    print(f"MCP Server: Advertising tool: {mcp_tool_schema.name}")
    return [mcp_tool_schema]

#-----------------------[call_tool]-----------------------
@mcp_svr_app.call_tool()
async def call_tool(
    name: str, arguments: dict
) -> list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource]:
    """
    MCP handler for processing tool execution requests.

    This function is called when a client requests to execute a tool.
    If the requested tool name matches the ADK tool, it is executed asynchronously and the result is returned in MCP content format.
    If the tool is not found or an error occurs, an MCP-formatted error message is returned.

    Args:
        name (str): Name of the tool to execute
        arguments (dict): Arguments to pass to the tool
    Returns:
        list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource]:
            List of tool responses formatted as MCP content
    """

    print(f"MCP Server: Received call_tool request for '{name}' with args: {arguments}")

    # Check if the requested tool name matches the wrapped ADK tool
    if name == exchange_rate_tool.name:
        try:
            # Execute the ADK tool's run_async method
            # Note: tool_context is not a full ADK Runner call, so None is used
            adk_response = await exchange_rate_tool.run_async(
                args=arguments,
                tool_context=None, # 여기서는 ADK 컨텍스트 없음
            )
            print(f"MCP Server: ADK tool '{name}' executed successfully.")
            # Convert the ADK tool's response (usually a dict) to MCP format
            # Here, the response dictionary is serialized to a JSON string and wrapped in TextContent
            # Adjust formatting as needed for actual tool output and client requirements
            response_text = json.dumps(adk_response, indent=2)
            return [mcp_types.TextContent(type="text", text=response_text)]

        except Exception as e:
            print(f"MCP Server: Error executing ADK tool '{name}': {e}")
            # Return error message in MCP format
            # More robust MCP error responses can be implemented
            error_text = json.dumps({"error": f"Failed to execute tool '{name}': {str(e)}"})
            return [mcp_types.TextContent(type="text", text=error_text)]
    else:
        # Handle unknown tool calls
        print(f"MCP Server: Tool '{name}' not found.")
        error_text = json.dumps({"error": f"Tool '{name}' not implemented."})
        # Simply return the error as TextContent
        return [mcp_types.TextContent(type="text", text=error_text)]

#-----------------------[run_server]-----------------------
async def run_server():
    """
    Runs the MCP server using standard input/output.

    This function starts the server using the MCP library's stdio_server context manager, performs the handshake, and enters the main event loop to handle requests and tool execution.
    Used as the main entry point for the MCP server process.

    Returns:
        None
    """
  
    # Use the MCP library's stdio_server context manager
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        print("MCP Server starting handshake...")
        # Start the MCP server run loop.
        # This call performs the protocol handshake using the provided read/write streams,
        # registers the server via the supplied InitializationOptions (name, version, capabilities),
        # and then enters the main asynchronous message-processing loop.
        # While running, the MCP server will receive incoming MCP messages (e.g., list_tools, call_tool),
        # dispatch them to the registered handlers defined above, and write responses back over the
        # write stream. The call completes when the client disconnects or the streams are closed.
        #
        # Note: `read_stream` and `write_stream` are connected to the subprocess stdio (from
        # `mcp.server.stdio.stdio_server()`), so this is suitable for subprocess-based MCP transports.
        await mcp_svr_app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=mcp_svr_app.name, # Use the server name defined above
                server_version="0.1.0",
                capabilities=mcp_svr_app.get_capabilities(
                    # Define server capabilities - see MCP documentation
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
