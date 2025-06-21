# Agent Tool Integration Example (ADK)

## Example Overview
This folder demonstrates how to integrate agent-to-agent tools within ADK agents. It shows how one agent can call another as a tool, enabling modular and composable agent workflows.

- `sub_agent_tool/`: Contains examples of sub-agents used as tools.

## Environment Setting
Set the following keys in your `.env` file (located in the parent folder):

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## How to Run the Source Code
Run the agent example with:

```bash
uv run python agent_tool/agent.py
```

Refer to the `sub_agent_tool/` folder for additional sub-agent tool examples.

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../LICENSE) file for details.
