# ADK Conversation Agent - Memory

This example demonstrates how to build and operate a conversational AI agent with memory using the ADK framework and the Vertex AI Agent Engine Memory Bank feature. The example consists of two agents that communicate using information stored from previous sessions via a memory service. A memory-enabled conversational agent stores selected session information into the memory so that another agent can later retrieve those values.

The Memory feature has a different purpose than storing full sessions in a database. Information stored in Memory is a summarized representation of the session rather than a complete session dump. Persisting session data to a database saves the entire session contents, whereas Memory stores condensed summaries intended for retrieval and contextual recall.

## .env configuration

Create a `.env` file in the parent folder (`02-context`). See the ADK quickstart for recommended environment variables and authentication instructions:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

The example below shows environment variables used when running ADK with Vertex AI / Agent Engine in an enterprise environment. Note: the Gemini endpoint location and Agent Engine location can be configured independently.

```
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "YOUR_PROJECT_LOCATION"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"

MEMORY_BANK_ID = "1131366489594658816"
```

For individual users using AI Studio, set the API key like this:

```
GOOGLE_GENAI_USE_VERTEXAI = FALSE
GOOGLE_API_KEY = PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## Example: run the demo

Authenticate your environment with Google Cloud:

```
adk_workshop/adk/02-context$gcloud auth application-default login
```

To test is this example, you have run the agents seperately. you can run step by step the example or you can run this agent with seperated command environment at a time.

### 1. Run a agent to store a session to memory
Run the agent to add a session to memory. 

```
adk_workshop/adk/02-context$ uv run -m memory_bank.runner_store --app_name ai_assist --user_id forus
```
Provide some information such as "I'm Forus, what's your name? " 

### 2. Run a agent to recall a session from memory
You can get the information from memory by using recall agent
```
adk_workshop/adk/02-context$ uv run -m memory_bank.runner_recall --app_name ai_assist --user_id forus
```

Ask your name to Agent like "Do you remember my name? " 

## License

This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).