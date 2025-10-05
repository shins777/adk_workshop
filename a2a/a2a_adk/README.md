# a2a_adk (Agent-to-Agent Agent Development Kit)

This directory contains modules and tools for building agent-to-agent (A2A) systems using the ADK framework. Each subfolder demonstrates a specific aspect of A2A agent development, including agent logic, reusable tools, and remote agent implementations.

## Directory Overview

### a2a_agent

Core logic for agent-to-agent (A2A) communication and orchestration.

- Provides agent client logic, remote agent implementations (such as a stock price agent), and sub-agent modules.
- Supports creation, registration, and management of agents that interact with each other and external services.
- Includes configuration examples and instructions for running remote agents and clients.

See [a2a_agent/README.md](a2a_agent/README.md) for architecture, configuration, and usage details.

### a2a_tool

Reusable tools, remote agent templates, and function modules for A2A agent systems.

- Includes remote agents (e.g., stock price), modular functions, and sub-agent definitions.
- Designed for easy integration and extension of A2A workflows.
- Provides example commands for running remote agents and interacting with them as a client.

See [a2a_tool/README.md](a2a_tool/README.md) for tool structure, configuration, and example usage.

## Getting Started

1. Choose a subfolder that matches your use case or learning goal.
2. Review the README file in that subfolder for setup, configuration, and running instructions.
3. Set up environment variables as described (typically via a `.env` file).
4. Run the example using the recommended commands.

## License

This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).