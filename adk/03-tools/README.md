# ADK 03-tools Complete Guide

This directory contains submodules that provide various agent and tool functionalities in ADK (Agent Development Kit). Each subfolder is responsible for a specific feature or integration with external services. Below is an overview of each tool and instructions for environment setup.

## Folder and Feature Summary

### agent_tool
Sub Agent tool example. Demonstrates how to register and use an Agent as a tool in ADK. Includes differences and usage of Agent vs Sub Agent, and .env setup examples.

### bigquery
Built-in BigQuery agent for ADK. Includes examples for searching various metadata in BigQuery and querying specific table information using natural language.

### code_execution
Built-in code execution agent for ADK. Provides automated code execution features such as writing and running Python code, solving expressions, and returning results. Includes .env setup examples.

### function_call
Multi-function tool example. Guides how to integrate various function-based tools (e.g., exchange rates, stock prices). Includes .env setup and Stock API key examples.

### google_search
Google Search tool example. Demonstrates how to use the built-in Google Search tool with an ADK agent to answer user queries with real-time web search results. Includes .env setup examples.

### langchain_tavily
Tavily Search tool example. Provides examples for integrating LangChain-based Tavily Search and exchange rate queries for web search and currency information. Includes .env setup and Tavily API key examples.

### mcp_client
MCP client file browser agent example. Uses Model Context Protocol (MCP) to explore and manage the file system. Includes .env setup and GOOGLE_API_KEY instructions for AI Studio.

### mcp_client_server
MCP server exchange rate agent example. Integrates with a custom Python MCP server to provide real-time exchange rate information. Includes .env setup examples.

### rag_engine
RAG engine tool example. Guides how to use Vertex AI-based RAG (Retrieval-Augmented Generation) engine for corpus search. Includes .env setup and RAG_CORPUS examples.

### toolbox
MCP toolbox for database example, This folder provides an example of a toolbox agent in the ADK (Agent Development Kit) environment, using ToolboxSyncClient for database integration to connect with external data sources such as BigQuery.

### vertexai_search
Vertex AI Search tool example. Provides functionality to answer user queries based on Vertex AI Search datastore. Includes .env setup and VAIS_PROJECT_NUMBER examples.

## Ways to use the codes.
Refer to each subfolder's README.md for detailed usage, example code, and environment setup instructions.

## License

This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).