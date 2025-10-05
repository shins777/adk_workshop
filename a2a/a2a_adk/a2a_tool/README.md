# a2a_tool

## Overview

The `a2a_tool` module provides tools and utilities for building and extending agent-to-agent (A2A) interactions within the ADK (Agent Development Kit) framework. It includes reusable components, remote agent templates, and function modules that can be integrated into A2A agent systems.

### Tool Structure

- **Remote Agents**: Contains templates and implementations for remote agents, such as the stock price agent, which can be run as independent services and communicate with other agents.
- **Functions**: Provides modular functions (e.g., for retrieving stock prices) that can be invoked by agents or sub-agents.
- **Sub-Agents**: Defines sub-agents that encapsulate specific skills or tasks, allowing for flexible and scalable agent design.

- The `remote_agents/stock_price/agent_stock_price` directory includes a remote agent capable of fetching and returning stock prices.
- Functions are defined in `functions.py`, and sub-agents are implemented in `sub_agents.py` for modular handling of stock-related queries.

## File Structure

```
a2a_tool/
├── remote_agents/
│   └── stock_price/
│       └── agent_stock_price/
│           ├── functions.py   # Stock price functions
│           └── sub_agents.py  # Sub-agent definitions
└── ...
```

## Configuration
Create a .env file in a2a_tool folder. 

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="ai-hangsik"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"
```

## Run example

To run a remote agent, use the following command:

```
(a2a) /adk_workshop/a2a/adk$ adk api_server --a2a --port 8001 a2a_tool/remote_agents/exchange_rate
```

To run a client and interact with the remote agent:

```
(a2a) /adk_workshop/a2a/adk$ adk web a2a_tool
```

Example question to ask the agent:

```
What is the latest exchange rate between USD and KRW?
```

## License
This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).