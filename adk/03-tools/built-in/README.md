# Built-in Tools Example (ADK)

## Example Overview
This folder demonstrates how to use built-in tools with ADK agents, including code execution, Google search, RAG, and VertexAI search. Each subfolder provides a specific example.

- `code_execution/`: Math/code execution agent.
- `google_search/`: Google search agent.
- `rag_engine/`: Vertex AI RAG corpus retrieval agent.
- `vertexai_search/`: Vertex AI Search data store agent.

## Environment Setting
Set the following keys in your `.env` file (located in the parent folder):

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## How to Run the Source Code
See each subfolder for agent code and instructions. Example:

```bash
built-in/adk web
```

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../LICENSE) file for details.
