
# ADK Runtime Agent Example - Understanding ADK Runtime

This folder demonstrates how to build and operate advanced AI agents using sub-agents and agent tools with the ADK (Agent Development Kit) framework.
This example explains how to use the Runner class. This approach is not executed via the adk web interface, but rather through API calls, as would be done from the presentation layer in a real project. In production environments, you would use Runner from a customized UI to invoke the agent.

## Background

### Event Loop in ADK Runtime
The image below explains the most important concept in ADK Runtime: the event loop. This event loop mechanism is similar to Python's asynchronous event loop.
![event loop](https://google.github.io/adk-docs/assets/event-loop.png)
Image source: https://google.github.io/adk-docs/runtime/#core-idea-the-event-loop

### Invocation Flow
You can see more detailed operation process by referencing the following url.   
* https://google.github.io/adk-docs/runtime/#how-it-works-a-simplified-invocation

## Overview
The `runtime` agent example demonstrates:
- Defining a root agent that includes sub-agents for positive and negative critique
- Optionally wrapping sub-agents with agent tools
- Loading configuration values from environment variables
- Executing using the Runner class


## .env Setup

The `.env` file should be located in the parent folder (`01-agent`). For details on what to include in the environment file, refer to the following URL:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

Below is an example configuration for using ADK with Vertex AI in an enterprise environment:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # Use Vertex AI for enterprise.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # Change to your own Project ID.
GOOGLE_CLOUD_LOCATION="global"                  # Use Global Endpoint.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # Latest Gemini version.
```

For general users using AI Studio, set the GOOGLE_API_KEY as follows:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
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

- `agent.py`: Contains build and setup code for the root agent, including sub-agent and agent tool integration.
- `runner.py`: Provides a script for running a conversation loop to handle user input and agent responses.
- `sub_agent.py`: Defines positive and negative critic sub-agents.
- `__init__.py`: Marks the folder as a Python package.


## How It Works

The root agent is defined using the ADK `Agent` class, and includes sub-agents as shown below.
The sub-agents are invoked by the root agent based on the analysis of the user's question, calling the appropriate sub-agent for the query.

```
    agent = Agent(
        name = "root_agent",
        model = os.getenv("MODEL"),
        description = "Agent that answers user queries",
        instruction = INSTRUCTION,
        sub_agents = [positive_critic, negative_critic],
    ) 
```

## Running the Example
### 1. Run using google.adk.runners.Runner class

Set up Google Cloud authentication using the following gcloud command:

```
gcloud auth application-default login
```

You can run the runner class using `uv run` command as follows.
```
adk_workshop/adk/01-agent$ uv run -m runtime.runner
```

Or run via web browser:
```
ai_agent/adk/01-agent$ adk web
```


## License

This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).