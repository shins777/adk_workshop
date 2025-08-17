# ADK General Workflow Agent Example

## 1. Example Overview
This folder contains a general workflow agent example built with the Agent Development Kit (ADK). The agent demonstrates a configurable workflow for processing user input and can be extended or customized for various business scenarios. This example is useful for understanding how to structure multi-step or multi-agent workflows in ADK.

## 2. Environment Setup
Create a `.env` file in the parent directory (`adk/05-workflow/`) with the environment variables required by ADK.

Refer to the ADK quickstart for details on the variables to include:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

The following example variables apply when using ADK with Vertex AI in an enterprise environment:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # Use Vertex AI for enterprise.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # Replace with your Project ID.
GOOGLE_CLOUD_LOCATION="global"                  # Use the global endpoint.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # Example Gemini model.
```

For individual users using AI Studio, set the API key as shown below:
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## How to run the source code
Authenticate to Google Cloud using the following command:
```
gcloud auth application-default login
```

Run the workflow sub-agent example with the ADK CLI (from the repository root):
```
adk_workshop/adk/05-workflow $ adk web
```

## License
This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).