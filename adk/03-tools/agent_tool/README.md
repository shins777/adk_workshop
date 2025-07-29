# 서브 에이전트 도구 예제 (ADK)
ADK 에서는 Sub Agent를 도구로 등록해서 사용할 수 있습니다. Agent를 도구로 사용하는 경우와 sub agent 로 사용하는 경우는 아래와 같이 큰 차이가 있습니다.
 * Agent를 도구로 사용하는 경우 : 다른 Tool 사용하는 경우와 동일하게 모든 출력에 대한 제어권을 호출한 Agent가 가져감. 
   * 이 경우에는 등록된 Tool들을 모두 호출이 가능함.
 * Agent를 Sub Agent로 사용하는 경우 : 호출한 Agent는 호출되는 sub agent 에게 해당 Agent 출력에 대한 사항을 위임함.
   * 이 경우 특정 Sub Agent 하나만 호출됨. 

## 예제 개요
이 폴더는 ADK 에이전트 내에서 서브 에이전트를 도구로 활용하여 모듈화되고 조합 가능한 워크플로우를 구현하는 방법을 보여줍니다.

## .env 설정.

`.env` 파일은 현재 폴더의 `상위 폴더(03-tools)` 에 위치해야 합니다.  환경파일 내 들어갈 내용은 아래 URL을 참고하세요.   

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
adk_workshop/adk/03-tools$ adk web
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.