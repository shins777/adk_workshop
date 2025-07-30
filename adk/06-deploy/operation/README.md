# ADK Agent 배포 예제

## 예제 개요
이 예제는 Agent Engine을 여러가지 형태로 생성하고 업데이트 하는 예제입니다. 

## .env 환경 설정.

상위 폴더(`adk/06-deploy/`)에 아래와 같이 `.env` 파일을 생성하세요. 

환경파일내 들어갈 내용은 아래 URL을 참고하세요.    
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model 

아래 환경설정은 기업에서 `Vertex AI`기반에서 ADK를 사용할때 적용되는 예제입니다.    

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 를 참고해서 변경.
GOOGLE_CLOUD_LOCATION="us-central1"             # Global Endpoint 사용, 이 위치는 Agent Engine 의 위치도 같이 활용. 
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 현재 Gemini 최신 버전.

AGENT_ENGINE_PROJECT_NUMBER = "70000000000"
AGENT_ENGINE_BUCKET="gs://agent-0417"           # ADK로 만들어진 Agent의 아티팩트(소스코드등)가 저장되는 GCP 의 GCS 위치. 

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

AI Agent 를 생성하는 명령어를 실행합니다. 이 예제는 로직이 없는 형태의 Agent Engine을 만드는 방식입니다.   
디플로이가 정상적으로 되면 Vertex AI 콘솔상에서 생성된 AI Agent를 확인 할수 있습니다.
```
adk_workshop/adk/06-deploy$ uv run -m operation.create --display_name adk_agent_20250728
```


다음 예제는 이미 배포된 Agent Engine을 새롭게 ADK 로 만든것으로 Update 하는 예제입니다. 
```
adk_workshop/adk/06-deploy$ uv run -m operation.update --agent_engine_id 4971736494105427968
```

디플로이가 정상적으로 처리가 되면 아래와 같은 명령어로 원격의 AI Agent 에 접속해서 쿼리를 합니다. 
```
adk_workshop/adk/06-deploy$ uv run -m operation.execute --agent_engine_id 1384109217509539840 --user_id forus --query 'What is the Generative AI?'
```

## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.

