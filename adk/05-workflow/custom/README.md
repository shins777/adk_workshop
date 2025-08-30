# Custom Workflow CriticAgent Example (ADK)

This folder demonstrates how to build and operate a custom multi-stage critique agent using the Agent Development Kit (ADK). The example shows how to delegate positive, negative, and aggregated review steps to separate sub-agents and coordinate their outputs to complete a full critique workflow.

Contents
- `agent.py`: Defines the root `CriticAgent` that orchestrates the positive, negative, and review sub-agents.
- `critic.py`: Implements the custom `CriticAgent` class that runs each sub-agent sequentially and yields events for each stage.
- `sub_agent.py`: Defines the sub-agents used by the workflow:
  - `positive_critic_agent`: Produces positive feedback.
  - `negative_critic_agent`: Produces constructive negative feedback.
  - `review_critic_agent`: Aggregates critiques and produces a final review.

## .env Configuration

Create a `.env` file in the parent folder (`adk/05-workflow/`) with the environment variables required by the ADK examples.

Refer to the ADK quickstart for the recommended variables and authentication steps:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

Example environment variables for Vertex AI (enterprise):
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # Use Vertex AI for enterprise.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # Replace with your Project ID.
GOOGLE_CLOUD_LOCATION="global"                  # Use the global endpoint.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # Example Gemini model.
```

For individual users using AI Studio, set the API key as follows:
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## How to run the source code
Authenticate to Google Cloud using the following command:
```
adk_workshop/adk/05-workflow $ gcloud auth application-default login
```

Run the parallel sub-agent example using the ADK CLI (from the repository root):
```
adk_workshop/adk/05-workflow $ adk web
```

Check the module-level README files and source code to explore how each sub-agent works and to adapt the workflow for your use case.

## License
This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).