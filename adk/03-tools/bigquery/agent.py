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

import asyncio
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools.bigquery import BigQueryCredentialsConfig
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
from google.genai import types
import google.auth

load_dotenv()

def get_bigquery_toolset() -> BigQueryToolset:
    """
    BigQuery 툴셋을 설정하고 반환합니다.

    이 함수는 BigQuery 인증 정보를 로드하고, BigQuery 툴셋을 초기화하여
    BigQueryToolConfig를 사용해 설정합니다. 이 툴셋은 BigQuery 데이터베이스와 상호작용하는 데 사용됩니다.

    반환값:
        BigQueryToolset: 설정된 BigQuery 툴셋 인스턴스
    """
    # 모든 쓰기 작업을 차단하기 위한 도구 구성을 정의합니다.
    tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

    # 자격 증명 구성을 정의합니다. 이 예에서는 애플리케이션 기본 자격 증명을 사용합니다.
    # https://cloud.google.com/docs/authentication/provide-credentials-adc
    application_default_credentials, _ = google.auth.default()
    credentials_config = BigQueryCredentialsConfig(
        credentials=application_default_credentials
    )

    # Instantiate a BigQuery toolset
    bigquery_toolset = BigQueryToolset(
        credentials_config=credentials_config, bigquery_tool_config=tool_config
    )
    return bigquery_toolset

def build_agent() -> Agent:
    """
    Google Search 툴이 포함된 Agent 인스턴스를 생성하고 설정합니다.

    이 함수는 환경 변수를 불러오고, 에이전트의 지시문 템플릿을 설정하며,
    이 에이전트는 자체 지식과 검색 기능을 활용해 사용자 질문에 답변하도록 설계되었습니다.

    반환값:
        Agent: 사용자 질의를 처리할 준비가 된 설정된 Agent 인스턴스
    """

    INSTRUCTION = """
        BigQuery 데이터 및 모델에 대한 질문에 답변하고 SQL 쿼리를 실행하는 Data science agent 입니다.
        사용자의 다양한 질문에 대해서 BigQuery 데이터베이스에서 정보를 검색하고, SQL 쿼리를 작성하여 실행후 답을 해주세요.
    """
    bigquery_toolset = get_bigquery_toolset()

    agent = Agent(
        name = "search_agent",
        model = os.getenv("GOOGLE_GENAI_MODEL"),
        description = "BigQuery 데이터 및 모델에 대한 질문에 답변하고 SQL 쿼리를 실행하는 Data science agent",
        instruction = INSTRUCTION,
        tools=[bigquery_toolset],
    )
    return agent

root_agent = build_agent()