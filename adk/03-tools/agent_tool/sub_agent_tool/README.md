# 서브 에이전트 도구 예제 (ADK)
ADK 에서는 Sub Agent를 도구로 등록해서 사용할 수 있습니다. Agent를 도구로 사용하는 경우와 sub agent 로 사용하는 경우는 아래와 같이 큰 차이가 있습니다.
 * Agent를 도구로 사용하는 경우 : 다른 Tool 사용하는 경우와 동일하게 모든 출력에 대한 제어권을 호출한 Agent가 가져감. 
 * Agent를 Sub Agent로 사용하는 경우 : 호출한 Agent는 호출되는 sub agent 에게 해당 Agent 출력에 대한 사항을 위임함.

## 예제 개요
이 폴더는 ADK 에이전트 내에서 서브 에이전트를 도구로 활용하여 모듈화되고 조합 가능한 워크플로우를 구현하는 방법을 보여줍니다.

## 환경 설정
상위 폴더의 `.env` 파일에 다음 키를 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## 소스 코드 실행 방법
아래 명령어로 서브 에이전트 도구 예제를 실행할 수 있습니다:

```
adk web
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.