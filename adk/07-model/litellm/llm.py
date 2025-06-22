from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

def build_agent(model_name: str):
    """
    지정한 모델에 대한 LlmAgent 인스턴스를 생성하고 설정합니다.

    이 함수는 전달받은 model_name에 따라 OpenAI GPT-4o 또는 Anthropic Claude Haiku를 사용하여
    LlmAgent를 초기화합니다. 각 모델에 맞는 모델명, 에이전트 이름, instruction을 설정합니다.

    인자:
        model_name (str): 사용할 모델 이름 ("gpt"는 OpenAI GPT-4o, "claude"는 Anthropic Claude Haiku)

    반환값:
        LlmAgent: 지정한 모델에 맞게 설정된 LlmAgent 인스턴스
    """

    if model_name =="gpt": 
        # OpenAI의 GPT-4o (OPENAI_API_KEY 필요) ---
        agent_openai = LlmAgent(
            model=LiteLlm(model="openai/gpt-4o"), # LiteLLM 모델 문자열 포맷
            name="openai_agent",
            instruction="당신은 GPT-4o로 구동되는 유용한 어시스턴트입니다.",
        )
        return agent_openai

    elif model_name =="claude":
        # Anthropic의 Claude Haiku (Vertex 미사용, ANTHROPIC_API_KEY 필요) ---
        agent_claude_direct = LlmAgent(
            model=LiteLlm(model="anthropic/claude-3-haiku-20240307"),
            name="claude_direct_agent",
            instruction="당신은 Claude Haiku로 구동되는 어시스턴트입니다.",
        )
        return agent_claude_direct
    
root_agent = build_agent("gpt") # gpt 또는 claude
