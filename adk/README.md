# AI Agent on ADK(Agent Development Kit)

The source codes in this repository were developed using VS Code, but it's IDE-agnostic.  
You can install VS Code from the following url.  Note : https://code.visualstudio.com/

## git clone
```
git clone https://github.com/ForusOne/adk_agent.git
```

## Install uv package manager.
### 1. uv install

This project uses uv for python package manager.    
An extremely fast Python package and project manager, written in Rust.
Note : https://github.com/astral-sh/uv

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
or 
```
pip install uv
```

## 2. uv inititalizaton and set virtual env. 

Initialize venv with **pyproject.toml** file which should be located in **the same directory**.  
You have to have **pyproject.toml** in the **/adk_agent/adk** directory.

```
/adk_agent/adk$ uv venv --python 3.12
```

Activate the virtual environment
```
/adk_agent/adk$ source .venv/bin/activate
(adk) adk_agent/adk$
```

After finishing the test, you can deactivate the virtual environment.
```
/adk_agent/adk$ deactivate
```

###  3. Unit test for a simple ADK agent. 

To check the runtime virtual environment is properly configured, let's run a simple ADK agent in code. 

adk package install.

```
(adk) /adk_agent/adk/01-agent$ uv add google-adk[vertexai]==1.1.1
```

Create .env file in **adk_agent/adk/01-agent/***

```
(adk) /adk_agent/adk/01-agent$ ls -al
total 16
drwxr-xr-x   7 forus  pgroup   224 Jun  2 08:26 .
drwxr-xr-x  18 forus  pgroup   576 Jun  2 08:21 ..
-rw-r--r--   1 forus  pgroup   198 Jun  2 08:26 .env
-rw-r--r--   1 forus  pgroup  3178 Jun  2 08:20 README.md
drwxr-xr-x   6 forus  pgroup   192 Jun  2 08:25 basic
drwxr-xr-x   8 forus  pgroup   256 Jun  2 08:20 runtime
drwxr-xr-x   7 forus  pgroup   224 Jun  2 08:26 search
(adk) /adk_agent/adk/01-agent$
```

Here is sample .env file, change the information with your GCP project information and API key. 

Note: https://ai.google.dev/gemini-api/docs/api-key

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzaSyD6ugbCWYZVM2uZh6Bd8

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "721523942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
```

Run the unit test
```
(adk) /adk_agent/adk/01-agent$ adk web
```

Type in the chat : What is Generative AI ?

If your test is ok, you can see the following output.
![adk_web](https://github.com/ForusOne/adk_agent/blob/main/images/adk_web.png?raw=true)