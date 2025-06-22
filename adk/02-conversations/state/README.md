# 상태 기반 대화 예제 (ADK)

## 예제 개요
이 폴더는 ADK 프레임워크를 활용해 State 기반 대화형 에이전트를 구축하는 방법을 보여줍니다. 이를 통해 고급 컨텍스트 및 흐름 제어가 가능합니다. 이 예제는 Session 내에서 state의 상태를 어떻게 변경하고 활용하는지에 대한 예제입니다.

## .env 환경 설정
상위 폴더의 `.env` 파일에 아래와 같이 키를 설정하세요.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## 소스코드 실행 방법

### 1. output_key 테스트
output_key는 세션내에서 간단하게 사용할 수 있는 상태를 표시하는 예약된 keyword 입니다.
일반적으로 멀티턴 환경에서 마지막 turn 에 대한 정보를 가지고 있는 state 입니다.

```
uv run -m state.output_key --app_name <app_name> --user_id <user_id> 
```
### 2. Session 내에서 State를 변경하는 테스트
일반적으로 세션 내에서의 state에 대한 변경은 이벤트를 생성해서 append 하므로써 state를 변경할 수 있습니다.
```
await session_service.append_event(session, system_event)
```

해당 예제를 실행하는 방법은 아래와 같습니다.
```
uv run -m state.state_change --app_name <app_name> --user_id <user_id> 
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.