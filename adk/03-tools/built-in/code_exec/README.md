# ADK Built-in Code Execution Agent

This folder demonstrates how to build and operate an ADK (Agent Development Kit) agent with built-in code execution capabilities. The agent can solve mathematical expressions by writing and executing Python code, returning both the code and the result as plain text.

The Code Execution Agent is designed to:
- Accept mathematical expressions from the user
- Write and execute Python code to solve the expression
- Return both the code and the result as plain text
- Respond in the same language as the user's input

---

## .env Example

Place your `.env` file in the parent folder (e.g., `adk/03-tools`). Example:

Note : This file should be located in the **parent upper folder**.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklKWYZVM2uZh6Bd8 <-- you should use your key.

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "921543942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
```
## Folder Structure

```
adk/03-tools/built-in/code_execution/
├── __init__.py
├── agent.py
├── README.md
```

- `agent.py`  
  Defines the code execution agent, its instruction template, and integrates the built-in code execution tool.
- `__init__.py`  
  Marks the folder as a Python package.


## Example Workflow

1. User provides a mathematical expression (e.g., "What is 2 + 2 * 3?")
2. Agent writes Python code to solve the expression
3. Agent executes the code and returns:
   - The Python code used
   - The final numerical result

---

## Example Usage
Note : Execute the following command on **03-tools/built-in** folder. 

```
ai_agent/adk/03-tools/built-in$ adk web
```

Jun 1 2025 : Error because of code change. 

```
ValueError: Failed to parse the parameter item: tuple[str, str] of function BuiltInCodeExecutor for automatic function calling. Automatic function calling works best with simpler function signature schema, consider manually parsing your function declaration for function BuiltInCodeExecutor.
```

---

## License

This project is licensed under the Apache License 2.0.
