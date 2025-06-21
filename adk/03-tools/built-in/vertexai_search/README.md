# Vertex AI Search Tool Example (ADK)

## Example Overview
This folder demonstrates how to use the built-in Vertex AI Search tool with ADK agents to answer user queries using Vertex AI Search data stores.

## Environment Setting
Set the following keys in your `.env` file (located in the parent folder):

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=your_location
PROJECT_NUMBER=your_project_number
DATASTORE_ID=your_datastore_id
MODEL=your_model_name
```

## Example Usage
Note : Execute the following command on **03-tools/built-in** folder. 

```
ai_agent/adk/03-tools/built-in$ adk web
```

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../../../LICENSE) file for details.
