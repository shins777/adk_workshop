import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search

load_dotenv()

def build_agent():
    """
    Google Search 도구 지원이 포함된 Agent 인스턴스를 생성하고 구성합니다.

    이 함수는 환경 변수를 로드하고, 에이전트의 안내 템플릿을 설정하며,
    이름, 모델, 설명, 안내문, Google Search 도구, output_key를 포함하여 Agent를 초기화합니다.
    이 에이전트는 자체 지식과 검색 기능을 모두 활용하여 사용자 문의에 답변하도록 설계되었습니다.

    반환값:
        Agent: 사용자 질의 처리가 가능한 구성된 Agent 인스턴스
    """

    INSTRUCTION = """
        당신은 사용자의 질문에 답변을 제공하는 에이전트입니다.
        사용자가 질문을 입력하면, 해당 질문에 대해 Google 검색(tool:google_search)을 수행하고 결과를 바탕으로 답변을 제공해야 합니다. 전체적으로 답변은 간결하고 명확해야 하며 5줄 이내로 답해주세요, 사용자가 질문한 언어로 작성되어야 합니다.
        
    """

    search_agent = Agent(
        name = "search_agent",
        model = os.getenv("GOOGLE_GENAI_MODEL"),
        description = "사용자 질의에 답변하는 에이전트",
        instruction = INSTRUCTION,
        tools=[google_search],
        output_key = "last_turn"
    )
    return search_agent

root_agent = build_agent()
