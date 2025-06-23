# ADK A2A 간단 예제

## 예제 개요
이 폴더는 ADK 프레임워크를 활용한 에이전트-에이전트(A2A) 통신의 간단한 에이전트, 클라이언트, 서버 예제를 포함합니다. 기본적인 A2A 워크플로우를 설정하고 실행하는 방법을 보여줍니다.

- `agent.py`: 에이전트 예제 구현
- `client.py`: 클라이언트 예제 구현
- `server.py`: 서버 예제 구현
- `convert.py`, `executor.py`: 에이전트 동작을 위한 유틸리티 모듈

## 환경 설정
에이전트 또는 클라이언트 코드에서 필요하다면, 상위 폴더의 `.env` 파일에 다음과 같이 키를 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## 실행 방법
아래와 같이 에이전트, 클라이언트, 서버 예제를 실행할 수 있습니다:

### 1. A2A 서버 기동.

```
ai_agent/a2a/adk $ uv run -m simple.server
```

### 2. client 실행

```
ai_agent/a2a/adk $ uv run -m simple.client

```

자세한 내용은 각 하위 폴더의 README.md를 참고하세요.

## 라이선스 안내
이 프로젝트는 Apache License 2.0 하에 배포됩니다. 자세한 내용은 [LICENSE](../../LICENSE) 파일을 참고하세요.
