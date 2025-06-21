# ADK Deployment Examples

## 1. Example Overview
This directory contains advanced examples for deploying, managing, and running multi-agent pipelines using the Agent Development Kit (ADK) and Vertex AI Agent Engine. Each subfolder demonstrates a different deployment and session management scenario, with scripts for local and remote execution, GCP integration, and agent engine management.

- **agent_engine/**: Shows how to build, deploy, and run a multi-agent pipeline using a SequentialAgent and Vertex AI Agent Engine.
- **agent_session/**: Demonstrates session management, deployment, updating, and running of agents with conversational continuity.

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
4. Refer to the subfolder README.md files for specific deployment, update, and run instructions for each scenario.

## 4. License Information
This project is licensed under the Apache License 2.0.
