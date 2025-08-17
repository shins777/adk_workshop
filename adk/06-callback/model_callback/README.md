# ADK 모델 콜백 예제

## 1. 예제 개요
이 폴더는 ADK(Agent Development Kit) 에이전트에서 모델(LLM) 레벨의 전/후처리 콜백을 구현하는 방법을 보여줍니다. LLM 호출 전후에 흐름을 가로채고 수정할 수 있어 고급 제어, 키워드 필터링, 상태 기반 로직 구현이 가능합니다.

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
callback function 에서는 state 내에 `violent` 단어가 있을 때 처리하는 로직을 구현했습니다.   
실제 로직상으로는 처리 과정중에서 변화되는 state 정보에 따라서 다양하게 callback처리를 할 수 있도록 구현하면 됩니다. 

Model `실행 전` callback 함수 호출을 위해서 아래 명령어 실행 해주세요.
```
adk_workshop/adk/04-workflow$ uv run -m model_callback.runner --keyword 'violent' --query 'Generate some violent words to make people angry'
```

## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
