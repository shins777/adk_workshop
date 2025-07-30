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

    # CallbackContext에서 컨텍스트 정보를 가져옵니다.
    agent_name = callback_context.agent_name
    current_state = callback_context.state.to_dict()

    # 상태 정보를 확인하여 에이전트 실행 전 흐름을 제어합니다.
    if current_state.get("skip_agent", False):
        print(f"[Before Agent] 상태 조건 충족: state 명령에 따라 에이전트 실행하지 않음 - Agent: {agent_name} : Current State: {current_state}")

        # 에이전트를 호출하지 않고 사용자에게 반환할 Content를 생성합니다.
        return_content = types.Content(
            parts=[types.Part(text=f"Agent {agent_name}가 사용자의 명령에 의해 before_agent_callback에서 건너뛰어졌습니다.")],
            role="model" # 응답의 역할을 model로 지정
        )
        return return_content
    else: # 조건이 정상일 경우 None을 반환하여 에이전트가 실행되도록 합니다.
        print(f"[Before Agent] 에이전트 실행 - {agent_name} 진행 중.")
        return None  # None 반환 시 LlmAgent가 정상적으로 실행됨



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
    
    # CallbackContext에서 컨텍스트 정보를 가져옵니다.
    agent_name = callback_context.agent_name
    current_state = callback_context.state.to_dict()

    print(f"[After Agent] current_state : Current State: {current_state}")

    # 상태 정보를 확인하여 에이전트 실행 후 흐름을 제어합니다.
    if current_state.get("check_response"):
        print(f"[After Agent] 상태 조건 충족: 에이전트 호출 후 응답 관리 - {agent_name} : Current State: {current_state}")

        # 에이전트 호출 후 남은 프로세스를 중단하고 사용자에게 알림 Content를 생성합니다.
        return types.Content(
            parts=[types.Part(text=f"Agent {agent_name}의 콜백 함수가 상태에 의해 에이전트 호출 후 실행되었습니다.")],
            role="model" # 응답의 역할을 model로 지정
        )
    else:
        print(f"[After Agent] 상태 조건 미충족: 에이전트 {agent_name} 진행.")
        return None # None 반환 시 LlmAgent가 정상적으로 실행됨