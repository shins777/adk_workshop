# Function Tools Example (ADK)

## Example Overview
This folder demonstrates how to use function tools with ADK agents for calling external APIs. Examples include single and multiple function tool calls.

- `single_call/`: Single function tool (e.g., exchange rates).
- `multiple_call/`: Multiple function tools (e.g., exchange rates, stock prices).

## Environment Setting
Set the following keys in your `.env` file (located in the parent folder):

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
STOCK_API_KEY=your_stock_api_key
```

## How to Run the Source Code
See each subfolder for agent code and instructions. Example:

```bash
function/single_call/adk web
```

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../../LICENSE) file for details.
