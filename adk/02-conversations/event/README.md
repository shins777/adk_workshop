# ADK Event Conversation Agent - Event

This folder demonstrates how to build and operate an event-driven conversational AI agent using the ADK (Agent Development Kit) framework. The agent is designed to answer user queries by performing a Google search and providing structured responses, while the runner script showcases detailed event streaming and introspection.

## .env Example

Place your `.env` file in the parent folder (e.g., `adk/02-conversations/`). Example:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-project-id
PROJECT_NUMBER=your-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
```

---

## Folder Structure

```
adk/02-conversations/event/
├── __init__.py
├── agent.py
├── runner.py
└── README.md
```

- `agent.py`  
  Defines the agent, including its instruction template and integration with the Google Search tool.
- `runner.py`  
  Provides an asynchronous script to run the agent, stream events, and print detailed event information for each step of the conversation.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Example Usage
Note : Execute the following command on **01-conversations** folder. 

```
ai_agent/adk/02-conversations$ uv run -m event.runner
```

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../../LICENSE) file for details.