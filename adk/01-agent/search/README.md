# ADK 검색 에이전트 - Google Search Tool 활용

이 폴더는 Agent Development Kit(ADK)와 Google Search 연동을 활용한 에이전트 구현 예제를 제공합니다. 이 에이전트는 자체 지식과 실시간 검색 결과를 모두 활용해 사용자 질문에 답변합니다. 이 예제를 통해서 간단한 Tool 사용방법을 이해할 수 있습니다.

## .env 설정.

`.env` 파일은 현재 runtime 폴더의 **상위 폴더(01-agent)**에 위치해야 합니다.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-gcp-project-id
PROJECT_NUMBER=your-gcp-project-number
LOCATION=us-central1
MODEL=gemini-2.5-flash
```

## 폴더 구조

```
adk/01-agent/search/
├── __init__.py
├── agent.py
├── instruction.py
└── README.md
```

- **`agent.py`**: 메인 에이전트 정의 및 빌더
- **`instruction.py`**: 에이전트 동작을 위한 지시문 템플릿
- **`__init__.py`**: 에이전트 임포트용

## 예제 실행

**01-agent** 폴더에서 아래 명령어를 실행하세요.

```
ai_agent/adk/01-agent$ adk web
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.