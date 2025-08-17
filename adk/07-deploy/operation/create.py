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
import argparse

from operation import util

load_dotenv()

if __name__ == "__main__":

    print(""" Usage : uv run -m operation.create --display_name adk_agent_20250728 """)
    
    parser = argparse.ArgumentParser(description="Create a new Agent Engine.")
    parser.add_argument("--display_name",type=str,help="The display name of agent",)
    args = parser.parse_args()
    
    DISPLAY_NAME = args.display_name.strip()
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
    AGENT_ENGINE_BUCKET = os.getenv("AGENT_ENGINE_BUCKET")

    #1. 등록된 모든 에이전트를 인쇄하세요.
    util.show_agents()

    #2. 원격 에이전트 엔진 인스턴스를 생성합니다.
    util.create_agent(display_name= DISPLAY_NAME,
                  project_id=PROJECT_ID,
                  location=LOCATION,
                  gcs_dir_name=AGENT_ENGINE_BUCKET,
                  description="사용자 질문에 대한 AI Agent Engine",)
    
