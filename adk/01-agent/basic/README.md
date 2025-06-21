
# ADK Basic Agent Example - Basic concept of ADK

This folder demonstrates how to build and operate a simple AI agent using the ADK (Agent Development Kit) framework.

## Background

### Agent types
We can use there three types of agents for the purpose of business scenarios in various ways of composition of multi-agents and tools.
![agent types](https://google.github.io/adk-docs/assets/agent-types.png)
Image source : https://google.github.io/adk-docs/agents/#agents

### Agent Comparison
Here are comparison of three types of agents. 
![agent types](https://github.com/ForusOne/adk_agent/blob/main/images/agent_comparison.png?raw=true)
Image source : https://google.github.io/adk-docs/agents/#choosing-the-right-agent-type

## Overview
The `basic` agent is a minimal example that shows how to:
- Define an agent with a custom instruction and description
- Load environment variables for configuration
- Instantiate and return an ADK `Agent` object
- Run the agent to answer user queries in a structured format 

## .env Example

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklKWYZVM2uZh6Bd8 

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "921543942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
```

## File Structure
```
adk/01-agent/basic/
├── __init__.py
├── agent.py
└── README.md
```

- `agent.py`  
  Contains the code to build and configure the basic agent.
- `__init__.py`  
  Marks the folder as a Python package.

---

## Example Usage
Note : Execute the following command on **01-agent** folder. 

```
ai_agent/adk/01-agent$ adk web
```

## License

This project is licensed under the Apache License 2.0.