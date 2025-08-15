# Sub-Agent Tool Example (ADK)
In ADK, you can use a sub agent as a tool. There are key differences between using an Agent as a tool and as a sub-agent:
 * Using an Agent as a tool: The calling Agent has control over all outputs, just like using any other Tool.
   * In this case, all registered Tools can be invoked.
 * Using an Agent as a Sub Agent: The calling Agent delegates output control to the called sub-agent.
   * In this case, only one specific Sub Agent is invoked.

## Example Overview
This folder demonstrates how to implement modular and composable workflows by utilizing sub-agents as tools within an ADK agent.

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

## License

This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).