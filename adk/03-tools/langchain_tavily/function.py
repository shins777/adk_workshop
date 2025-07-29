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

def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "KRW",
    currency_date: str = "latest", )->dict:
    """
    지정한 날짜에 두 통화 간의 환율을 조회합니다.

    Frankfurter API(https://api.frankfurter.app/)를 사용하여
    환율 데이터를 가져옵니다.

    인자:
        currency_from: 기준 통화(3자리 통화 코드). 기본값은 "USD"(미국 달러).
        currency_to: 대상 통화(3자리 통화 코드). 기본값은 "KRW"(원화).
        currency_date: 환율을 조회할 날짜. 기본값은 "latest"로 최신 환율 데이터를 의미합니다.
            과거 환율은 YYYY-MM-DD 형식으로 지정할 수 있습니다.

    반환값:
        dict: 환율 정보가 담긴 딕셔너리.
            예시: {"amount": 1.0, "base": "USD", "date": "2023-11-24", "rates": {"EUR": 0.95534}}
    """
    import requests
    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()