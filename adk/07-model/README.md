# Model Integration Examples (ADK)

## Example Overview
This folder demonstrates how to integrate external LLM providers with the ADK framework. It includes examples for LiteLLM (OpenAI, Anthropic) and Ollama-based models.

- `litellm/`: Shows how to use OpenAI GPT-4o and Anthropic Claude with ADK agents via LiteLLM.
- `ollama_agent/`: Shows how to use local Ollama models (Llama 3, Gemma) with ADK agents.

## Environment Setting
Copy `.env` to your working directory and set the following keys as needed:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=...
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
PROJECT_ID=...
PROJECT_NUM=...
LOCATION=...
MODEL=...
OLLAMA_API_BASE=...
```

Refer to each subfolder for specific requirements.

## How to Run
- See each subfolder (`litellm/`, `ollama_agent/`) for agent code and instructions.
- Example (for `litellm`):
  ```bash
  uv run python litellm/llm.py
  ```
- Example (for `ollama_agent`):
  ```bash
  uv run python ollama_agent/agent.py
  ```

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](../LICENSE) file for details.
