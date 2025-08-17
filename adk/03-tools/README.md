# ADK 03-tools Complete Guide

This directory hosts a collection of tool and agent examples for the Agent Development Kit (ADK). Each subfolder demonstrates a particular integration pattern or toolset you can use within ADK agents (e.g., MCP servers, search tools, code execution, BigQuery access). The summaries below describe the purpose and key files for each example.

## Folder and Feature Summary

### agent_tool
- Purpose: Example showing how to register and use an Agent as a tool within ADK.
- Key files: `agent.py`, supporting sub-agents and examples.
- Description: Demonstrates the differences between using a full Agent vs a Sub-Agent as a callable tool, and shows how to wire that tool into another agent's workflow.

### bigquery
- Purpose: BigQuery integration example for ADK.
- Key files: agent and tool wrappers that demonstrate how to query BigQuery programmatically.
- Description: Shows how to search dataset and table metadata, and how to run natural-language driven queries against BigQuery.

### code_execution
- Purpose: Code execution tool example.
- Key files: example agents and an execution tool that can write and run Python code.
- Description: Demonstrates automated code generation and execution flows (e.g., compute results, run small programs) and how to return outputs to agents.

### function_call
- Purpose: Multi-function tool examples.
- Key files: wrappers for small function-based tools (exchange rates, stock prices, etc.).
- Description: Shows how to expose and use multiple function-call style tools from agents and how to configure API keys in `.env` for external services.

### google_search
- Purpose: Google Search integration example.
- Key files: agent examples and tool wrappers for web search.
- Description: Demonstrates using the built-in Google Search tool to answer user queries using live web search results (requires appropriate API credentials configured in `.env`).

### langchain_tavily
- Purpose: Integrating LangChain/Tavily search.
- Key files: example connectors and agent wrappers.
- Description: Shows how to wire a LangChain-based search (Tavily) into ADK agents and combine web/corpus search and exchange-rate lookups where applicable.

### rag_engine
- Purpose: RAG (Retrieval-Augmented Generation) engine examples.
- Key files: agents and connectors for Vertex AI RAG retrieval.
- Description: Demonstrates how to configure a RAG pipeline using Vertex AI and ADK, including guidance for preparing a corpus and configuring datastore IDs.

### vertexai_search
- Purpose: Vertex AI Search integration example.
- Key files: agent examples and configuration to query Vertex AI Search datastores.
- Description: Shows how to answer user queries from documents indexed into Vertex AI Search. Requires VAIS-related environment variables for authentication.

## How to use these examples
- Each subfolder contains a `README.md` with detailed instructions about required environment variables, how to run the example, and any additional setup steps.

## License
This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).