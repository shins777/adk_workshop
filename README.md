# ADK_agent: Multi-Agent, A2A, and AI Agent Development Kit Examples

This repository provides a comprehensive set of examples and reference implementations for building, deploying, and evaluating AI agents using the Agent Development Kit (ADK), A2A (Agent-to-Agent) protocol, and related tools. The project is organized into modular folders, each demonstrating a specific concept, agent type, tool integration, workflow, deployment, or evaluation scenario.

---

## Repository Structure

### a2a/
- **adk/simple/**: Minimal ADK agent exposed via A2A protocol, with Google Search tool integration, conversion utilities, and both server/client implementations.
- **concept/basic/**: Basic A2A protocol example with an echo agent, A2A-compliant server, and Python client.

### adk/
- **01-agent/**: Core agent implementations, including basic, runtime, and search agents. Each subfolder contains agent code, instructions, and runners.
- **02-conversations/**: Conversation management examples (event, memory, session, state), each with agent/session logic and runners.
- **03-tools/**: Tool integration examples, including built-in tools (code execution, search, RAG, VertexAI), function tools, LangChain tools, and MCP tools. Each tool type is organized in its own subfolder.
- **04-workflow/**: Workflow orchestration examples (custom, general, loop, parallel, sequential), each with agent and workflow logic.
- **05-callback/**: Callback mechanism examples (agent, model, tool), showing how to intercept and modify agent/model/tool execution.
- **06-deploy/**: Deployment and session management for agents, including agent engine and session pipelines, GCP/Vertex AI integration, and update scripts.
- **07-model/**: Model integration examples, including LiteLLM and Ollama agent implementations.
- **08-output/**: Output schema enforcement using Pydantic, with agents that return structured responses.
- **09-evaluate/**: Agent evaluation and benchmarking tools.
- **10-unittest/**: Unit test scripts for async and REST-based agent logic.

### mcp/
- **concept/**: Demonstrates parent/child process communication for MCP (Model Context Protocol).

### notebooks/
- **01-adk/**: Jupyter notebooks for ADK tutorials, agent/callback/session/tools/workflow demos.
- **02-agent_engine/**: Notebooks for agent engine management and LangChain/Graph integration.
- **03-rag_engine/**: RAG engine management and demonstration notebooks.
- **04-mcp/**: MCP protocol and agent integration notebooks.
- **05-a2a/**: A2A protocol and ADK integration notebooks.
- **agentspace/**: AgentSpace deployment and integration notebooks.
- **common/**: Common ADK, agent engine, and LangChain reference notebooks.

---

## Getting Started

1. **Install dependencies**: See `pyproject.toml` or `requirements.txt` in each module for required packages.
2. **Set up environment variables**: Many examples require a `.env` file with model, API, and GCP credentials.
3. **Run examples**: Navigate to the desired folder and follow the instructions in the local `README.md` or run the provided scripts/notebooks.

---

## Key Features
- Modular agent and tool design for easy extension
- A2A protocol support for agent-to-agent communication
- Built-in, function, and external tool integration
- Workflow orchestration (sequential, parallel, loop, custom)
- Callback hooks for agent/model/tool execution
- Deployment to Vertex AI Agent Engine and session management
- Output schema enforcement and evaluation utilities
- Jupyter notebooks for interactive exploration and tutorials

---

## License

This project is licensed under the Apache License 2.0.  
  
All code and content is copyrighted by **shins777@gmail.com**.