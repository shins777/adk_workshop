# ADK Conversation Agent - State

## Example Overview
This folder demonstrates how to build a state-based conversational agent using the Agent Development Kit (ADK). It shows how to modify and utilize session state to enable advanced context handling and flow control. The example illustrates how session state can be changed and leveraged within a session.

## .env Configuration

Place the `.env` file in the parent folder (`02-context`). See the ADK quickstart for the environment variables and authentication steps:
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

## How to run the source code

Authenticate your environment with Google Cloud:

```bash
adk_workshop/adk/02-context$ gcloud auth application-default login
```

`output_key` is a reserved keyword used in the session to store a simple, easily-accessible indicator of the last turn's output. In a multi-turn environment, it holds information about the final output from the most recent turn.

Session state is typically changed by appending events that include a state delta. For example:

```python
await session_service.append_event(session, system_event)
```

Run the example with:

```bash
adk_workshop/adk/02-context$ uv run -m state.runner --app_name ai_assist --user_id forus
```

## License

This project is licensed under the Apache License 2.0. All code and content copyright