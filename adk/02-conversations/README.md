# ADK 02-Conversations Examples

This directory contains advanced conversation agent examples using the Agent Development Kit (ADK). Each subfolder demonstrates a different approach to session management, memory, event streaming, and stateful agent design.

## Background
### Session, Event and State

<img src="https://github.com/ForusOne/adk_agent/blob/main/images/session_state_events.png?raw=true" alt="drawing" width="600"/>

## Subfolders Overview

### 1. `event/` — Event-Driven Conversation Agent

- Answers user questions using Google Search and provides structured responses.
- Streams detailed event information for each step of the conversation.
- See [`event/README.md`](./event/README.md) for details.

### 2. `memory/` — Memory-Enabled Conversation Agent

- Combines a search agent and a recall agent to demonstrate storing and retrieving information from memory.
- Supports both in-memory and Vertex AI RAG corpus memory backends.
- See [`memory/README.md`](./memory/README.md) for details.

### 3. `session/` — Session-Aware Conversation Agent

- Demonstrates session management, allowing conversations to persist across turns and sessions.
- Supports in-memory, database, and Vertex AI session backends.
- See [`session/README.md`](./session/README.md) for details.

### 4. `state/` — Stateful Conversation Agent

- Tracks and updates state across conversation turns using both implicit and explicit state management.
- Demonstrates how to use output keys and events to manage session state.
- See [`state/README.md`](./state/README.md) for details.

## Getting Started

1. Choose a subfolder (`event`, `memory`, `session`, or `state`) based on your needs.
2. Review the subfolder's README for specific setup and usage instructions.
3. Place your `.env` file in the parent folder as described above.
4. Run the agent using the recommended command for that example.

---

For more information, see the individual README files in each subfolder.
