# Ollama 에이전트 예제 (ADK)

## 예제 개요
이 예제는 ADK 프레임워크에서 로컬 Ollama 모델(Llama 3, Gemma 등)을 LLM 에이전트로 연동하는 방법을 보여줍니다.

## 환경 설정
`.env` 파일에 아래와 같이 키를 설정하세요.

```
OLLAMA_API_BASE=http://localhost:11434
```

기타 기능을 위해서는 (예: GOOGLE_API_KEY) 추가 키가 필요할 수 있습니다.

## 실행 방법
아래 명령어로 에이전트 예제를 실행하세요.

```bash
uv run python agent.py
```

`agent.py` 파일을 수정하여 사용할 모델(`gemma` 또는 `llama`)을 선택할 수 있습니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다. 자세한 내용은 [LICENSE](../../LICENSE) 파일을 참고하세요.
