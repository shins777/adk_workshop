# ADK Built-in Code Execution Agent

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent with built-in code execution capabilities. The agent writes and executes Python code to solve mathematical expressions, returning both the code and results as plain text.

The code execution agent provides the following features:
- Receives mathematical expressions from the user.
- Writes and executes Python code to solve the expressions.
- Returns both the code and results as plain text.
- Responds in the same language as the user input.

## .env Setup

The `.env` file should be located in the parent folder (`03-tools`). For details on what to include in the environment file, refer to the following URL:

https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

Below is an example configuration for using ADK with Vertex AI in an enterprise environment:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # Use Vertex AI for enterprise.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # Change to your own Project ID.
GOOGLE_CLOUD_LOCATION="global"                  # Use Global Endpoint.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # Latest Gemini version.
```

For general users using AI Studio, set the GOOGLE_API_KEY as follows:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## Folder Structure

```
adk/03-tools/code_execution/
├── __init__.py
├── agent.py
├── README.md
```

## How to Run the Source Code
Set up Google Cloud authentication using the following gcloud command:
```
gcloud auth application-default login
```

Run the sub-agent tool example with the following command:
```
adk_workshop/adk/03-tools$ adk web
```

In the UI, select code_execution and run the following command:
```
Write and execute a program to find and sum all prime numbers from 1 to 100.
```

## License

This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).
