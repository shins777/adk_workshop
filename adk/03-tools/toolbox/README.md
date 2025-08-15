# Toolbox Agent Example (ADK)

This folder provides an example of a toolbox agent in the ADK (Agent Development Kit) environment, using ToolboxSyncClient for database integration to connect with external data sources such as BigQuery.

Before running the example, you need to understand and install MCP Toolbox for Database.

* MCP Toolbox for Databases
    * https://googleapis.github.io/genai-toolbox/getting-started/introduction/

* MCP Toolbox Installation
    * For installation instructions, refer to the MCP Toolbox GitHub:
    * https://github.com/googleapis/genai-toolbox

    ```
    # For MacOS users
    brew install mcp-toolbox
    ```

## .env Configuration

The `.env` file should be located in the parent folder (`03-tools`). For details on what to include in the environment file, refer to the following URL:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

The following environment settings are examples for using ADK with Vertex AI in an enterprise environment:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # Use Vertex AI for enterprise.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # Change to your own Project ID.
GOOGLE_CLOUD_LOCATION="global"                  # Use the global endpoint.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # Latest Gemini model.

# Toolbox configuration
TOOLBOX_SYNC_CLIENT = "http://127.0.0.1:5000"

```

For regular users using `AI Studio`, set the GOOGLE_API_KEY as follows:
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE

```

## Example tools.yaml

To set up tools in the toolbox, create a yaml file as shown below. The filename is typically `tools.yaml`.
For BigQuery configuration, refer to the following URL:
* https://googleapis.github.io/genai-toolbox/samples/bigquery/mcp_quickstart/


```yaml
sources:
  bigquery-bbc:
    kind: "bigquery"
    project: "ai-hangsik"

tools:
  query_bbc:
    kind: "bigquery-sql"
    source: "bigquery-bbc"
    statement:
      SELECT category, count(*) 
      FROM `ai-hangsik.bbc_news.fulltext` 
      group by category
    description: "Query the number of BBC news articles by category."

toolsets:
 my_bq_toolset:
   - query_bbc
```

## Example Execution

Set up Google Cloud authentication using the following gcloud command:
```
gcloud auth application-default login
```

### Run MCP Toolbox
Open a new console window and start the toolbox as follows:
```
toolbox --tools-file "tools.yaml"
```

### Run Agent
Similarly, GCP authentication is required in the shell:
```
gcloud auth application-default login
```
Run the Toolbox agent example with the following command:
```
adk_workshop/adk/03-tools$ adk web
```
After selecting the toolbox agent, try asking "Show me the BBC table."

## License

This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).
