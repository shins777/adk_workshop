# 상태 기반 대화 예제 (ADK)

## 예제 개요
이 폴더는 ADK 프레임워크를 활용해 State 기반 대화형 에이전트를 구축하는 방법을 보여줍니다. 이를 통해 고급 컨텍스트 및 흐름 제어가 가능합니다. 이 예제는 Session 내에서 state의 상태를 어떻게 변경하고 활용하는지에 대한 예제입니다.

## .env 설정.

`.env` 파일은 현재 폴더의 `상위 폴더(02-conversations)` 에 위치해야 합니다.  환경파일내 들어갈 내용은 아래 URL을 참고하세요.    
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

## 소스코드 실행 방법

gcloud 명령어를 통해서 Google Cloud 실행 환경 로그인 설정합니다.

```
gcloud auth application-default login
```

### 1. output_key 테스트
output_key는 세션내에서 간단하게 사용할 수 있는 상태를 표시하는 예약된 keyword 입니다.
일반적으로 멀티턴 환경에서 마지막 turn 에 대한 정보를 가지고 있는 state 입니다.

```
adk_workshop/adk/02-conversations$ uv run -m state.output_key --app_name ai_assist --user_id forus
```
### 2. Session 내에서 State를 변경하는 테스트
일반적으로 세션 내에서의 state에 대한 변경은 이벤트를 생성해서 append 하므로써 state를 변경할 수 있습니다.
```
await session_service.append_event(session, system_event)
```

해당 예제를 실행하는 방법은 아래와 같습니다.
```
adk_workshop/adk/02-conversations$ uv run -m state.state_change --app_name ai_assist --user_id forus 
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.