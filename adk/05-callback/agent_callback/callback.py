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

from google.genai import types 
from typing import Optional
from google.adk.agents.callback_context import CallbackContext

#----------------------------------[ callback_before_agent ]------------------------------------

def callback_before_agent(callback_context: CallbackContext) -> Optional[types.Content]:

    """
    Pre-processing callback executed before the agent runs.

    This function inspects the current state from the CallbackContext. If the state contains
    'skip_agent' set to True, it prevents the agent from running and returns a custom response
    to the user. Otherwise, it allows the agent to proceed by returning None.

    Args:
        callback_context (CallbackContext): The context containing agent information and state.

    Returns:
        Optional[types.Content]: A custom Content response if the agent should be skipped,
        or None to proceed with normal agent execution.
    """

    # Get the contextual information from CallbackContext
    agent_name = callback_context.agent_name
    current_state = callback_context.state.to_dict()

    # Check the information in the state to control flow berfore calling the agent. 
    if current_state.get("skip_agent", False):
        print(f"[Before Agent] State condition met, don't run agent due to command in state - Agent: {agent_name} : Current State: {current_state}")

        # Build a content to be returned back to user without calling agent.
        return_content = types.Content(
            parts=[types.Part(text=f"Agent {agent_name} skipped by before_agent_callback due to user's command.")],
            role="model" # Assign model role to the overriding response
        )
        return return_content
    else: # If the condition is OK to go to run agent, the return response shoud be just None. 
        
        print(f"[Before Agent] Run agent - Proceeding with agent {agent_name}.")
        return None  # Return None to allow the LlmAgent's normal execution


#----------------------------------[ callback_after_agent ]------------------------------------

def callback_after_agent(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Post-processing callback executed after the agent runs.

    This function examines the current state from the CallbackContext. If the state contains
    'check_response' set to True, it returns a custom response to the user and halts further
    processing. Otherwise, it allows the agent's normal execution to continue by returning None.

    Args:
        callback_context (CallbackContext): The context containing agent information and state.

    Returns:
        Optional[types.Content]: A custom Content response if post-processing is required,
        or None to proceed with normal agent execution.
    """
    
    # Get the contextual information from CallbackContext
    agent_name = callback_context.agent_name
    current_state = callback_context.state.to_dict()

    # Check the information in the state to control flow after calling the agent. 
    if current_state.get("check_response", False):
        print(f"[After Agent] State condition met : Manage the response after calling agent : {agent_name} : Current State: {current_state}")

        # Stop the remained process after this agent called and build a content to notify to user. 
        return types.Content(
            parts=[types.Part(text=f"Agent {agent_name}'s callback function was called after calling the agent due to state.")],
            role="model" # Assign model role to the overriding response
        )
    else:
        print(f"[After Agent] State condition not met: Proceeding with agent {agent_name} forward.")
        return None # Return None to allow the LlmAgent's normal execution