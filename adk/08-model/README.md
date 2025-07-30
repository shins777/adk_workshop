# 모델 연동 예제 (ADK)

## 예제 개요
이 폴더는 외부 LLM 제공자를 ADK 프레임워크와 연동하는 방법을 보여줍니다. LiteLLM(OpenAI, Anthropic) 및 Ollama 기반 모델 예제가 포함되어 있습니다.

- `litellm/`: LiteLLM을 통해 OpenAI GPT-4o, Anthropic Claude를 ADK 에이전트와 연동하는 예제
- `ollama_agent/`: 로컬 Ollama 모델(Llama 3, Gemma 등)을 ADK 에이전트와 연동하는 예제

## 환경 설정
`.env` 파일을 작업 디렉토리에 복사하고 아래와 같이 키를 설정하세요.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=...
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
PROJECT_ID=...
PROJECT_NUM=...
LOCATION=...
MODEL=...
OLLAMA_API_BASE=...
```

각 하위 폴더별 요구사항은 해당 폴더를 참고하세요.

## 실행 방법
- 각 하위 폴더(`litellm/`, `ollama_agent/`)의 에이전트 코드와 안내를 참고하세요.
- 예시 (`litellm`):
  ```bash
  uv run python litellm/llm.py
  ```
- 예시 (`ollama_agent`):
  ```bash
  uv run python ollama_agent/agent.py
  ```

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다. 자세한 내용은 [LICENSE](../LICENSE) 파일을 참고하세요.
