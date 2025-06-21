
# ADK 01-Agent Examples

This directory contains example agent implementations using the Agent Development Kit (ADK). Each sub-folder demonstrates a different approach to building, configuring, and running AI agents, from basic setups to advanced runtime and search-enabled agents.


## ADK component
The following image explain components of ADK.
![adk component](https://github.com/ForusOne/adk_agent/blob/main/images/adk_components.png?raw=true)

## Agent Hierarchy.
ADK is a framework to configure multi-agent system in **a process**.  You can configure multiple sub-agents and tools to implement multi-agent system, But you have to be careful, all this processing is done in a monolithic way, within a single process. 
![Agent Hierarchy](https://github.com/ForusOne/adk_agent/blob/main/images/multi-agent.png?raw=true)

## Subfolders Overview

### 1. `basic/` — Basic Agent Example

A minimal example showing how to define and run a simple ADK agent.

- **Key Features:**
  - Custom instruction and description
  - Loads environment variables for configuration
  - Instantiates and returns an ADK `Agent` object
  - Example `.env` configuration provided
- **How to Run:**
  - Place your `.env` file in the parent folder
  - Run: `adk web` from the `01-agent` directory

See [`basic/README.md`](./basic/README.md) for details.

---

### 2. `runtime/` — Runtime Agent Example

An advanced example featuring a root agent with sub-agents for positive and negative critique, and optional agent tool integration.

- **Key Features:**
  - Root agent with sub-agents
  - Agent tools for critique tasks
  - Conversational loop runner script
  - Example `.env` configuration provided
- **How to Run:**
  - Place your `.env` file in the parent folder
  - Use the provided runner script for interactive sessions

See [`runtime/README.md`](./runtime/README.md) for details.

---

### 3. `search/` — Search Agent Example

An agent that answers user queries by leveraging Google Search, providing up-to-date information with source references.

- **Key Features:**
  - Integrates Google Search tool
  - Formats answers with question, source, and response
  - Example `.env` configuration provided
- **How to Run:**
  - Place your `.env` file in the parent folder
  - Run: `adk web` from the `01-agent` directory

See [`search/README.md`](./search/README.md) for details.

---

## Common Requirements

- Python 3.8+
- `python-dotenv`
- ADK and Google ADK libraries (ensure `google.adk` is installed and configured)
- Google API key and project configuration (see `.env` examples in each subfolder)

---

## Example `.env` File
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE 
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY 

PROJECT_ID=your-project-id 
PROJECT_NUMBER=your-project-number 
LOCATION=us-central1 
MODEL=gemini-2.0-flash
```

## Getting Started

1. Choose a subfolder (`basic`, `runtime`, or `search`) based on your needs.
2. Review the subfolder's README for specific setup and usage instructions.
3. Place your `.env` file in the parent folder as described above.
4. Run the agent using the recommended command for that example.

---

For more information, see the individual README files in each subfolder.



## License

This project is licensed under the Apache License 2.0.