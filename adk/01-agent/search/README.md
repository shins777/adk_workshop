# ADK 검색 에이전트 - Google Search Tool 활용

이 폴더는 Agent Development Kit(ADK)와 Google Search 연동을 활용한 에이전트 구현 예제를 제공합니다.  
이 에이전트는 자체 지식과 실시간 검색 결과를 모두 활용해 사용자 질문에 답변합니다. 이 예제를 통해서 간단한 Tool 사용방법을 이해할 수 있습니다.

## .env 설정.

`.env` 파일은 현재 runtime 폴더의 `상위 폴더(01-agent)` 에 위치해야 합니다.  환경파일내 들어갈 내용은 아래 URL을 참고하세요.    
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

## 예제 실행

gcloud 명령어를 통해서 Google Cloud 실행 환경 로그인 설정합니다.

```
gcloud auth application-default login
```

**01-agent** 폴더에서 아래 명령어를 실행하세요. 실행 하면 UI 접속 URL을 통해서 단위테스트를 할 수 있습니다.

```
ai_agent/adk/01-agent$ adk web
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.