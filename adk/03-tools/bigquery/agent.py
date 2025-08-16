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
    Configure and return a BigQuery toolset.

    This function loads BigQuery authentication information, initializes the BigQuery toolset,
    and configures it using BigQueryToolConfig. This toolset is used to interact with the BigQuery database.

    Returns:
        BigQueryToolset: Configured BigQuery toolset instance
    """
    # Define tool configuration to block all write operations.
    tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

    # Define credentials configuration. This example uses application default credentials.
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

# Get the bigquery toolset, This will be used in the agent to interact with BigQuery
bigquery_toolset = get_bigquery_toolset()

INSTRUCTION = """
        You are a data science agent that answers questions about BigQuery data and models and executes SQL queries. 
        Retrieve information from the BigQuery database, write SQL queries, execute them, and provide answers to various user questions.
        """

root_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "Data science agent that answers questions about BigQuery data and models and runs SQL queries.",
    instruction = INSTRUCTION,
    tools=[bigquery_toolset],
)
