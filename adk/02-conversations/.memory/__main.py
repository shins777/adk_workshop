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
import asyncio
import argparse
from dotenv import load_dotenv

from google.adk.sessions import InMemorySessionService
from google.adk.memory import VertexAiRagMemoryService
from google.adk.memory import InMemoryMemoryService 

from memory import runner

if __name__ == "__main__":

    load_dotenv()

    print("에이전트를 실행합니다...")
    print("사용법 : uv run memory.main --memory_type [in_memory|rag_corpus] --app_name <app_name> --user_id <user_id>")
    print("사용 가능한 memory_type : in_memory, rag_corpus")

    parser = argparse.ArgumentParser(description="사용자 질의와 함께 ADK 에이전트를 실행합니다.")
    parser.add_argument("--memory_type",type=str,help="세션의 유형",)
    parser.add_argument("--app_name",type=str,help="이 에이전트의 애플리케이션 이름.",)
    parser.add_argument("--user_id",type=str,help="이 에이전트와 상호작용하는 사용자 이름",)
    args = parser.parse_args()
    
    session_service = InMemorySessionService()

    if args.memory_type == "in_memory":
        memory_service = InMemoryMemoryService()
    
    elif args.memory_type == "rag_corpus":

        PROJECT_ID = os.environ['PROJECT_ID']
        LOCATION = os.environ['LOCATION']
        CORPUS_ID = os.environ['CORPUS_ID']
        
        RAG_CORPUS_RESOURCE_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/ragCorpora/{CORPUS_ID}"

        memory_service = VertexAiRagMemoryService(
            rag_corpus=RAG_CORPUS_RESOURCE_NAME,
            similarity_top_k=10,
            vector_distance_threshold=0.2
        )
    
    else:
        raise ValueError("유효하지 않은 세션 유형입니다. 'in_memory' 또는 'rag_corpus' 중에서 선택하세요.")

    asyncio.run(runner.orchestrate_search_and_recall(session_service = session_service, 
                                 memory_service = memory_service,
                                 app_name = args.app_name, 
                                 user_id = args.user_id, 
                                 ))
