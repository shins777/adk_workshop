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
from google.adk.sessions import BaseSessionService
from google.adk.runners import Runner
from google.adk.memory import BaseMemoryService

from memory import agent

#--------------------------------[orchestrate_search_and_recall]----------------------------------

async def orchestrate_search_and_recall(
    session_service: BaseSessionService,
    memory_service: BaseMemoryService,
    app_name: str,
    user_id: str,
):
    """
    Orchestrates a workflow that first runs a search agent and then a recall agent.

    This function initializes a Runner with the provided session and memory services,
    executes the search agent in a dedicated session, stores the session results in memory,
    and then runs the recall agent in a separate session to retrieve information from memory.

    Args:
        session_service (BaseSessionService): The session service for managing user sessions.
        memory_service (BaseMemoryService): The memory service for storing and retrieving session data.
        app_name (str): The name of the application.
        user_id (str): The user identifier.

    Returns:
        None
    """

    runner = Runner(agent=agent.search_agent,
                    app_name=app_name,
                    session_service=session_service,
                    memory_service=memory_service)

    # Use different session. 
    search_session_id = "search_session_id"
    await run_search_agent(runner,app_name,user_id,search_session_id,)

    recall_session_id = "recall_session_id"
    await run_recall_agent(runner,app_name,user_id,recall_session_id,)

#--------------------------------[run_search_agent]----------------------------------

async def run_search_agent(runner:Runner,
                     app_name,
                     user_id,
                     session_id,):    

    """
    Runs the search agent in a dedicated session and stores the session results in memory.

    This function creates a new session for the search agent, prompts the user for input,
    sends the query to the agent, and prints the agent's final response. After the interaction,
    it adds the completed session to the memory service for later retrieval.

    Args:
        runner (Runner): The Runner instance managing agent execution.
        app_name (str): The name of the application.
        user_id (str): The user identifier.
        session_id (str): The session identifier for the search agent.

    Returns:
        None
    """


    search_session = await runner.session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id,
    )

    query = input("\n 👤 User: ")
    if query.lower() == "exit":
        return
    
    content_search = types.Content(role='user', parts=[types.Part(text=query)])

    async for event in runner.run_async(user_id=search_session.user_id, 
                            session_id=search_session.id, 
                            new_message=content_search):
        
        if event.is_final_response():
            final_response_text = event.content.parts[0].text
            print(f"Agent 1 Final Response: {final_response_text}")


    completed_session_1 = await runner.session_service.get_session(app_name=search_session.app_name, 
                                                      user_id=search_session.user_id, 
                                                      session_id=search_session.id)

    print("\n--- Adding search session to Memory ---")
    await runner.memory_service.add_session_to_memory(completed_session_1)
    print("Session added to memory.")

#--------------------------------[run_recall_agent]----------------------------------

async def run_recall_agent(runner:Runner,
                           app_name,
                           user_id,
                           session_id,): 
    """
    Runs the recall agent in a dedicated session to retrieve information from memory.

    This function creates a new session for the recall agent, prompts the user for input,
    sends the query to the agent, and prints the agent's final response. The recall agent
    is expected to use the memory service to provide answers based on previously stored sessions.

    Args:
        runner (Runner): The Runner instance managing agent execution.
        app_name (str): The name of the application.
        user_id (str): The user identifier.
        session_id (str): The session identifier for the recall agent.

    Returns:
        None
    """

    recall_session = await runner.session_service.create_session(app_name=app_name, 
                                                    user_id=user_id, 
                                                    session_id=session_id)

    runner.agent = agent.recall_agent
    
    recall_instruction = input("\n 👤 User: ")
    if recall_instruction.lower() == "exit":
        return
    
    content_recall = types.Content(role='user', parts=[types.Part(text=recall_instruction)])

    async for event in runner.run_async(user_id=recall_session.user_id, 
                                  session_id=recall_session.id, 
                                  new_message=content_recall):

        print(f"  Event: {event.author} - Type: {'Text' if event.content and event.content.parts and event.content.parts[0].text else ''}"
            f"{'FuncCall' if event.get_function_calls() else ''}"
            f"{'FuncResp' if event.get_function_responses() else ''}")
        
        if event.is_final_response():
            final_response_text_2 = event.content.parts[0].text
            print(f"\n 🤖 AI Assistant: {final_response_text_2}")
            break 
