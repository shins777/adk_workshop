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
    에이전트 실행 전에 호출되는 전처리 콜백입니다.

    이 함수는 CallbackContext에서 현재 상태를 확인합니다. 만약 상태에 'skip_agent'가 True로 설정되어 있으면,
    에이전트 실행을 중단하고 사용자에게 커스텀 응답을 반환합니다. 그렇지 않으면 None을 반환해 에이전트가 정상적으로 실행되도록 합니다.

    인자:
        callback_context (CallbackContext): 에이전트 정보와 상태를 담은 컨텍스트

    반환값:
        Optional[types.Content]: 에이전트 실행을 건너뛰어야 할 경우 커스텀 Content 응답, 아니면 None(정상 실행)
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
    에이전트 실행 후에 호출되는 후처리 콜백입니다.

    이 함수는 CallbackContext에서 현재 상태를 확인합니다. 만약 상태에 'check_response'가 True로 설정되어 있으면,
    사용자에게 커스텀 응답을 반환하고 이후 처리를 중단합니다. 그렇지 않으면 None을 반환해 에이전트의 정상 실행을 계속합니다.

    인자:
        callback_context (CallbackContext): 에이전트 정보와 상태를 담은 컨텍스트

    반환값:
        Optional[types.Content]: 후처리가 필요한 경우 커스텀 Content 응답, 아니면 None(정상 실행)
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