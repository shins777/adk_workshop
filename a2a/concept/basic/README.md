# ADK A2A 기본 예제

## 예제 개요
이 폴더는 ADK 프레임워크를 활용한 에이전트-에이전트(A2A) 통신의 기본적인 에이전트, 클라이언트, 서버 예제를 포함합니다. 최소한의 동작으로 A2A 워크플로우를 구현하는 방법을 보여줍니다.

- `agent.py`: 기본 에이전트 구현 예제
- `client.py`: 기본 클라이언트 구현 예제
- `server.py`: 기본 서버 구현 예제
- `executor.py`: 에이전트 동작을 위한 유틸리티 모듈

## 환경 설정
에이전트 또는 클라이언트 코드에서 필요하다면, `.env` 파일에 다음과 같이 키를 설정하세요:

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
ai_agent/a2a/concept$ uv run -m basic.server
```

### 2. client 실행

```
ai_agent/a2a/concept$ uv run -m basic.client

```

## 라이선스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.