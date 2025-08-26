# ADK Basic Agent Example - ADK Core Concepts

This folder demonstrates how to build and run a simple AI agent using the ADK (Agent Development Kit) framework.

## .env Setup

The `.env` file should be located in the parent folder (`01-agent`). For details on what to include in the environment file, refer to the following URL:  
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

Below is an example configuration for using ADK with Vertex AI in an enterprise environment:

You must set the GOOGLE_GENAI_LIVE_MODEL for the Gemini live model and set the location should be "us-central1" for currently possible region. 

```
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "us-central1"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"
GOOGLE_GENAI_LIVE_MODEL = "gemini-live-2.5-flash"
```

For general users using AI Studio, set the GOOGLE_API_KEY as follows:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## Running the Example

Set up Google Cloud authentication using the following gcloud command:

```
gcloud auth application-default login
```

The core role of the cacert.pem file is to verify that the SSL/TLS certificate presented by a website is genuine and was issued by a trusted authority (CA, Certificate Authority).

```
adk_workshop/adk/01-agent$ export SSL_CERT_FILE=$(python3 -m certifi) 
```

From the `01-agent` folder, run the command below and test in the adk web interface:
```
adk_workshop/adk/01-agent$ adk web
```

## License
This project follows the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).