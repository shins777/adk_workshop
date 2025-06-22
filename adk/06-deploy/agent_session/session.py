import os 
import argparse
import asyncio
from dotenv import load_dotenv

from google.genai import types
from google.adk.sessions import VertexAiSessionService
from google.adk.runners import Runner

from agent_session import agent

load_dotenv()

#-----------------------------[call_agent]-----------------------------

def call_agent(runner, 
               user_id:str,
               session_id:str,
               query:str):
    """
    사용자 쿼리를 에이전트에 전달하고 에이전트의 응답을 출력합니다.

    이 함수는 사용자의 입력으로 메시지를 생성하여 runner를 통해 에이전트에 전달하고,
    응답 이벤트를 순회합니다. 최종 응답이 도착하면 에이전트의 답변을 콘솔에 출력합니다.

    인자:
        runner: 에이전트 실행에 사용되는 Runner 인스턴스
        user_id (str): 사용자 식별자
        session_id (str): 세션 식별자
        query (str): 에이전트가 처리할 사용자 입력 또는 질문

    반환값:
        None
    """

    content = types.Content(role='user', parts=[types.Part(text=query)])
    
    events = runner.run(
        user_id=user_id, session_id=session_id, new_message=content)

    for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print(f"\n 🤖 AI Assistant: {final_response}\n")

#-----------------------------[run_agent]-----------------------------

def run_agent(agent_engine_id:str,
                    user_id:str,
                    query:str,
                    session_id:str = None,):

    """
    지정한 에이전트 엔진과 세션을 사용해 대화 루프에서 에이전트를 실행합니다.

    이 함수는 사용자 및 애플리케이션에 대한 세션을 생성한 뒤,
    사용자 입력을 받아 에이전트에 전달하고, 에이전트의 응답을 출력하는 루프를 실행합니다.
    사용자가 "exit"를 입력할 때까지 대화가 계속됩니다.

    인자:
        agent_engine_id (str): 에이전트 엔진(앱 이름) 식별자
        user_id (str): 사용자 식별자
        query (str): 초기 사용자 쿼리(루프에서는 사용되지 않음)
        session_id (str, optional): 세션 식별자(미지정 시 새 세션 생성)

    반환값:
        None
    """

    # Create the ADK runner with VertexAiSessionService
    session_service = VertexAiSessionService(os.getenv("PROJECT_ID"), os.getenv("LOCATION"))

    runner = Runner(
        agent=agent.root_agent,
        app_name=agent_engine_id,
        session_service=session_service)

    # Create a session
    session = session_service.create_session(
        app_name=agent_engine_id,
        user_id=user_id,
        session_id=session_id)

    while True:
        query = input("\n 👤 User: ")
        if query.lower() == "exit":
            break

        call_agent(runner, 
                   user_id = user_id, 
                   session_id = session.id, 
                   query = query)

#-----------------------------[__main__]-----------------------------

if __name__ == "__main__":
    
    print(""" 사용법 : uv run -m agent_session.session --agent_engine_id 112774708637728768 --user_id forus --session_id 8517270617299353600 """)
    
    parser = argparse.ArgumentParser(description="사용자 쿼리로 ADK 에이전트를 실행합니다.")
    
    parser.add_argument("--agent_engine_id",type=str)
    parser.add_argument("--user_id",type=str)
    parser.add_argument("--session_id",type=str)
    parser.add_argument("--query",type=str)
    
    args = parser.parse_args()

    agent_engine_id = args.agent_engine_id
    query = args.query
    user_id = args.user_id
    session_id = args.session_id

    run_agent(agent_engine_id=args.agent_engine_id,
                          user_id=args.user_id,
                          session_id=args.session_id,
                          query=args.query)

