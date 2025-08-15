# Multiple Function Tool Example (ADK)

This folder demonstrates how to use function tools (e.g., exchange rates, stock prices) in ADK (Agent Development Kit).

## .env Setup

The `.env` file should be located in the parent folder (`03-tools`). For details on what to include in the environment file, refer to the following URL:

https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

Below is an example configuration for using ADK with Vertex AI in an enterprise environment:

To get the exchange rates, you can use https://api.frankfurter.app/ freely.   
But, in order to access "https://www.alphavantage.co/", you should have proper access key to use the service.   
Visit the https://www.alphavantage.co/ to get the api key. 

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # Use Vertex AI for enterprise.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # Change to your own Project ID.
GOOGLE_CLOUD_LOCATION="global"                  # Use Global Endpoint.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # Latest Gemini version.

# Stock API keys
STOCK_API_KEY = "STOCK_API_KEY"

```

For general users using AI Studio, set the GOOGLE_API_KEY as follows:

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
adk_workshop/adk/03-tools$ adk web
```

In the UI, select function_call and run the following command:
```
Please tell me the latest USD/KRW exchange rate and Google stock price.
```

## License

This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).
