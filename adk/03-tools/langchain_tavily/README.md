# Tavily Search 툴 예제 (ADK)

이 폴더는 ADK(Agent Development Kit)에서 LangChain 기반 Tavily Search 툴과 환율 조회 기능을 연동하여, 웹 검색 및 환율 정보를 질의할 수 있는 에이전트 예제를 제공합니다.

## 주요 파일 안내
- `agent.py` : Tavily Search 및 환율 조회 도구가 포함된 ADK 에이전트의 메인 코드입니다.
- `function.py` : 환율 정보를 조회하는 함수형 도구가 정의되어 있습니다.
- `__init__.py` : 에이전트 모듈을 임포트합니다.

## 환경 설정
상위 폴더의 `.env` 파일에 다음과 같은 키를 설정하세요.

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
TAVILY_API_KEY=your_tavily_api_key
```

## 실행 방법
아래 명령어로 예제를 실행할 수 있습니다.

```
adk web
```

## 예제 기능
- **환율 정보 질의**: 기준 통화, 대상 통화, 날짜를 입력하면 해당 환율 정보를 반환합니다.
- **웹 검색 질의**: 환율 질문이 아닌 경우 Tavily Search를 통해 웹 검색 결과와 참고 출처, 답변을 제공합니다.

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
