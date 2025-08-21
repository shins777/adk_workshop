# MCP Client File Browser Agent Example (ADK)

This folder provides an agent example in ADK (Agent Development Kit) that uses Model Context Protocol (MCP) to explore and manage the file system.

## .env Configuration

The `.env` file should be located in the parent folder (`04-mcp`). For details on what to include in the environment file, refer to the following URL:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

The following environment settings are examples for using ADK with Vertex AI in an enterprise environment:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # Use Vertex AI for enterprise.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # Change to your own Project ID.
GOOGLE_CLOUD_LOCATION="global"                  # Use the global endpoint.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # Latest Gemini model.
```

For regular users using `AI Studio`, set the GOOGLE_API_KEY as follows:
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## How to Run the Source Code
Set up Google Cloud authentication using the following gcloud command:
```
gcloud auth application-default login
```

Run the sub-agent tool example with the following command:
```
adk_workshop/adk/04-mcp$ adk web
```

For testing, use a question like:
```
Search for information in the current folder.
```

## Explanation
- You can perform file system management tasks such as listing files and reading files in the specified folder, integrated with the MCP server.
- Connects to the MCP server using npx and @modelcontextprotocol/server-filesystem.

## License

This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).