# Custom Workflow CriticAgent Example (ADK)

## Example Overview
This folder demonstrates how to build and operate a custom multi-stage critique agent using the Agent Development Kit (ADK). The agent orchestrates a workflow of positive and negative critiques by delegating to specialized sub-agents and coordinating their outputs.

- `agent.py`: Defines the root `CriticAgent`, which coordinates the workflow using sub-agents for positive and negative critiques.
- `critic.py`: Implements the `CriticAgent` class, a custom agent that runs a multi-step critique workflow, yielding events from each sub-agent.
- `sub_agent.py`: Defines the sub-agents:
    - `positive_critic_agent`: Generates positive reviews.
    - `negative_critic_agent`: Generates negative reviews.

## Environment Setting
Set the following keys in your `.env` file (located in the parent folder):

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## How to Run the Source Code
Run the agent example with:

```bash
adk web
```

You can customize the workflow logic in `critic.py` and the sub-agent behaviors in `sub_agent.py`.

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../LICENSE) file for details.
