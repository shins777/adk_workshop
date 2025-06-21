# ADK Agent Session Deployment Example

## 1. Example Overview
This folder demonstrates how to build, manage, deploy, update, and run a multi-agent pipeline with session management using the Agent Development Kit (ADK) and Vertex AI Agent Engine. It provides scripts and utilities for local and remote execution, session handling, and agent engine management. The example shows how to use a SequentialAgent with sub-agents and how to manage sessions for conversational continuity.

## 2. Environment Setting
Create a `.env` file in the parent folder (`adk/06-deploy/`) with the following content (adjust values as needed):

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-gcp-project-id
PROJECT_NUMBER=your-gcp-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
STAGING_BUCKET=gs://your-bucket-name
```

## 3. How to Run the Source Code
1. Install dependencies as specified in the `pyproject.toml` or `requirements.txt`.
2. Authenticate with GCP:
   ```bash
   gcloud auth application-default login
   ```
3. Navigate to the `adk/06-deploy/` directory in your terminal.
4. Deploy, update, or run the agent with session management:
   - Deploy agent engine:
     ```bash
     uv run -m agent_session.engine --agent_name my_agent
     ```
   - Update deployed agent engine:
     ```bash
     uv run -m agent_session.update --agent_engine_id <agent_engine_id>
     ```
   - Run agent with session:
     ```bash
     uv run -m agent_session.session --agent_engine_id <agent_engine_id> --user_id user1 --session_id 12345
     ```
5. Interact with the agent via the terminal prompt or remote API.

## 4. License Information
This project is licensed under the Apache License 2.0.
