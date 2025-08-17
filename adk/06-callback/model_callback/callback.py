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
from google.adk.models import LlmResponse, LlmRequest

#--------------------------------[callback_before_model]----------------------------------

def callback_before_model(callback_context: CallbackContext, 
                         llm_request: LlmRequest
                         ) -> Optional[LlmResponse]:
    """
    LLM 모델이 호출되기 전에 실행되는 Callback function입니다.

    이 함수는 에이전트 상태에 정의된 특정 키워드가 사용자의 마지막 메시지에 포함되어 있는지 확인합니다.
    키워드가 감지되면 LLM 호출을 차단하고 커스텀 응답 메시지를 반환합니다.
    그렇지 않으면 None을 반환해 LLM 호출이 정상적으로 진행되도록 합니다.

    인자:
        callback_context (CallbackContext): 에이전트 정보와 상태를 담은 컨텍스트
        llm_request (LlmRequest): 사용자 입력과 메시지 내용을 담은 요청 객체

    반환값:
        Optional[LlmResponse]: 키워드가 감지된 경우 커스텀 LlmResponse, 아니면 None(정상 호출)
    """
    
    # CallbackContext에서 컨텍스트 정보를 가져옵니다.
    agent_name = callback_context.agent_name
    current_state = callback_context.state.to_dict()
    keyword = current_state.get("keyword").lower()

    # 요청 내용의 마지막 사용자 메시지를 검사합니다.
    last_user_message = ""
    if llm_request.contents and llm_request.contents[-1].role == 'user':
         if llm_request.contents[-1].parts:
            last_user_message = llm_request.contents[-1].parts[0].text.lower()

    print(f"[Before Model] Agent Name : {agent_name} Keyworkd : {keyword} - 마지막 메시지 '{last_user_message}'")

    # 사용자 메시지에서 바람직하지 않은 키워드가 포함되어 있는지 확인하세요.
    if keyword in last_user_message:        
        print(f"[Before Model] 사용자 쿼리에서 {keyword} 키워드로 문의하는 것이 감지되었습니다. LLM 호출을 건너뜁니다.")
        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part(text="키워드를 사용할 수 없으므로 LLM 호출이 콜백 함수에 의해 차단되었습니다.")],
            )
        )
    else:
        print(f"[Before Model] 사용자 쿼리에서 위반된 특정 {keyword} 키워드가 감지되지 않았습니다. LLM 호출을 진행합니다.")
        return None

#--------------------------------[callback_after_model]----------------------------------
    
def callback_after_model(callback_context: CallbackContext, 
                        llm_response: LlmResponse
                        ) -> Optional[LlmResponse]:
    """
    LLM 모델이 응답을 생성한 후 실행되는 Callback function 입니다.

    이 함수는 에이전트 상태에 정의된 특정 키워드가 LLM 응답에 포함되어 있는지 확인합니다.
    키워드가 감지되면 원래 LLM 응답을 차단하고 커스텀 메시지를 반환합니다.
    그렇지 않으면 None을 반환해 원래 응답이 정상적으로 전달되도록 합니다.

    인자:
        callback_context (CallbackContext): 에이전트 정보와 상태를 담은 컨텍스트
        llm_response (LlmResponse): LLM 모델이 생성한 응답 객체

    반환값:
        Optional[LlmResponse]: 키워드가 감지된 경우 커스텀 LlmResponse, 아니면 None(정상 응답)
    """

    # CallbackContext에서 컨텍스트 정보를 가져옵니다.
    agent_name = callback_context.agent_name
    current_state = callback_context.state.to_dict()
    keyword = current_state.get("keyword").lower()

    llm_response_message = ""
    if llm_response.content and llm_response.content.parts:
        llm_response_message = llm_response.content.parts[0].text.lower()

    print(f"[After Model] Agent Name : {agent_name} Keyworkd : {keyword} - 메시지 검사: '{llm_response_message}'")

    if keyword in llm_response_message:

        print(f"[After Model] {keyword} AI 응답에서 키워드가 발견되었습니다. 수신된 모델 응답을 사용자에게 회신하지 마세요..")
        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part(text=f"모델 호출 응답은 callback_after_model로 인해 차단되었습니다. {keyword} 키워드가 응답에 포함되어 있습니다.")],
            )
        )
    else:
        print(f"[After Model] 모델 응답에서 특정 {keyword}를 찾을 수 없습니다. 모델 호출에 대한 응답을 진행합니다.")
        return None
