# ADK 01-Agent Example

This directory contains example implementations of agents using the Agent Development Kit (ADK). Each subfolder demonstrates a different approach, from basic setup to advanced runtime and search-enabled agents.

## ADK Components
The image below illustrates the main components of the ADK framework:  
![adk component](https://github.com/ForusOne/adk_agent/blob/main/images/adk_components.png?raw=true)

## Agent Hierarchy
ADK allows you to build multi-agent systems **within a single process**. You can combine multiple sub-agents and tools to create a multi-agent system, but all processing is handled monolithically within one process.  
![Agent Hierarchy](https://github.com/ForusOne/adk_agent/blob/main/images/multi-agent.png?raw=true)


## 01-agent Logic and Structure

The `01-agent` examples demonstrate the fundamental logic and structure of an ADK-based agent system:

- **Agent Initialization**: Define and initialize a root agent and multiple sub-agents using ADK.
- **Message Routing**: User input is received by the root agent, which routes the message to the appropriate sub-agent or tool for processing.
- **Role Assignment**: Each sub-agent is responsible for a specific task (e.g., critique, information retrieval), and the root agent combines their outputs to generate the final response.
- **Monolithic Execution**: All agents and tools run within a single process, making management and deployment straightforward.

## .env Configuration

For environment variable setup, refer to the following URL:  
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model 

Below is an example configuration for enterprise use with Vertex AI:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION="YOUR_PROJECT_LOCATION"
GOOGLE_GENAI_MODEL="gemini-2.5-flash"
```

For general users with AI Studio, set the `GOOGLE_API_KEY` as follows:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## Getting Started

1. Choose one of the subfolders as needed.
2. Review the README file in the selected subfolder for specific setup and usage instructions.
3. Place the `.env` file in the parent folder as described above.
4. Run the agent using the recommended command for the chosen example.

For more details, refer to the individual README files in each subfolder.

## License

This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).