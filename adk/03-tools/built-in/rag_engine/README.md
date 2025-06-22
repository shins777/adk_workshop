# RAG 엔진 도구 예제 (ADK)

## 예제 개요
이 폴더는 ADK 에이전트와 함께 내장 RAG(Retrieval-Augmented Generation) 엔진 도구를 활용하여 Vertex AI 기반 코퍼스 검색을 수행하는 방법을 보여줍니다.

## 환경 설정
상위 폴더의 `.env` 파일에 다음 키를 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
RAG_CORPUS=your_rag_corpus_id
```

## 소스 코드 실행 방법
RAG 엔진 에이전트를 실행하려면 아래와 같이 하세요:

## 예제 실행 방법
참고: 아래 명령어는 **03-tools/built-in** 폴더에서 실행하세요.

```
ai_agent/adk/03-tools/built-in$ adk web
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.