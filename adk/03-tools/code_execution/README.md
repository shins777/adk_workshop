# ADK Built-in Code Execution 에이전트

이 폴더는 코드 실행 기능이 내장된 ADK(에이전트 개발 키트) 에이전트를 빌드하고 운영하는 방법을 보여줍니다. 에이전트는 Python 코드를 작성하고 실행하여 수학 표현식을 풀고, 코드와 결과를 모두 일반 텍스트로 반환합니다.

코드 실행 에이전트는 다음과 같은 기능을 제공합니다.
- 사용자로부터 수학 표현식을 입력받습니다.
- 표현식을 풀기 위한 Python 코드를 작성하고 실행합니다.
- 코드와 결과를 모두 일반 텍스트로 반환합니다.
- 사용자 입력과 동일한 언어로 응답합니다.

## .env 설정.

`.env` 파일은 현재 runtime 폴더의 `상위 폴더(03-tools)` 에 위치해야 합니다.  환경파일내 들어갈 내용은 아래 URL을 참고하세요.    
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
adk/03-tools/code_execution/
├── __init__.py
├── agent.py
├── README.md
```


## 소스 코드 실행 방법
gcloud 명령어를 통해서 Google Cloud 실행 환경 로그인 설정합니다.
```
gcloud auth application-default login
```

아래 명령어로 서브 에이전트 도구 예제를 실행할 수 있습니다:
```
ai_agent/adk/03-tools$ adk web
```

UI 에서 code_execution 선택후 아래와 같이 명령어 실행합니다.
```
1 에서 100까지 소수를 구하여 합하는 프로그램을 작성 후 실행해주세요.
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
