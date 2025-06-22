# MCP 클라이언트 파일 브라우저 에이전트 예제 (ADK)

이 폴더는 ADK(Agent Development Kit)에서 Model Context Protocol(MCP)을 활용하여 파일 시스템을 탐색하고 관리할 수 있는 에이전트 예제를 제공합니다.

## 주요 파일 안내
- `agent.py` : MCPToolset을 활용해 지정 폴더 내 파일을 관리하는 LlmAgent의 메인 코드입니다.
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
```

## 실행 방법
아래 명령어로 예제를 실행할 수 있습니다.

```
adk web
```
테스트 할때는 질문은 "현재 폴더내의 정보를 검색해주세요." 라고해주세요. 

## 예제 기능
- 지정한 폴더 내 파일 목록 조회, 파일 읽기 등 파일 시스템 관리 작업을 MCP 서버와 연동하여 수행할 수 있습니다.
- npx와 @modelcontextprotocol/server-filesystem을 활용해 MCP 서버에 연결합니다.

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.