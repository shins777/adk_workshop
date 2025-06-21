# LiteLLM Agent Example (ADK)

## Example Overview
This example demonstrates how to use the ADK framework with external LLM providers via LiteLLM. It supports both OpenAI GPT-4o and Anthropic Claude models.

## Environment Setting
Set the following keys in your `.env` file:

```
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
```

Other keys (e.g., GOOGLE_API_KEY) may be required for additional features.

## How to Run
Run the agent example with:

```bash
uv run python llm.py
```

Edit `llm.py` to select the model (`gpt` or `claude`).

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](../../LICENSE) file for details.
