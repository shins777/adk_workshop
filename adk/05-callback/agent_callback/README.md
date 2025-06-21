# ADK Agent Callback Example

## 1. Example Overview
This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent with pre- and post-processing callbacks at the agent level. The agent can intercept and modify the flow before and after the main agent logic runs, allowing for advanced control, custom responses, and state-based logic.

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

## 3. How to Run the Source Code
1. Install dependencies as specified in the `pyproject.toml` or `requirements.txt`.
2. Navigate to the `adk/05-callback/` directory in your terminal.
3. Run the agent using the ADK runner or a provided script. For example:
   ```bash
   adk web
   ```
   or, if a runner script is provided:
   ```bash
   uv run -m agent_callback.runner
   ```
4. Interact with the agent via the web interface or terminal prompt.

## 4. License Information
This project is licensed under the Apache License 2.0.
