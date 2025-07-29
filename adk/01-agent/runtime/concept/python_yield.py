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

"""
아래 내용은 AI 에이전트 내에서 서브 에이전트(Sub Agent)가 작동하는 방식을 파이썬(Python)의 yield 구문에 비유하여 설명하고 있습니다.
핵심은 위임과 재개의 흐름입니다.

위임 및 일시 중단: 메인 에이전트는 특정 작업을 서브 에이전트에게 위임하고, 자신은 잠시 동작을 멈춥니다.
작업 처리 및 결과 반환: 서브 에이전트는 위임받은 작업을 수행한 뒤 결과를 yield하게 됩니다.
재개: 메인 에이전트는 서브 에이전트처리가 완료되면 다음 작업을 이어서 수행합니다.
결론적으로, 이 방식은 특정 작업을 서브 에이전트에 맡겨 처리하게 함으로써 작업의 흐름을 효율적으로 구성하는 모델입니다.
"""
import time
def count_up_to(max_number):
    number = 0
    while number < max_number:
        # 숫자를 반환하고 함수 실행을 일시 중단한 뒤, 처리가 끝나면 실행을 재개하여 반환합니다.
        yield number  
        print("count_up_to에서 yield 이후:", number)
        number += 1

for num in count_up_to(5):
    print(num)  # 0, 1, 2, 3, 4 출력
    time.sleep(1)  # 1초 대기
    print("반복문에서 yield됨:", num)  # 반복문에서 yield됨: 0, 1, ...