# ADK 이벤트 대화 에이전트 - Event

이 폴더는 ADK(Agent Development Kit) 프레임워크를 활용해 이벤트 기반 대화형 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다. 
이벤트는 ADK에서 사용자와 Agent 간의 커뮤니케이션 하는 과정에서 매우 중요한 개념입니다. 이 코드에서는 개별 이벤트내의 다양한 속성 정보를 확인할 수 있습니다.
이 에이전트는 기본적으로 Google 검색을 통해 사용자 질문에 답변하고, 러너 스크립트는 각 단계별 상세 이벤트 스트리밍과 내부 동작을 시연합니다.

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

아래 Runner 클래스를 사용하는 방법은 좀더 Programatic 방식으로 이벤트를 코드레벨에서 제어할 수 있습니다.
```
ai_agent/adk/02-conversations$ uv run -m event.runner
```
또는 웹상에서 이벤트별 내용을 확인하기 위해서 아래 명령어 사용도 가능합니다. 
```
ai_agent/adk/02-conversations$ adk web
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.