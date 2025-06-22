# MCP 서버 환율 정보 에이전트 예제 (ADK)

이 폴더는 ADK(Agent Development Kit)에서 Model Context Protocol(MCP)을 활용하여 커스텀 Python MCP 서버와 연동, 실시간 환율 정보를 조회하는 에이전트 예제를 제공합니다.


## 환경 설정
상위 폴더의 `.env` 파일에 다음과 같은 키를 설정하세요.

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## 주요 파일 안내
- `agent.py` : MCPToolset을 통해 환율 정보를 조회하는 LlmAgent의 메인 코드입니다.
- `exchange_rate_server.py` : 실제 환율 정보를 제공하는 커스텀 MCP 서버(Python) 코드입니다.
- `__init__.py` : 에이전트 모듈을 임포트합니다.

## 실행 방법

```
adk web
```
질문 : 원달러 환율을 알려주세요. 

## 예제 기능
- 사용자의 환율 질의에 대해 MCP 서버와 연동하여 실시간 환율 정보를 제공합니다.
- Frankfurter API를 활용해 다양한 통화 간 환율을 조회할 수 있습니다.

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.