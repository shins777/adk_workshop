# ADK 07-output 전체 가이드

이 디렉토리는 ADK(Agent Development Kit)에서 출력 결과의 구조화 및 스키마 기반 결과 생성 예제를 제공합니다. 각 서브 폴더는 다양한 출력 방식과 스키마(Pydantic 등)를 활용한 결과 생성 방법을 안내합니다.

## 폴더 및 기능 요약

### schema
Pydantic 기반 output schema를 활용하여 에이전트가 구조화된 형태(JSON 등)로 답변을 생성하는 예제입니다. 검색 결과, 질의 의도, 답변 등 명확한 필드를 갖는 스키마를 통해 일관된 결과를 제공합니다.

## 공통 환경설정 (.env)
모든 출력 예제는 상위 폴더(07-output)에 `.env` 파일을 위치시키고, 아래 URL의 가이드를 참고하여 환경설정을 진행해야 합니다.

https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

각 예제별 환경설정 예시는 각 서브 폴더의 README.md에 상세히 안내되어 있습니다. 주요 환경 변수 예시는 다음과 같습니다:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 참고
GOOGLE_CLOUD_LOCATION="global"                  # Global Endpoint 사용
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 최신 Gemini 버전
# 각 예제별 추가 환경 변수는 각 README.md 참고
```

## 참고
각 서브 폴더의 README.md를 참고하여 상세 사용법, 예제 코드, 환경설정 방법을 확인하세요.
