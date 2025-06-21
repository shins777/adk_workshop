# LangChain Tools Example (ADK)

## Example Overview
This folder demonstrates how to use LangChain-powered tools with ADK agents for advanced web search and data retrieval.

- `tavily_search/`: Tavily web search and exchange rate agent.

## Environment Setting
Set the following keys in your `.env` file (located in the parent folder):

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
TAVILY_API_KEY=your_tavily_api_key
```

## How to Run the Source Code
See the subfolder for agent code and instructions. Example:

```bash
langchain/adk web
```

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../LICENSE) file for details.
