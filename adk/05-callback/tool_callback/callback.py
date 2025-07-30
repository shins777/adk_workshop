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

from typing import Dict, Any
from copy import deepcopy
from typing import Optional

from google.adk.tools.tool_context import ToolContext
from google.adk.tools.base_tool import BaseTool

#--------------------------------[get_capital_city]----------------------------------

def get_capital_city(country: str) -> dict:

    """
    주어진 국가의 수도를 반환하는 LLM 함수 호출용 툴 함수입니다.

    이 함수는 미리 정의된 딕셔너리에서 해당 국가의 수도를 조회합니다.
    국가가 목록에 없으면 수도를 찾을 수 없다는 메시지를 반환합니다.

    인자:
        country (str): 조회할 국가명

    반환값:
        str: 해당 국가의 수도 또는 정보를 찾을 수 없을 때의 메시지
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
    툴이 호출되기 전에 실행되는 전처리 콜백입니다.

    이 함수는 툴 이름과 인자를 검사하여,
    툴이 'get_capital_city'이고 country 인자가 'Dubai'인 경우,
    인자를 'UAE'로 변경합니다. 그 외에는 원래 인자를 그대로 사용합니다.

    인자:
        tool (BaseTool): 호출될 툴 인스턴스
        args (Dict[str, Any]): 툴에 전달되는 인자
        tool_context (ToolContext): 에이전트 및 툴 정보를 담은 컨텍스트

    반환값:
        Optional[Dict]: 인자가 변경된 경우 수정된 딕셔너리, 아니면 None(원본 인자 사용)
    """

    # CallbackContext에서 컨텍스트 정보를 가져옵니다.
    agent_name = tool_context.agent_name
    tool_name = tool.name

    print(f"[Before Tool] Tool call for tool '{tool_name}' in agent '{agent_name}' and args: {args}")

    if tool_name == 'get_capital_city' and args.get('country', '').lower() == 'korea':
        args['country'] = 'south korea'
        print(f"[Before Tool] 'Korea'가 감지되었습니다. args를 'south korea'로 수정합니다. : {args}")
        return None
    else:
        print(f"[Before Tool] 원래 인수를 전달합니다. : {args}")
        return None

#--------------------------------[callback_after_tool]----------------------------------

def callback_after_tool(tool: BaseTool, 
                        args: Dict[str, Any], 
                        tool_context: ToolContext, 
                        tool_response: Dict
                        ) -> Optional[Dict]:
    """
    툴이 호출된 후 실행되는 후처리 콜백입니다.

    이 함수는 툴의 응답을 검사하여,
    툴이 'get_capital_city'이고 결과가 'Seoul'인 경우,
    응답에 '서울은 대한민국의 수도'라는 노트를 추가해 반환합니다.
    그 외에는 원래 응답을 그대로 사용합니다.

    인자:
        tool (BaseTool): 호출된 툴 인스턴스
        args (Dict[str, Any]): 툴에 전달된 인자
        tool_context (ToolContext): 에이전트 및 툴 정보를 담은 컨텍스트
        tool_response (Dict): 툴이 반환한 응답

    반환값:
        Optional[Dict]: 응답이 변경된 경우 수정된 딕셔너리, 아니면 None(원본 응답 사용)
    """

    # Get the contextual information from CallbackContext
    agent_name = tool_context.agent_name
    tool_name = tool.name

    print(f"[After Tool] Tool call for tool '{tool_name}' in agent '{agent_name}' and args: {args}, tool_response: {tool_response}")

    original_tool_response  = tool_response.get('result', '')


    # If the tool was 'get_capital_city' and result is 'Seoul'
    if tool_name == 'get_capital_city' and original_tool_response.lower() == "seoul" :
        print("[After Tool] '서울'을 감지했습니다. 도구 응답을 수정합니다.")

        # Note: Create a new response.
        modified_response = deepcopy(tool_response)
        modified_response["result"] = f"{original_tool_response} (Note: 이곳은 대한민국의 수도입니다)."
        modified_response["note_added_by_callback"] = True # Add extra info if needed

        print(f"[After Tool] Modified tool_response: {modified_response}")
        return modified_response # Return the modified dictionary
    else:
        print("[After Tool] Passing original tool response through.")
        return None # Return None to use the original tool_response