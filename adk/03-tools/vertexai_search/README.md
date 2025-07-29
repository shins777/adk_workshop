# Vertex AI Search 도구 예제 (ADK)

## 예제 개요
이 폴더는 ADK 에이전트와 함께 내장 Vertex AI Search 도구를 활용하여 Vertex AI Search 데이터스토어 기반으로 사용자 질의에 답변하는 방법을 보여줍니다.

## 환경 설정
상위 폴더의 `.env` 파일에 다음 키를 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=your_location

PROJECT_NUMBER=your_project_number
DATASTORE_ID=your_datastore_id
MODEL=your_model_name

```

## 예제 실행 방법
참고: 아래 명령어는 **03-tools/built-in** 폴더에서 실행하세요.

### 1. GCP 로그인(인증)
```
gcloud auth application-default login
```

### 2. 소스 실행
```
ai_agent/adk/03-tools/built-in$ adk web
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.