# ADK Conversation Agent - Event

This folder demonstrates how to build and operate an event-driven conversational AI agent using the Agent Development Kit (ADK). Events are a central concept for communication between users and agents in ADK. This example shows how to inspect various properties inside individual events. The agent answers user queries using Google Search by default, and the runner script demonstrates detailed event streaming and the agent's internal behavior at each stage.

This example parses and inspects a variety of fields contained in actual events. In a real project, you can use the information carried by events to control workflow, trigger actions, or present results.

## .env Configuration

Place the `.env` file in the parent folder (`02-context`). See the ADK quickstart for recommended environment variables and authentication steps:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

The following environment settings are an example for using ADK with Vertex AI in an enterprise environment:

```
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "YOUR_PROJECT_LOCATION"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"
```

For individual users using AI Studio, set the API key as follows:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## Running the Example

Authenticate your environment with Google Cloud:

```
adk_workshop/adk/02-context$ gcloud auth application-default login
```

From the `02-context` folder, run the runner script:

```
adk_workshop/adk/02-context$ uv run -m event.runner
```

The Runner class demonstrates a programmatic way to control and inspect events at the code level.

To view event details via the web UI, you can also run:

```
adk_workshop/adk/02-context$ adk web
```

## License

This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).