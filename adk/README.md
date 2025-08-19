# ADK (Agent Development Kit) Local Development Setup

ADK provides a convenient local development environment for building and testing agents. Developing locally is recommended because commands like `adk web` make it easy to inspect, debug, and understand complex data flows. If you prefer rapid prototyping in notebooks, refer to the examples under the `notebooks/` directory (note: not all features are covered there).

The source code was developed with Visual Studio Code but is not tied to any specific IDE. Clone the repository and use the tools that fit your development environment. If you want to install VS Code, see https://code.visualstudio.com/.

## Git clone
To get the repository locally, run:

```
git clone https://github.com/shins777/adk_workshop.git
```

## Install the `uv` package manager

This project uses `uv` as the Python package and project manager. `uv` is a fast, ergonomic manager written in Rust. See the project for more details: https://github.com/astral-sh/uv

You can install `uv` using one of the following methods:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

or

```
pip install uv
```

## 2. Initialize a virtual environment with `uv`

It is recommended to use a Python virtual environment when working with `uv`.
If you cloned the repository, a `pyproject.toml` file should exist under `adk_workshop/adk`. That file defines the project dependencies and allows `uv` to create an isolated environment to run the example code.

We recommend using Python 3.12 for development.

Create the virtual environment:

```
cd adk_workshop/adk
uv venv --python 3.12
```

Activate the virtual environment:

```
source .venv/bin/activate
(adk) adk_workshop/adk$
```

When finished testing, deactivate the environment:

```
deactivate
```

## 3. Quick ADK agent smoke test

Verify the runtime environment by running a simple ADK agent example.

1) Install the ADK package into your environment. As of July 2025 this example targets `google-adk` 1.8.0:

```
(adk) adk_workshop/adk/01-agent$ uv add "google-adk[vertexai]==1.8.0"
```

2) Create a `.env` file containing runtime configuration used by the examples. For quick testing, create the `.env` file inside `adk_workshop/adk/01-agent/`.

Example directory listing after creating `.env`:

```
(adk) adk_workshop/adk/01-agent$ ls -al
total 16
-rw-r--r--   1 user  staff   198 Jun  2 08:26 .env
-rw-r--r--   1 user  staff  3178 Jun  2 08:20 README.md
drwxr-xr-x   6 user  staff   192 Jun  2 08:25 basic
drwxr-xr-x   8 user  staff   256 Jun  2 08:20 runtime
drwxr-xr-x   7 user  staff   224 Jun  2 08:26 search
```

Refer to the ADK quickstart for variables required in `.env`:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

Example enterprise (Vertex AI) `.env` variables:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="ai-hangsik"
GOOGLE_CLOUD_LOCATION="global"
GOOGLE_GENAI_MODEL="gemini-2.5-flash"
```

For AI Studio / API key usage:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

3) Run the ADK example via the ADK CLI. Authenticate to Google Cloud if needed:

```
gcloud auth application-default login
```

Start the example UI / runtime:

```
(adk) adk_workshop/adk/01-agent$ adk web
```

Enter a test prompt such as "What is Generative AI?" into the chat interface. If the test runs correctly, you should see the ADK web interface similar to the screenshot in the repository.

## Additional notes
- The examples assume a working Python environment with the required dependencies installed. If you encounter import errors, verify the virtual environment and installed packages.
- The repository includes notebook examples for quick experimentation; they may not cover every feature.
- Protect API keys and other secrets; do not commit `.env` files containing real credentials to version control.

## License
This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).