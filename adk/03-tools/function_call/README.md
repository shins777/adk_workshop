# 다중 함수형 툴 예제 (ADK)

이 폴더는 ADK(Agent Development Kit)에서 여러 함수형 툴(예: 환율, 주가 등)을 연동하는 방법을 보여줍니다.

## .env 설정.

`.env` 파일은 현재 폴더의 `상위 폴더(03-tools)` 에 위치해야 합니다.  환경파일 내 들어갈 내용은 아래 URL을 참고하세요.   

https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model 

아래 환경설정은 기업에서 `Vertex AI`기반에서 ADK를 사용할때 적용되는 예제입니다.    

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 를 참고해서 변경.
GOOGLE_CLOUD_LOCATION="global"                  # Global Endpoint 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 현재 Gemini 최신 버전.

# Stock API keys
STOCK_API_KEY = "STOCK_API_KEY"

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

UI 에서 function_call 선택 후 아래와 같이 명령어 실행합니다.
```
최근 원달러 환율과 구글 주식 가격을 알려주세요.
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
