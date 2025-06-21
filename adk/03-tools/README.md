# ADK Tools Overview

## Example Overview
This directory contains a comprehensive set of examples for integrating various types of tools into ADK (Agent Development Kit) agents. Each subfolder demonstrates a different approach to tool integration, including built-in tools, function tools, LangChain tools, and Model Context Protocol (MCP) tools. Use these examples to learn how to extend agent capabilities with real-world data, web search, code execution, and external system integration.

## Environment Setting
Set the following keys in your `.env` file (located in this folder):

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=your_location
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
RAG_CORPUS=your_rag_corpus
DATASTORE_ID=your_datastore_id
STOCK_API_KEY=your_stock_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Refer to each subfolder for additional requirements.

## How to Run the Source Code
- See each subfolder for agent code and instructions.
- Example (for a built-in tool):
  ```bash
  uv run python built-in/code_execution/agent.py
  ```
- Example (for a function tool):
  ```bash
  uv run python function/single_call/agent.py
  ```
- Example (for a LangChain tool):
  ```bash
  uv run python langchain/tavily_search/agent.py
  ```
- Example (for an MCP tool):
  ```bash
  uv run python mcp/client_file_browser/agent.py
  ```

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../LICENSE) file for details.