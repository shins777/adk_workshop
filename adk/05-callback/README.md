# ADK Callback Agent Examples

This directory contains examples of using callback mechanisms in the Agent Development Kit (ADK) to control agent, model, and tool behavior. Each subfolder demonstrates a different callback scenario, allowing you to intercept, modify, or block execution at various stages of the agent workflow.

---

## 1. Example Overview

- **agent_callback/**: Demonstrates agent-level callbacks for pre- and post-processing around the main agent logic. Allows for advanced control, custom responses, and state-driven conversational flows.
- **model_callback/**: Demonstrates model-level (LLM) callbacks for pre- and post-processing around the LLM call. Enables keyword filtering, content moderation, and custom flows.
- **tool_callback/**: Demonstrates tool-level callbacks for pre- and post-processing around tool execution. Allows for argument/result manipulation and custom tool flows.

Each example shows how to intercept and modify the flow before and after the main agent/model/tool logic runs, providing advanced control and customization.

---

## 2. Environment Setting
Create a `.env` file in the parent folder (`adk/05-callback/`) with the following content (adjust values as needed):

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-project-id
PROJECT_NUMBER=your-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
```

---

## 3. How to Run the Source Code
1. Install dependencies as specified in the `pyproject.toml` or `requirements.txt`.
2. Navigate to the `adk/05-callback/` directory in your terminal.
3. Run the agent using the ADK runner or a provided script. For example:
   ```bash
   adk web
   ```
   or, for a specific callback example:
   ```bash
   uv run -m agent_callback.runner
   uv run -m model_callback.runner
   uv run -m tool_callback.runner
   ```
4. Interact with the agent via the web interface or terminal prompt.

---

## 4. License Information
This project is licensed under the Apache License 2.0.
