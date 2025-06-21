
# ADK Runtime Agent Example - Understanding ADK Runtime.

This folder demonstrates how to build and operate an advanced AI agent using the ADK (Agent Development Kit) framework, featuring sub-agents and agent tools for critique tasks.

## Background

### Event Loop in ADK Runtime
The following image explain the most important concept, that is event loop in ADK runtime. this even loop mechanism is similar with python async event loop. 
![event loop](https://google.github.io/adk-docs/assets/event-loop.png)
Image source : https://google.github.io/adk-docs/runtime/#core-idea-the-event-loop

### Invocation Flow

![invocation flow](https://google.github.io/adk-docs/assets/invocation-flow.png)
Image source : https://google.github.io/adk-docs/runtime/#how-it-works-a-simplified-invocation

## Overview
The `runtime` agent example shows how to:
- Define a root agent with sub-agents for positive and negative critique
- Optionally use agent tools to wrap sub-agents
- Load environment variables for configuration
- Instantiate and return an ADK `Agent` object
- Run the agent in a conversational loop using a runner script

## .env Sample

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklK--------WYZVM2uZh6Bd8 <-- you should use your key.

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "9215---43942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
```

## File Structure
```
adk/01-agent/runtime/
├── __init__.py
├── agent.py
├── runner.py
├── sub_agent.py
└── README.md
```

- `agent.py`  
  Contains the code to build and configure the root agent, including sub-agents and agent tool integration.
- `runner.py`  
  Provides a script to run the agent in a conversational loop, handling user input and agent responses.
- `sub_agent.py`  
  Defines the positive and negative critique sub-agents.
- `__init__.py`  
  Marks the folder as a Python package.

## How It Works

The root agent is defined using the ADK `Agent` class. It can be configured in two modes:
- **Sub-agent mode:** The agent delegates critique tasks to `positive_critic` and `negative_critic` sub-agents.
- **Agent tool mode:** The agent uses `AgentTool` wrappers to expose sub-agents as callable tools.

The agent's instruction guides it to:
- Organize the intent of the user's question
- Use the appropriate sub-agent/tool for positive or negative critique
- Always answer in the same language as the user's question

## Example Usage
```
ai_agent/adk/01-agent$ uv run -m runtime.runner
```

## License

This project is licensed under the Apache License 2.0.