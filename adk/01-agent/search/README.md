# ADK Search Agent - Use Google Search Tool 

This folder provides an example of an agent implementation using the Agent Development Kit (ADK) with Google Search integration. The agent is designed to answer user queries by leveraging both its own knowledge and real-time search results.

## .env Sample

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklKWYZVM2uZh6Bd8 <-- you should use your key.

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "921543942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
```

## Folder Structure

```
adk/01-agent/search/
├── __init__.py
├── agent.py
├── instruction.py
└── README.md
```

- **`agent.py`**: Main agent definition and builder.
- **`instruction.py`**: Contains the instruction template for the agent's behavior.
- **`__init__.py`**: Imports the agent for easy access.
- **`README.md`**: Documentation (this file).

## Example Usage
Note : Execute the following command on **01-agent** folder. 

```
ai_agent/adk/01-agent$ adk web
```

## License

This project is licensed under the Apache License 2.0.