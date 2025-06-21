# ADK A2A Simple Examples

## Example Overview
This folder contains simple agent, client, and server examples using the ADK framework for agent-to-agent (A2A) communication. It demonstrates how to set up and run basic A2A workflows.

- `agent.py`: Example agent implementation.
- `client.py`: Example client implementation.
- `server.py`: Example server implementation.
- `convert.py`, `executor.py`: Utility modules for agent operation.

## Environment Setting
Set the following keys in your `.env` file (if required by your agent or client code):

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## How to Run the Source Code
Run the agent, client, or server examples with:

```bash
uv run python agent.py
uv run python client.py
uv run python server.py
```

Refer to the README.md in each subfolder for more details.

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../LICENSE) file for details.
