# MCP Google Maps Tool Example (ADK)

This folder demonstrates how to integrate the Google Maps MCP server tool with an ADK agent using the Model Context Protocol (MCP). The provided `agent.py` shows how to initialize an MCPToolset that launches the `@modelcontextprotocol/server-google-maps` server (via `npx`) and expose Google Maps capabilities to an LLM-powered agent.

> Note: This example is experimental. The MCP server implementation and tool behavior may change over time.

## .env configuration

Place a `.env` file in the parent folder (`04-mcp `). The agent expects the Google Maps API key to be available through the `GOOGLE_MAPS_API_KEY` environment variable.

Example `.env` entries (parent `04-mcp ` folder):

```
# Use Vertex AI or AI Studio according to your environment
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="your-project-id"
GOOGLE_CLOUD_LOCATION="global"
GOOGLE_GENAI_MODEL="gemini-2.5-flash"

# Provide your Google Maps API key used by the MCP Google Maps server
GOOGLE_MAPS_API_KEY=PASTE_YOUR_GOOGLE_MAPS_API_KEY_HERE
```

If the `GOOGLE_MAPS_API_KEY` is not set, the agent will raise an error to prevent launching the tool without credentials.

## Requirements

- Node.js / npx installed (the MCP Google Maps server is launched with `npx`).
- A valid Google Maps API key with the required Maps APIs enabled.
- ADK environment and dependencies installed according to the main project README.

## How to run

1. Authenticate with Google Cloud if you are using Vertex AI or other GCP resources:

```
gcloud auth application-default login
```

2. Ensure the `.env` file in `04-mcp ` contains a valid `GOOGLE_MAPS_API_KEY` and other required entries.

3. Run the ADK web server to load the tools and agents:

```
adk_workshop/adk/04-mcp $ adk web
```

When the agent initializes, it will create an MCPToolset that launches the Google Maps MCP server via `npx @modelcontextprotocol/server-google-maps` and injects the `GOOGLE_MAPS_API_KEY` into the server process environment.

## Usage

- After starting the ADK web UI, select the Google Maps / MCP agent (the agent name is `Assistant_agent_Google_Map` in `agent.py`).
- Ask mapping-related questions such as:

```
Find the nearest coffee shop to my current location.
```

or

```
Get directions from Central Park, New York to Times Square, New York.
```

The agent will forward appropriate requests to the MCP Google Maps server and return the results.

## Security considerations

- Do not commit your API key into source control. Always use environment variables or a secure secret store.
- For production, restrict the API key to authorized HTTP referrers or IP addresses and enable only required Maps APIs.

## Troubleshooting

- If the agent raises `RuntimeError: GOOGLE_MAPS_API_KEY is not set.`, verify that the `.env` file is in the parent `04-mcp ` folder and contains a valid `GOOGLE_MAPS_API_KEY` entry.
- Ensure `npx` is available in the system PATH and that `@modelcontextprotocol/server-google-maps` can be launched on your machine.
- Check the browser console and the terminal running `adk web` for server startup logs and error messages.

## License

This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).