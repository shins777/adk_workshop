# ADK Agent Engine Deployment Example

## 1. Example Overview
This folder demonstrates how to build, manage, deploy, and run a multi-agent pipeline using the Agent Development Kit (ADK) and Vertex AI Agent Engine. It provides scripts and utilities for local testing, deployment to Vertex AI, and remote execution. The example shows how to use a SequentialAgent to orchestrate multiple sub-agents (positive, negative, and review critics) and how to deploy and manage the agent on Google Cloud Vertex AI.

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
1. GCP Login 
```
gcloud auth application-default login
```
2. Authenticate with GCP:
   ```bash
   gcloud auth application-default login
   ```
3. Navigate to the `adk/06-deploy/` directory in your terminal.
4. Run the agent locally or deploy to Vertex AI:
   - Local test & deployment:
     ```bash
     uv run -m agent_engine.deploy --query 'What is Generative AI?' --agent_name my_agent --user_id user1 --session_id 12345

     ```
   - Run deployed agent remotely:
     ```bash
     uv run -m agent_engine.run --resource_name <resource_name> --user_id user1 --session_id 12345 --query 'What is Generative AI?'

     Note : You should set the project number rather than project id in the resource name. 
     ex> uv run -m agent_engine.run --resource_name projects/721521243942/locations/us-central1/reasoningEngines/2417773292921290752 --user_id user1 --session_id 12345 --query 'What is Generative AI?'
     

     ```
5. Interact with the agent via the terminal prompt or remote API.

## 4. License Information
This project is licensed under the Apache License 2.0.
