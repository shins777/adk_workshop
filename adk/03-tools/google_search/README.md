
# Google Search Tool Example (ADK)

This folder demonstrates how to use the built-in Google Search tool with ADK agents to answer user queries with real-time web search results.

## .env Setup

The `.env` file should be located in the parent folder (`03-tools`). For details on what to include in the environment file, refer to the following URL:

https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

Below is an example configuration for using ADK with Vertex AI in an enterprise environment:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # Use Vertex AI for enterprise.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # Change to your own Project ID.
GOOGLE_CLOUD_LOCATION="global"                  # Use Global Endpoint.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # Latest Gemini version.
```

For general users using AI Studio, set the GOOGLE_API_KEY as follows:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## How to Run the Source Code
Set up Google Cloud authentication using the following gcloud command:
```
gcloud auth application-default login
```

Run the sub-agent tool example with the following command:
```
adk_workshop/adk/03-tools$ adk web
```

In the UI, select function_call and run the following command:
```
What are the social issues in Korea this week?
```

## License

This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).