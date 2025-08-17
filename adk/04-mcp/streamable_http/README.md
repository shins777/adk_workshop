# MCP Server Exchange Rate Agent Example (ADK)

This directory contains an example ADK (Agent Development Kit) setup that demonstrates how to expose a simple tool via the Model Context Protocol (MCP) using a Streamable HTTP transport. The example provides a small MCP server that returns exchange rate information by calling the Frankfurter API.

## .env Configuration

The example expects environment configuration to be available in a `.env` file in the repository root or the parent `04-mcp` directory. See the ADK quickstart for recommended variables and authentication steps:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

Typical environment variables used in the ADK examples:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=global
GOOGLE_GENAI_MODEL=gemini-2.5-flash

# OR for AI Studio usage:
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## How to run the MCP server locally

### Streamable MCP 서버 Cloud run 기반으로 기동.

Similarly, GCP authentication is required in the shell:
```
gcloud auth application-default login
```

먼저 mcp_server 안에 있는 remote_server.py 파일을 GCP Cloud run 위에 기동을 해야 합니다.
실행 방법은 아래와 같습니다.

```
adk/04-mcp/streamable_http/mcp_server $ . ./deploy.sh
```

정상적으로 기동이 되었다면 GCP console 에서 확인이 가능합니다. 

### ADK agent 에서 Streamable MCP 서버 접속 및 실행.

Similarly, GCP authentication is required in the shell:
```
gcloud auth application-default login
```

Run the ADK agent example with the following command:
```
adk/04-mcp $ adk web
```

Ask "Show me the won-dollar exchange rate on August 14, 2025."

## License

This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).
