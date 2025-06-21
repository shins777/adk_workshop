# A2A Protocol & ADK Integration Examples

This directory contains reference implementations and minimal working examples for the A2A (Agent-to-Agent) protocol and its integration with the Google Agent Development Kit (ADK). Each subfolder demonstrates a different aspect of agent communication, protocol compliance, and ADK-powered agent deployment.

---

## Subfolders & Summaries

### [`adk/`](adk/README.md)
- **Purpose:** ADK-powered A2A agent examples, including a minimal Google Search agent and utilities for A2A/GenAI message conversion.
- **Key Example:**
  - [`simple/`](adk/simple/README.md):
    - Minimal ADK agent exposed via A2A protocol
    - Google Search tool integration
    - Conversion utilities for A2A/GenAI message formats
    - Both server and client implementations
    - See [adk/simple/README.md](adk/simple/README.md) for details and usage

---

### [`concept/`](concept/README.md)
- **Purpose:** Basic A2A protocol demonstration with a simple echo agent, A2A-compliant server, and Python client.
- **Key Example:**
  - [`basic/`](concept/basic/README.md):
    - Echo agent that returns user input in uppercase
    - A2A-compliant server and client
    - Demonstrates agent card, skill registration, and streaming/non-streaming APIs
    - See [concept/basic/README.md](concept/basic/README.md) for details and usage

---

## Getting Started

- See the `README.md` in each subfolder for setup, environment, and usage instructions.
- Most examples require Python 3.13+ and the `uv` package manager.
- For ADK-powered agents, ensure you have a `.env` file with model and API credentials in the parent directory.

---

## Example: Change Python Version with uv

```bash
uv venv --python 3.13
```

```
/ai_agent/a2a$ source .venv/bin/activate
(a2a) /ai_agent/a2a$ 
```


---

## License

This project is licensed under the Apache License 2.0.
