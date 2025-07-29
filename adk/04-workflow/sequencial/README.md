# ADK 순차 워크플로우 에이전트 예제

## 1. 예제 개요
이 폴더는 Agent Development Kit(ADK)를 활용한 순차 워크플로우 에이전트 예제를 제공합니다. 이 에이전트는 사용자 입력을 여러 단계 또는 서브 에이전트를 통해 정해진 순서대로 처리합니다. 단계별 데이터 처리, 단계적 추론 등 반드시 순서대로 작업이 진행되어야 하는 시나리오에 적합한 예제입니다.

## .env 환경 설정.

상위 폴더(`adk/04-workflow/`)에 아래와 같이 `.env` 파일을 생성하세요. 

환경파일내 들어갈 내용은 아래 URL을 참고하세요.    
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

## 소스 코드 실행 방법
gcloud 명령어를 통해서 Google Cloud 실행 환경 로그인 설정합니다.
```
gcloud auth application-default login
```

아래 명령어로 서브 에이전트 도구 예제를 실행할 수 있습니다:
```
adk_workshop/adk/04-workflow$ adk web
```

## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.