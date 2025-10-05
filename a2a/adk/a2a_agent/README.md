# a2a_agent

## Overview

The `a2a_agent` module provides the core logic for agent-to-agent (A2A) communication and orchestration within the ADK (Agent Development Kit) framework. It enables the creation, registration, and management of agents that can interact with each other and external services.

### Agent Structure

- **Agent Client**: The main entry point for agent logic. Handles agent lifecycle, message processing, and communication.
- **Remote Agents**: Specialized agents (e.g., stock price agent) that implement domain-specific logic and functions.
- **Sub-Agents**: Modular components that encapsulate specific tasks or skills, which can be invoked by the main agent.

- The `remote_agents/stock_price/agent_stock_price` directory contains an agent that can fetch and return stock prices.
- It exposes functions (in `functions.py`) and sub-agents (in `sub_agents.py`) for modular handling of stock-related queries.

## File Structure

```
a2a_agent/
├── agent_client/
│   └── agent.py         # Core agent client logic
├── remote_agents/
│   └── stock_price/
│       └── agent_stock_price/
│           ├── functions.py   # Stock price functions
│           └── sub_agents.py  # Sub-agent definitions
└── ...
```

## Configuration
Create a .env file in a2a_agent folder. 

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="ai-hangsik"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"

# Stock API keys
STOCK_API_KEY = <get the key from https://www.alphavantage.co/ >
```

## Run example

Run a remote agent with the following port. 

```
(a2a) /adk_workshop/a2a/adk$ adk api_server --a2a --port 8001  a2a_tool/remote_agents/stock_price
```

Run a client to get the response from the remote agent. 
```
(a2a) /adk_workshop/a2a/adk$ adk web a2a_tool
```

type the following quesiton

```
What is the latest stock price of Google?
```

## License
This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).