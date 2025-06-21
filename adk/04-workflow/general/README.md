# ADK General Workflow Agent Example

## 1. Example Overview
This folder demonstrates a general workflow agent using the Agent Development Kit (ADK). The agent is designed to process user input through a configurable workflow, which can be extended or customized for various business scenarios. This example is ideal for understanding how to structure multi-step or multi-agent workflows in ADK.

## 2. Environment Setting
Create a `.env` file in the parent folder (`adk/04-workflow/`) with the following content (adjust values as needed):

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
2. Navigate to the `adk/04-workflow/` directory in your terminal.
3. Run the agent using the ADK runner or a provided script. For example:
   ```bash
   adk web
   ```
   or, if a runner script is provided:
   ```bash
   uv run -m general.runner
   ```
4. Interact with the agent via the web interface or terminal prompt.

## 4. License Information
This project is licensed under the Apache License 2.0.
