# ADK 04-mcp Guide

This directory contains examples and utilities that demonstrate how to expose and consume Model Context Protocol (MCP) tools using different transports and server styles. The examples show both server implementations (stdio and Streamable HTTP) and client-side examples that connect to those servers.

## Overview
MCP lets agents and tools communicate using a standardized protocol. This folder provides reference implementations that are useful when you want to:
- Expose custom tools (FunctionTool, wrappers) to remote agents via MCP.
- Run MCP servers using different transports (stdio, Streamable HTTP) suitable for local testing or deployment (e.g., Cloud Run).
- Build or test lightweight MCP clients that consume remote tools.

## Folder and Example Summary

### streamable_http
- Purpose: Example Streamable HTTP MCP server and utilities.
- Key files: `mcp_server/remote_server.py`, `mcp_server/Dockerfile`
- Description: A Starlette + uvicorn ASGI app that mounts a Streamable HTTP MCP endpoint (`/mcp`). The example advertises a `get_exchange_rate` tool (Frankfurter API) and demonstrates running blocking calls safely off the event loop. The Dockerfile shows how to build a container suitable for Cloud Run.

### stdio (stdio MCP server examples)
- Purpose: Example MCP servers that run over stdio (useful for local process-based setups and simpler testing).
- Key files: examples that implement MCP stdio servers exposing FunctionTool wrappers and demonstrating `list_tools` and `call_tool` handlers.
- Description: Useful for learning how to expose tools to agents via a subprocess-based MCP transport.

### mcp_client
- Purpose: MCP client examples that connect to MCP servers and call tools programmatically.
- Key files: client implementations and example agents that use MCP-based tools.
- Description: Includes a file-browser style agent and other small clients that demonstrate how to use MCP connection parameters to talk to stdio or Streamable HTTP servers.

### mcp_client_server
- Purpose: End-to-end client+server example demonstrating a client agent interacting with a Python MCP server.
- Key files: client-side agent examples and server implementations (exchange rate tool example).

### mcp_google_map
- Purpose: Example showing how to wrap Google Maps functionality as an MCP tool.
- Key files: agent wrappers and a small server/launcher example.
- Notes: Requires a valid `GOOGLE_MAPS_API_KEY` set in the environment. The example may launch a local helper using `npx` in some configurations — review the README in that subfolder for details and security considerations.


## How to run the examples

Check the README and source files inside each  subfolder for details about that example and how to run the specific agent or server.

## License
This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).