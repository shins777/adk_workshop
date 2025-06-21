from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

def build_agent(model_name: str):
    """
    Creates and configures an LlmAgent instance for the specified model.

    This function initializes an LlmAgent using either OpenAI's GPT-4o or Anthropic's Claude Haiku,
    depending on the provided model_name. It sets the appropriate model, agent name, and instruction
    for each supported model.

    Args:
        model_name (str): The name of the model to use ("gpt" for OpenAI GPT-4o, "claude" for Anthropic Claude Haiku).

    Returns:
        LlmAgent: A configured LlmAgent instance for the specified model.
    """

    if model_name =="gpt": 
        # OpenAI's GPT-4o (Requires OPENAI_API_KEY) ---
        agent_openai = LlmAgent(
            model=LiteLlm(model="openai/gpt-4o"), # LiteLLM model string format
            name="openai_agent",
            instruction="You are a helpful assistant powered by GPT-4o.",
        )
        return agent_openai

    elif model_name =="claude":
        # Anthropic's Claude Haiku (non-Vertex) (Requires ANTHROPIC_API_KEY) ---
        agent_claude_direct = LlmAgent(
            model=LiteLlm(model="anthropic/claude-3-haiku-20240307"),
            name="claude_direct_agent",
            instruction="You are an assistant powered by Claude Haiku.",
        )
        return agent_claude_direct
    
root_agent = build_agent("gpt") # gpt or claude
