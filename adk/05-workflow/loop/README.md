# ADK Loop Workflow Agent Example

This folder provides a loop-based workflow agent example using the Agent Development Kit (ADK). The agent processes user input in repeated iterations and is suitable for scenarios requiring iterative improvement, multi-turn questioning, or multi-step tasks. It is useful when a workflow must interact with the user or perform repeated steps until a stopping condition is met.

## .env Configuration

Create a `.env` file in the parent directory (`adk/05-workflow/`) containing the environment variables required by ADK.

Refer to the ADK quickstart for details on variables and authentication:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

The following example variables assume usage with Vertex AI in an enterprise environment:
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
gcloud auth application-default login
```

Run the loop workflow sub-agent example with the ADK CLI (from the repository root):
```
cd adk_workshop/adk/05-workflow
adk web
```

## License
This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).