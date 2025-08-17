# ADK 에이전트 엔진 배포 예제

## 예제 개요
이 폴더는 Agent Development Kit(ADK)와 Vertex AI Agent Engine을 활용해 멀티 에이전트 파이프라인을 구축, 관리, 배포, 실행하는 방법을 보여줍니다. 로컬 테스트, Vertex AI 배포, 원격 실행을 위한 스크립트와 유틸리티를 제공합니다. SequentialAgent를 활용해 여러 서브 에이전트(긍정, 부정, 리뷰 크리틱)를 오케스트레이션하고, Google Cloud Vertex AI에 에이전트를 배포 및 관리하는 방법을 시연합니다.

## .env 환경 설정.

상위 폴더(`adk/05-callback/`)에 아래와 같이 `.env` 파일을 생성하세요. 

환경파일내 들어갈 내용은 아래 URL을 참고하세요.    
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model 

아래 환경설정은 기업에서 `Vertex AI`기반에서 ADK를 사용할때 적용되는 예제입니다.    

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 를 참고해서 변경.
GOOGLE_CLOUD_LOCATION="us-central1"                  # Global Endpoint 사용, 이 위치는 Agent Engine 의 위치도 같이 활용. 
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

AI Agent 디플로이 명령어를 실행합니다. 디플로이가 정상적으로 되면 Vertex AI 콘솔상에서 생성된 AI Agent를 확인 할수 있습니다.
```
adk_workshop/adk/06-deploy$ uv run -m agent_engine.deploy --agent_name 'adk_agent_20250730'
```

디플로이가 정상적으로 처리가 되면 아래와 같은 명령어로 원격의 AI Agent 에 접속해서 쿼리를 합니다. 
```
adk_workshop/adk/06-deploy$ uv run -m agent_engine.run --engine_id 6733822624872267776 --user_id forus --query 'What is the Generative AI?'
```

## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
