# ADK A2A Concept Examples

## Example Overview
This folder demonstrates basic agent-to-agent (A2A) concepts using the ADK framework. It includes simple agent, client, and server implementations to illustrate A2A communication patterns.

- `basic/`: Contains minimal working examples for A2A agent, client, and server.

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
Run the agent, client, or server examples as described in the `basic/` subfolder's README.md. Example:

```bash
uv run python basic/agent.py
uv run python basic/client.py
uv run python basic/server.py
```

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../LICENSE) file for details.

1. change python version of uv.

    ```
    uv venv --python 3.13
    ```
