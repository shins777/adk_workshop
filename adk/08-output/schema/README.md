# Schema 기반 Output 예제

## 예제 개요
이 폴더는 ADK(Agent Development Kit)에서 Pydantic 기반의 output schema를 활용하여, 에이전트가 구조화된 형태로 답변을 생성하는 방법을 보여줍니다.  
검색 결과, 질의 의도, 답변 등 명확한 필드를 갖는 JSON 스키마를 통해 일관된 결과를 제공합니다.

## .env 설정.

`.env` 파일은 현재 runtime 폴더의 **상위 폴더(08-output)**에 위치해야 합니다.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-gcp-project-id
PROJECT_NUMBER=your-gcp-project-number
LOCATION=us-central1
MODEL=gemini-2.5-flash
```

## 주요 파일 안내
- `agent.py`: output_schema로 `SearchResult`를 지정한 검색 에이전트 정의
- `schema.py`: 검색 결과의 구조를 정의하는 Pydantic 모델(`SearchResult`) 및 JSON 스키마 예시 포함
- `__init__.py`: 패키지 초기화 파일

## 실행 방법

```
08-output# adk web

```

## 예제 Output 스키마
```json
{
  "query": "검색어 또는 질문",
  "intention": "질문 의도",
  "result": "검색 결과 또는 답변"
}
```

## 예제 기능
- 사용자의 질의와 의도를 명확히 분리하여 구조화된 답변 제공
- output_schema를 활용한 일관된 JSON 결과 반환
- 다양한 검색/질의 응답 시나리오에 확장 가능

## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
