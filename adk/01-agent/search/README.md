# ADK 검색 에이전트 - Google Search Tool 활용

이 폴더는 Agent Development Kit(ADK)와 Google Search 연동을 활용한 에이전트 구현 예제를 제공합니다. 이 에이전트는 자체 지식과 실시간 검색 결과를 모두 활용해 사용자 질문에 답변합니다.

## .env 예시

`.env` 파일은 **상위 폴더**에 위치해야 합니다.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzerD6uPZRFklKWYZVM2uZh6Bd8 <-- 본인 키로 변경

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "921543942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
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
- **`README.md`**: 문서 파일(본 파일)

## 예제 실행
**01-agent** 폴더에서 아래 명령어를 실행하세요.

```
ai_agent/adk/01-agent$ adk web
```

## 라이센스

이 프로젝트는 Apache License 2.0에 따라 라이센스가 부여됩니다.