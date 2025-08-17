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

import os
from dotenv import load_dotenv

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters

load_dotenv()

def mcp_google_map():

    """
    Initialize the MCP Google Map toolset with the API key from environment variables.
    As of Aug 2025, Google Map API is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
    
    """

    # Load the Google Maps API key from environment variables
    google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    # If the API key is not set, raise an exception to prevent running without credentials
    if not google_maps_api_key:
        raise RuntimeError("GOOGLE_MAPS_API_KEY is not set. Please set it as an environment variable.")
    else:
        # Create the MCPToolset for Google Maps, passing the API key to the server environment
        mcp_google_map = MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='npx',
                    args=[
                        "-y",
                        "@modelcontextprotocol/server-google-maps",
                    ],
                    env={
                        "GOOGLE_MAPS_API_KEY": google_maps_api_key
                    }
                ),
            ),
            # Optionally, you can filter for specific Maps tools:
            # tool_filter=['get_directions', 'find_place_by_id']
        )
        return mcp_google_map


mcp_google_map_tool = mcp_google_map()

INSTRUCTION = """
    You are an agent that helps users with mapping, directions, and finding places using Google Maps tools.
    When a user asks a question, you must use the 'mcp_google_map_tool' to provide an answer based on the results.
"""

root_agent = LlmAgent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name='Assistant_agent_Google_Map',
    instruction=INSTRUCTION,
    tools=[mcp_google_map_tool]
        
)

