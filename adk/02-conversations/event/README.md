# ADK 이벤트 대화 에이전트 - Event

이 폴더는 ADK(Agent Development Kit) 프레임워크를 활용해 이벤트 기반 대화형 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다. 이 에이전트는 Google 검색을 통해 사용자 질문에 답변하고, 러너 스크립트는 각 단계별 상세 이벤트 스트리밍과 내부 동작을 시연합니다.

## .env 예시

`.env` 파일을 상위 폴더(예: `adk/02-conversations/`)에 위치시키세요. 예시:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-project-id
PROJECT_NUMBER=your-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
```

---

## 폴더 구조

```
adk/02-conversations/event/
├── __init__.py
├── agent.py
├── runner.py
└── README.md
```

- `agent.py`  
  에이전트 정의, 지시문 템플릿 및 Google 검색 툴 연동 포함
- `runner.py`  
  에이전트 실행 및 이벤트 스트리밍, 각 단계별 상세 이벤트 정보 출력
- `__init__.py`  
  파이썬 패키지로 폴더 지정

---

## 예제 실행
**01-conversations** 폴더에서 아래 명령어를 실행하세요.

```
ai_agent/adk/02-conversations$ uv run -m event.runner
```

## 라이센스 정보
이 프로젝트는 Apache License 2.0에 따라 라이센스가 부여됩니다. 자세한 내용은 [LICENSE](../../../LICENSE) 파일을 참조하세요.