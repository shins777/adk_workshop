# ADK 툴 콜백 예제

이 폴더는 ADK(Agent Development Kit)에서 툴 실행 전후에 콜백을 활용하는 방법을 보여줍니다. 인자 및 결과 조작, 맞춤 툴 흐름 구현 등 고급 제어가 가능합니다.

## .env 환경 설정.

상위 폴더(`adk/05-callback/`)에 아래와 같이 `.env` 파일을 생성하세요. 

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
사용자의 요청이 처리되면 Tool 을 통해서 처리가 되는데, 툴내의 args 정보를 통해서 callback function에서 처리 되는 로직을 구현합니다.
툴을 호출하기 전에 입력된 args 정보들을 수정하고 추가해서 툴이 좀더 더 잘 실행될수 있도록 처리하는 예제입니다. 

Tool `실행 전` callback 함수 호출을 위해서 아래 명령어 실행 해주세요.
```
adk_workshop/adk/04-workflow$ uv run -m tool_callback.runner --query 'What is the capital city of Korea?'
```

## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
