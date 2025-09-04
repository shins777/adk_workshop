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
    Pre-processing callback invoked before agent execution.

    This function inspects the current state from the CallbackContext. If the state's
    'skip_agent' flag is set to True, it aborts agent execution and returns a custom
    response to the user. Otherwise it returns None to allow the agent to run normally.

    Args:
        callback_context (CallbackContext): Context containing agent info and state
    Returns:
        Optional[types.Content]: Custom Content response when skipping the agent, or None to continue.
    """

    # Retrieve context information from CallbackContext.
    agent_name = callback_context.agent_name
    current_state = callback_context.state.to_dict()

    # Control pre-execution flow based on state information.
    if current_state.get("skip_agent", False):
        print(f"[Before Agent] Condition met: skipping agent execution due to state flag - Agent: {agent_name} : Current State: {current_state}")

        # Create a Content response to return to the user without calling the agent.
        return_content = types.Content(
            parts=[types.Part(text=f"Agent {agent_name} was skipped by before_agent_callback due to the user's state flag.")],
            role="model"  # set the role of the response to 'model'
        )
        return return_content
    else:  # Return None to allow the agent to execute normally.
        print(f"[Before Agent] Executing agent - {agent_name} in progress.")
        return None  # Returning None lets the LlmAgent run as normal.



#----------------------------------[ callback_after_agent ]------------------------------------

def callback_after_agent(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Post-processing callback invoked after agent execution.

    This function inspects the current state from the CallbackContext. If the state's
    'check_response' flag is set, it returns a custom response to the user and halts
    further processing. Otherwise it returns None to continue normal post-agent flow.

    Args:
        callback_context (CallbackContext): Context containing agent info and state
    Returns:
        Optional[types.Content]: Custom Content response for post-processing, or None to continue.
    """
    
    # Retrieve context information from CallbackContext.
    agent_name = callback_context.agent_name
    current_state = callback_context.state.to_dict()

    print(f"[After Agent] current_state : Current State: {current_state}")

    # Control post-execution flow based on state information.
    if current_state.get("check_response"):
        print(f"[After Agent] Condition met: handling post-agent response - {agent_name} : Current State: {current_state}")

        print(f"## Callback context info : {callback_context}")
        # Stop further processing after agent call and create a notification Content for the user.
        return types.Content(
            parts=[types.Part(text=f"The agent {agent_name}'s callback was executed after the agent call due to the state flag.")],
            role="model"  # set the role of the response to 'model'
        )
    
    else:
        print(f"[After Agent] Condition not met: continuing agent {agent_name}.")
        return None  # Returning None lets the LlmAgent continue as normal