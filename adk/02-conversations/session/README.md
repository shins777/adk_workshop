# ADK Session Conversation Agent - Session

This folder demonstrates how to build and operate a session-aware conversational AI agent using the ADK (Agent Development Kit) framework. The agent is designed to answer user queries by performing a Google search and maintaining session state across interactions, supporting multiple session backends.

The Session Conversation Agent is designed to:
- Answer user questions using both its own knowledge and real-time Google Search results
- Maintain session state and history across multiple user interactions
- Support in-memory, SQLite database, and Vertex AI session backends
- Print detailed session properties and events after each turn

---

## .env Example

Place your `.env` file in the parent folder (e.g., `adk/02-conversations/`). Example:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-project-id
PROJECT_NUMBER=your-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
AGENT_ENGINE_ID=your-agent-engine-id  # Only needed for vertexai session type
```

## Folder Structure

```
adk/02-conversations/session/
├── __init__.py
├── agent.py
├── main.py
├── runner.py
└── README.md
```

- `agent.py`  
  Defines the agent, including its instruction template and integration with the Google Search tool.
- `runner.py`  
  Provides an asynchronous script to run the agent in a session-aware conversational loop, printing session state and event details after each interaction.
- `main.py`  
  Entry point for running the agent, allowing selection of session backend (in-memory, database, or Vertex AI) and managing session service setup.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Runner Script (`runner.py`)

- Asynchronously runs the agent in a session-aware conversational loop
- Checks for existing sessions and continues or creates new ones as needed
- Prompts the user for input, sends it to the agent, and prints the agent's response
- Prints session properties and events after each turn

---

## Main Script (`main.py`)

- Entry point for running the agent
- Allows selection of session backend via `--type` argument (`in_memory`, `database`, or `vertexai`)
- Sets up the appropriate session service
- Runs the session-aware conversational loop with user-specified app name, user ID, and session ID

```
uv run -m session.main --type <session_type> --app_name <app_name> --user_id <user_id> --session_id <session_id>
```
Usage : session type : in_memory, database, vertexai

### Example Usage

#### 1. type = in_memory

```
uv run -m session.main --type in_memory --app_name Search_Assistant --user_id forusone --session_id session_id_01
```
#### 2. type = database
```
uv run -m session.main --type database --app_name Search_Assistant --user_id forusone --session_id session_id_01
```

But this is the bug now : https://github.com/google/adk-python/issues/885  
It should be resializable, the fix shoul be in next week as of June 1 2025.

```
sqlalchemy.exc.StatementError: (builtins.TypeError) Object of type GroundingMetadata is not JSON serializable
```

#### 3. type = vertexai
To store session in Agent Engine, you have to configure the Agent engine and add the id into .env file first.
```
AGENT_ENGINE_ID = "17699933548393804800"
```

Then, login to GCP to access to the RAG Engine. use the following command.
```
gcloud auth application-default login
```
After login-in, run the followig command. 

```
uv run -m session.main --type vertexai --app_name Search_Assistant --user_id forusone --session_id session_id_01
```
---

## License

This project is licensed under the Apache License 2.0.


