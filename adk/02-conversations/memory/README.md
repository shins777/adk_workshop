# ADK Memory Conversation Agent - Memory

This folder demonstrates how to build and operate a conversational AI agent with memory capabilities using the ADK (Agent Development Kit) framework. The agent can answer user queries by performing a Google search and can also recall information from previous sessions using a memory service.

The Memory Conversation Agent is designed to:
- Answer user questions using both real-time Google Search and memory recall
- Store completed sessions in memory for later retrieval
- Support both in-memory and Vertex AI RAG corpus memory backends
- Demonstrate a multi-step workflow: search, store, recall

## .env Example

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklK--------WYZVM2uZh6Bd8 <-- you should use your key.

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "9215---43942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"

# For memory store in RAG Engine
CORPUS_ID = "55253532324830177280" <-- you should use your RAG Engine corpus ID.

```

## Folder Structure

```
adk/02-conversations/memory/
├── __init__.py
├── agent.py
├── main.py
├── runner.py
└── README.md
```

- `agent.py`  
  Defines two agents:
  - `search_agent`: Answers questions using Google Search.
  - `recall_agent`: Answers questions by retrieving information from memory.
- `runner.py`  
  Provides asynchronous functions to orchestrate a workflow where the search agent is run first, its session is stored in memory, and then the recall agent retrieves information from memory in a new session.
- `main.py`  
  Entry point for running the workflow. Allows selection of memory type (in-memory or Vertex AI RAG corpus) and manages session/memory service setup.
- `__init__.py`  
  Marks the folder as a Python package.

## Agent Details (`agent.py`)

- **`search_agent`**
  - Uses the `google_search` tool
  - Follows a structured response format (question, source information, answer)
- **`recall_agent`**
  - Uses the `load_memory` tool to retrieve information from memory
  - Answers based on previously stored sessions

---

## Runner Script (`runner.py`)

- Orchestrates the workflow:
  1. Runs the search agent in a dedicated session and stores the session in memory
  2. Runs the recall agent in a new session to retrieve information from memory
- Handles user input for both search and recall steps
- Prints agent responses and event details

---

## Main Script (`main.py`)

- Entry point for running the workflow
- Allows selection of memory type via `--memory_type` argument (`in_memory` or `rag_corpus`)
- Sets up session and memory services
- Runs the orchestrated workflow with user-specified app name and user ID

### Example Usage

#### 1. Command line.
```
uv run memory.main --memory_type [in_memory|rag_corpus] --app_name <app_name> --user_id <user_id>")
```

####  2. Use memory_type = `in_memory`
```
uv run -m memory.main --memory_type in_memory --app_name search_assistant --user_id forusone
```

####  3. Use memory_type = `rag_corpus`

First, you have to set up the RAG Engine in Vertex AI.
```
CORPUS_ID = "552535334330177280"
```
Then, login to GCP to access to the RAG Engine. use the following command.
```
gcloud auth application-default login
```
After login-in, run the followig command. 
```
uv run -m memory.main --memory_type rag_corpus --app_name search_assistant --user_id forusone
```
if you don't have an access to the RAG engine. you could see the following error message.
```
RuntimeError: ('Failed in indexing the RagFile due to: ', {'code': 403, 'message': "Permission 'aiplatform.ragFiles.upload' denied on resource '//aiplatform.googleapis.com/projects/ai-forus/locations/us-central1/ragCorpora/552535232177280' (or it may not exist)."
```

---

