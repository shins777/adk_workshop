# ADK 툴 개요

## 예제 개요
이 디렉토리는 ADK(Agent Development Kit) 에이전트에 다양한 종류의 툴을 통합하는 예제를 포함하고 있습니다. 각 하위 폴더는 내장 툴, 함수형 툴, LangChain 툴, MCP 툴 등 다양한 통합 방식을 보여줍니다. 실제 데이터, 웹 검색, 코드 실행, 외부 시스템 연동 등 에이전트의 기능 확장에 참고하세요.

## 환경 설정
이 폴더의 `.env` 파일에 아래와 같이 키를 설정하세요.

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=your_location
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
RAG_CORPUS=your_rag_corpus
DATASTORE_ID=your_datastore_id
STOCK_API_KEY=your_stock_api_key
TAVILY_API_KEY=your_tavily_api_key
```

각 하위 폴더별 추가 요구사항은 해당 폴더를 참고하세요.

## 소스코드 실행 방법
- 각 하위 폴더의 에이전트 코드와 안내를 참고하세요.
- 예시 (내장 툴):
  ```bash
  uv run python built-in/code_execution/agent.py
  ```
- 예시 (함수형 툴):
  ```bash
  uv run python function/single_call/agent.py
  ```
- 예시 (LangChain 툴):
  ```bash
  uv run python langchain/tavily_search/agent.py
  ```
- 예시 (MCP 툴):
  ```bash
  uv run python mcp/client_file_browser/agent.py
  ```

## 라이센스 정보
이 프로젝트는 Apache License 2.0에 따라 라이센스가 부여됩니다. 자세한 내용은 [LICENSE](../LICENSE) 파일을 참조하세요.