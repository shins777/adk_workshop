import asyncio
import time
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from state import agent

#--------------------------------[run_agent]----------------------------------

async def run_agent( app_name: str,
                     user_id: str,
                     session_id: str,):
    """
    세션 상태 변화를 표시하며 에이전트를 대화 루프에서 실행합니다.

    이 함수는 사용자와 애플리케이션에 대한 세션을 생성한 후,
    사용자 입력을 받아 에이전트에 전달하고, 에이전트의 응답을 출력합니다.
    각 상호작용 후에는 업데이트된 세션 상태를 조회하여 에이전트의 상태가 어떻게 변화하는지 보여줍니다.

    인자:
        app_name (str): 애플리케이션 이름
        user_id (str): 사용자 식별자
        session_id (str): 세션 식별자

    반환값:
        없음
    """

    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=app_name, 
                                            user_id=user_id, 
                                            session_id=session_id)

    runner = Runner(agent=agent.root_agent,
                    app_name=app_name,
                    session_service=session_service)
    
    print(f"초기 상태: {session.state}")

    while True:

        user_input = input("\n 👤 User: ")
        if user_input.lower().strip() in ["exit", "quit", "bye"]:
            break

        content = types.Content(role='user', parts=[types.Part(text=user_input)])

        events = runner.run_async(user_id=user_id,
                                session_id=session_id,
                                new_message=content,)

        async for event in events:
            if event.is_final_response():
                final_response = event.content.parts[0].text            
                print("\n 🤖 AI Assistant: " + final_response)

        updated_session = await session_service.get_session(app_name = app_name, 
                                                     user_id = user_id, 
                                                     session_id = session_id)

        print(f"\nState after agent run: {updated_session.state}")
        print(f"\nState after agent run - last_turn : {updated_session.state['last_turn']}")

#--------------------------------[__main__]----------------------------------

if __name__ == "__main__":
    import asyncio
    import argparse

    print("Running the agent...")
    print("Usage : uv run -m state.output_key --app_name <app_name> --user_id <user_id> --session_id <session_id>")

    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    parser.add_argument("--app_name",type=str,help="The application name of this agent.",)
    parser.add_argument("--user_id",type=str,help="The user name interacting with this agent",)
    parser.add_argument("--session_id",type=str,help="The session id to identify the session of this agent",)
    args = parser.parse_args()

    asyncio.run(run_agent(app_name = args.app_name, 
                          user_id = args.user_id, 
                          session_id = args.session_id,))
