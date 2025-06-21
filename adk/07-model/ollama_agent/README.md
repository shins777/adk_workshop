# Ollama Agent Example (ADK)

## Example Overview
This example demonstrates how to use the ADK framework with local Ollama models (Llama 3, Gemma) as LLM agents.

## Environment Setting
Set the following keys in your `.env` file:

```
OLLAMA_API_BASE=http://localhost:11434
```

Other keys (e.g., GOOGLE_API_KEY) may be required for additional features.

## How to Run
Run the agent example with:

```bash
uv run python agent.py
```

Edit `agent.py` to select the model (`gemma` or `llama`).

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](../../LICENSE) file for details.
