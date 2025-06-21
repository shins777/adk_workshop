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

    print("Running the agent...")
    print("Usage : uv run memory.main --memory_type [in_memory|rag_corpus] --app_name <app_name> --user_id <user_id>")
    print("Usage : memory_type : in_memory, rag_corpus")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--memory_type",type=str,help="The type of session",)
    parser.add_argument("--app_name",type=str,help="The application name of this agent.",)
    parser.add_argument("--user_id",type=str,help="The user name interacting with this agent",)
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
        raise ValueError("Invalid session type. Choose 'in_memory' or 'rag_corpus'.")

    asyncio.run(runner.orchestrate_search_and_recall(session_service = session_service, 
                                 memory_service = memory_service,
                                 app_name = args.app_name, 
                                 user_id = args.user_id, 
                                 ))
    