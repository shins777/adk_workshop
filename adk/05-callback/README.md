# ADK 05-callback 전체 가이드

이 디렉토리는 ADK(Agent Development Kit)에서 에이전트, 모델(LLM), 툴 실행 전후에 콜백을 활용하는 다양한 예제와 구현 방법을 제공합니다. 각 서브 폴더는 특정 콜백 유형별로 분리되어 있으며, 아래에 각 기능의 개요와 환경설정 방법을 안내합니다.

## 폴더 및 기능 요약

### agent_callback
에이전트 실행 전/후에 콜백을 적용하는 예제입니다. 에이전트의 상태에 따라 실행을 건너뛰거나, 맞춤 응답을 반환하는 등 고급 제어가 가능합니다.

### model_callback
모델(LLM) 실행 전/후에 콜백을 적용하는 예제입니다. LLM 호출 전후에 흐름을 제어하거나, 키워드 필터링, 상태 기반 로직 구현 등이 가능합니다.

### tool_callback
툴 실행 전/후에 콜백을 적용하는 예제입니다. 입력 및 결과 조작, 맞춤 툴 흐름 구현 등 고급 제어가 가능합니다.

## 공통 환경설정 (.env)
모든 콜백 예제는 상위 폴더(05-callback)에 `.env` 파일을 위치시키고, 아래 URL의 가이드를 참고하여 환경설정을 진행해야 합니다.

https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

각 콜백별 환경설정 예시는 각 서브 폴더의 README.md에 상세히 안내되어 있습니다. 주요 환경 변수 예시는 다음과 같습니다:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 참고
GOOGLE_CLOUD_LOCATION="global"                  # Global Endpoint 사용
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 최신 Gemini 버전
# 각 콜백별 추가 환경 변수는 각 README.md 참고
```

## 참고
각 서브 폴더의 README.md를 참고하여 상세 사용법, 예제 코드, 환경설정 방법을 확인하세요.

## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
