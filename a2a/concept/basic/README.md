# ADK A2A Basic Example

## Example Overview
This folder contains basic agent, client, and server examples for agent-to-agent (A2A) communication using the ADK framework. It demonstrates how to implement a minimal A2A workflow.

- `agent.py`: Basic agent implementation example
- `client.py`: Basic client implementation example
- `server.py`: Basic server implementation example
- `executor.py`: Utility module for agent operation

## Environment Setup
If needed in your agent or client code, set the following keys in a `.env` file:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## How to Run

You can run the agent, client, and server examples as follows:

### 1. Start the A2A server

```
ai_agent/a2a/concept$ uv run -m basic.server
```

### 2. Run the client

```
ai_agent/a2a/concept$ uv run -m basic.client
```

## License
This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).