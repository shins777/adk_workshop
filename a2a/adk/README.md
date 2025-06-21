# ADK A2A Project Overview

## Example Overview
This folder contains agent-to-agent (A2A) examples using the ADK framework. It demonstrates how to set up, run, and manage agents and clients for A2A communication, including basic concepts and simple agent workflows.

- `adk/`: Core ADK-based agent and client examples.
- `concept/`: Basic A2A agent and client concepts.

## Environment Setting
Set the following keys in your `.env` file (if required by your agent or client code):

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## How to Run the Source Code
1. Change the Python version for `uv` (if needed):
   ```bash
   uv venv --python 3.13
   ```
2. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```
3. Run agent or client examples as described in each subfolder's README.md.

## License Information
This project is licensed under the Apache License 2.0. See the [LICENSE](../LICENSE) file for details.
