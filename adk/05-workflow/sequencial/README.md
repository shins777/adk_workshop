# ADK Sequential Workflow Agent Example

## 1. Example Overview
This folder contains a sequential workflow agent example built with the Agent Development Kit (ADK). The agent processes user input through multiple stages or sub-agents in a defined order. This example is suitable for scenarios that require ordered processing, step-by-step data handling, or staged reasoning where tasks must be executed sequentially.

## .env Configuration

Create a `.env` file in the parent directory (`adk/05-workflow/`) containing the environment variables required by ADK.

Refer to the ADK quickstart for details on variables and authentication:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

The following example variables show settings typically used when running ADK with Vertex AI in an enterprise environment:
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

## License
This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).