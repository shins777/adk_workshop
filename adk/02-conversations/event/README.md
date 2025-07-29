# ADK 이벤트 대화 에이전트 - Event

이 폴더는 ADK(Agent Development Kit) 프레임워크를 활용해 이벤트 기반 대화형 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다. 
이벤트는 ADK에서 사용자와 Agent 간의 커뮤니케이션 하는 과정에서 매우 중요한 개념입니다. 이 코드에서는 개별 이벤트내의 다양한 속성 정보를 확인할 수 있습니다.
이 에이전트는 기본적으로 Google 검색을 통해 사용자 질문에 답변하고, 러너 스크립트는 각 단계별 상세 이벤트 스트리밍과 내부 동작을 시연합니다.

이 예제에서는 실제 이벤트 내에 다양한 정보를 파싱해서 확인하는 예제입니다.  실제 프로젝트에서는 해당 이벤트 내의 정보를 활용하여 다양한 제어를 하거나 결과를 표현할수 있습니다.

## .env 설정.

`.env` 파일은 현재 runtime 폴더의 `상위 폴더(02-conversations)` 에 위치해야 합니다.  환경파일내 들어갈 내용은 아래 URL을 참고하세요.    
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model 

아래 환경설정은 기업에서 `Vertex AI`기반에서 ADK를 사용할때 적용되는 예제입니다.    

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 를 참고해서 변경.
GOOGLE_CLOUD_LOCATION="global"                  # Global Endpoint 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 현재 Gemini 최신 버전.
```

참고로 `AI Studio`를 사용하는 일반 사용자 버전은 아래와 같이 GOOGLE_API_KEY 를 셋팅해야 합니다.  

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## 폴더 구조

```
adk/02-conversations/event/
├── __init__.py
├── agent.py
├── runner.py
└── README.md
```

- `agent.py` : 에이전트 정의, 지시문 템플릿 및 Google 검색 툴 연동 포함
- `runner.py` : 에이전트 실행 및 이벤트 스트리밍, 각 단계별 상세 이벤트 정보 출력
- `__init__.py` : 파이썬 패키지로 폴더 지정

## 예제 실행

gcloud 명령어를 통해서 Google Cloud 실행 환경 로그인 설정합니다.

```
gcloud auth application-default login
```

**02-conversations** 폴더에서 아래 명령어를 실행하세요.

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