# ADK 05-workflow Guide

This directory demonstrates several workflow patterns built with the Agent Development Kit (ADK). Depending on your business scenario, you can combine multiple agents and tools in various ways. The examples below illustrate common workflow agent types and how to use them.

![agent types](https://google.github.io/adk-docs/assets/agent-types.png)
Image source: https://google.github.io/adk-docs/agents/#agents

## Example workflows by folder

### 1. custom
- Purpose: CriticAgent workflow demonstrating positive, negative, and aggregated reviews.
- Description: Sub-agents produce positive, negative, and combined reviews; results are aggregated to complete the full workflow.

### 2. general
- Purpose: General workflow agent example.
- Description: A flexible workflow that can be extended or customized for a variety of business scenarios.

### 3. loop
- Purpose: Loop-based workflow agent example.
- Description: Processes user input iteratively, suitable for iterative improvement, multi-turn questioning, and multi-step tasks.

### 4. parallel
- Purpose: Parallel workflow agent example.
- Description: Runs multiple tasks or sub-agents in parallel to achieve faster completion or enable multi-agent collaboration.

### 5. sequencial
- Purpose: Sequential workflow agent example.
- Description: Processes multiple stages or sub-agents in a fixed order, suitable when steps must be executed sequentially (step-by-step reasoning or staged processing).

## How to run

Check the README and source files inside each workflow subfolder for details about that example and how to run the specific agent or server.

## License
This project is licensed under the Apache License 2.0. All code and content copyright **ForusOne** (shins777@gmail.com).
