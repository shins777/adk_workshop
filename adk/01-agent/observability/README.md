# ADK Basic Agent - ADK Observability Setup

This folder provides an example of how to use AgentOps for observability in AI Agents built with the ADK (Agent Development Kit) framework.
To run this code, you must sign up at the AgentOps site and obtain a token:
* https://app.agentops.ai/

Once you receive your API_KEY, set it in the .env file as shown below.

## .env Setup

The `.env` file should be located in the parent folder (`01-agent`). For details on what to include in the environment file, refer to the following URL:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

Below is an example configuration for using ADK with Vertex AI in an enterprise environment:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # Use Vertex AI for enterprise.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # Change to your own Project ID.
GOOGLE_CLOUD_LOCATION="global"                  # Use Global Endpoint.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # Latest Gemini version.

AGENTOPS_API_KEY="0000000-0000-0000-0000-000000" # AgentOps key
```

For general users using AI Studio, set the GOOGLE_API_KEY as follows:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## Basic Agent File Structure
```
adk/01-agent/basic/
├── __init__.py
├── agent.py
└── README.md
```

- `agent.py`: Contains build and setup code for the basic agent.
- `__init__.py`: Marks the folder as a Python package.

## Running the Example

Set up Google Cloud authentication using the following gcloud command:

```
gcloud auth application-default login
```

From the `01-agent` folder, run the command below and test in the adk web interface:

```
adk_workshop/adk/01-agent$ adk web
```

## License
This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).