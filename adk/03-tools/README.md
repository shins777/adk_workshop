# ADK 03-tools 전체 가이드

이 디렉토리는 ADK(Agent Development Kit)에서 다양한 에이전트 및 도구 기능을 제공하는 서브 모듈들을 포함합니다. 각 서브 폴더는 특정 기능 또는 외부 서비스와의 연동을 담당하며, 아래에 각 도구의 개요와 환경설정 방법을 안내합니다.

## 폴더 및 기능 요약

### agent_tool
서브 에이전트(Sub Agent) 도구 예제. ADK에서 Agent를 도구로 등록하여 활용하는 방법을 제공합니다. Agent와 Sub Agent의 차이 및 활용법, .env 환경설정 예시가 포함되어 있습니다.

### code_execution
ADK 내장 코드 실행 에이전트. Python 코드를 작성·실행하여 수식 표현식 풀이, 결과 반환 등 자동화된 코드 실행 기능을 제공합니다. .env 환경설정 예시가 포함되어 있습니다.

### function_call
다중 함수형 툴 예제. 다양한 함수형 도구(예: 환율, 주가 등)를 연동하는 방법을 안내합니다. .env 환경설정 및 Stock API 키 예시가 포함되어 있습니다.

### google_search
Google Search 도구 예제. ADK 에이전트와 함께 내장 Google Search 도구를 활용하여 실시간 웹 검색 결과로 사용자 질의에 답변하는 방법을 안내합니다. .env 환경설정 예시가 포함되어 있습니다.

### langchain_tavily
Tavily Search 툴 예제. LangChain 기반 Tavily Search 및 환율 조회 기능을 연동하여 웹 검색 및 환율 정보를 질의할 수 있는 예시를 제공합니다. .env 환경설정 및 Tavily API 키 예시가 포함되어 있습니다.

### mcp_client
MCP 클라이언트 파일 브라우저 에이전트 예제. Model Context Protocol(MCP)을 활용하여 파일 시스템을 탐색·관리하는 기능을 제공합니다. .env 환경설정 및 AI Studio용 GOOGLE_API_KEY 안내가 포함되어 있습니다.

### mcp_client_server
MCP 서버 환율 정보 에이전트 예제. 커스텀 Python MCP 서버와 연동하여 실시간 환율 정보를 조회하는 기능을 제공합니다. .env 환경설정 예시가 포함되어 있습니다.

### rag_engine
RAG 엔진 도구 예제. Vertex AI 기반 RAG(Retrieval-Augmented Generation) 엔진을 활용하여 코퍼스 검색을 수행하는 방법을 안내합니다. .env 환경설정 및 RAG_CORPUS 예시가 포함되어 있습니다.

### vertexai_search
Vertex AI Search 도구 예제. Vertex AI Search 데이터스토어 기반으로 사용자 질의에 답변하는 기능을 제공합니다. .env 환경설정 및 VAIS_PROJECT_NUMBER 예시가 포함되어 있습니다.

## 공통 환경설정 (.env)
모든 도구는 상위 폴더(03-tools)에 `.env` 파일을 위치시키고, 아래 URL의 가이드를 참고하여 환경설정을 진행해야 합니다.

https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

각 도구별 환경설정 예시는 각 서브 폴더의 README.md에 상세히 안내되어 있습니다. 주요 환경 변수 예시는 다음과 같습니다:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 참고
GOOGLE_CLOUD_LOCATION="global"                  # Global Endpoint 사용
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 최신 Gemini 버전
# 각 도구별 추가 환경 변수는 각 README.md 참고
```

## 참고
각 서브 폴더의 README.md를 참고하여 상세 사용법, 예제 코드, 환경설정 방법을 확인하세요.

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.