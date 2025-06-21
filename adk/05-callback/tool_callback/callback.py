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

from typing import Dict, Any
from copy import deepcopy
from typing import Optional

from google.adk.tools.tool_context import ToolContext
from google.adk.tools.base_tool import BaseTool

#--------------------------------[get_capital_city]----------------------------------

def get_capital_city(country: str) -> dict:

    """
    Tool function for LLM function calling that returns the capital city of a given country.

    This function looks up the capital city for the specified country from a predefined dictionary.
    If the country is not found, it returns a message indicating that the capital was not found.

    Args:
        country (str): The name of the country to look up.

    Returns:
        str: The capital city of the specified country, or a not found message if unavailable.
    """
    country_capitals = {
        "south korea": "Seoul",
        "japan": "Tokyo",
        "us": "Washington, D.C.",        
        "uk": "London",
        "france": "Paris",
        "germany": "Berlin",
        "italy": "Rome",
    }

    tool_response = { "result" : country_capitals.get(country.lower(), f"None") }

    return tool_response

    # return country_capitals.get(country.lower(), f"Capital not found for {country}")

#--------------------------------[callback_before_tool]----------------------------------

def callback_before_tool(tool: BaseTool, 
                         args: Dict[str, Any], 
                         tool_context: ToolContext
                        ) -> Optional[Dict]:
    """
    Pre-processing callback executed before a tool is called.

    This function inspects the tool name and arguments before the tool is executed.
    If the tool is 'get_capital_city' and the country argument is 'Dubai', it modifies
    the argument to use 'UAE' instead. Otherwise, it allows the original arguments to proceed.

    Args:
        tool (BaseTool): The tool instance that will be called.
        args (Dict[str, Any]): The arguments passed to the tool.
        tool_context (ToolContext): The context containing agent and tool information.

    Returns:
        Optional[Dict]: Modified arguments dictionary if changes are made, or None to use the original arguments.
    """

    # Get the contextual information from CallbackContext
    agent_name = tool_context.agent_name
    tool_name = tool.name

    print(f"[Before Tool] Tool call for tool '{tool_name}' in agent '{agent_name}' and args: {args}")

    if tool_name == 'get_capital_city' and args.get('country', '').lower() == 'korea':
        args['country'] = 'south korea'
        print(f"[Before Tool] Detected 'Korea'. Modifying args to 'south korea'. : {args}")
        return None
    else:
        print(f"[Before Tool] Passing original args through. : {args}")
        return None

#--------------------------------[callback_after_tool]----------------------------------

def callback_after_tool(tool: BaseTool, 
                        args: Dict[str, Any], 
                        tool_context: ToolContext, 
                        tool_response: Dict
                        ) -> Optional[Dict]:
    """
    Post-processing callback executed after a tool has been called.

    This function inspects the tool's response and, if the tool is 'get_capital_city' and the result is 'Seoul',
    it modifies the response to add a note indicating that Seoul is the capital of South Korea. Otherwise,
    it allows the original tool response to proceed unchanged.

    Args:
        tool (BaseTool): The tool instance that was called.
        args (Dict[str, Any]): The arguments passed to the tool.
        tool_context (ToolContext): The context containing agent and tool information.
        tool_response (Dict): The response returned by the tool.

    Returns:
        Optional[Dict]: A modified tool response dictionary if changes are made, or None to use the original response.
    """

    # Get the contextual information from CallbackContext
    agent_name = tool_context.agent_name
    tool_name = tool.name

    print(f"[After Tool] Tool call for tool '{tool_name}' in agent '{agent_name}' and args: {args}, tool_response: {tool_response}")

    original_tool_response  = tool_response.get('result', '')


    # If the tool was 'get_capital_city' and result is 'Seoul'
    if tool_name == 'get_capital_city' and original_tool_response.lower() == "seoul" :
        print("[After Tool] Detected 'Seoul'. Modifying tool response.")

        # Note: Create a new response.
        modified_response = deepcopy(tool_response)
        modified_response["result"] = f"{original_tool_response} (Note: This is the capital of the South Korea)."
        modified_response["note_added_by_callback"] = True # Add extra info if needed

        print(f"[After Tool] Modified tool_response: {modified_response}")
        return modified_response # Return the modified dictionary
    else:
        print("[After Tool] Passing original tool response through.")
        return None # Return None to use the original tool_response