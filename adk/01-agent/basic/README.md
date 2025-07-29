# ADK 기본 에이전트 예제 - ADK의 기본 개념

이 폴더는 ADK(Agent Development Kit) 프레임워크를 활용해 간단한 AI 에이전트를 구축하고 실행하는 방법을 보여줍니다.

## .env 설정.

`.env` 파일은 현재  폴더의 `상위 폴더(01-agent)` 에 위치해야 합니다.  환경파일내 들어갈 내용은 아래 URL을 참고하세요.    
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

## basic 에이전트 파일 구조
```
adk/01-agent/basic/
├── __init__.py
├── agent.py
└── README.md
```

- `agent.py`  : 기본 에이전트의 빌드 및 설정 코드를 포함합니다.
- `__init__.py`  : 폴더를 파이썬 패키지로 지정합니다.


## 예제 실행

gcloud 명령어를 통해서 Google Cloud 실행 환경 로그인 설정합니다.

```
gcloud auth application-default login
```

`01-agent` 폴더에서 아래 명령어를 실행후 adk web 화면에서 테스트를 진행하시면 됩니다. 

```
adk_workshop/adk/01-agent$ adk web
```

## 라이선스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.