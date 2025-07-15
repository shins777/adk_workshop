# ADK MCP 도구 개요

이 디렉터리에는 Model Context Protocol(MCP)을 활용하여 파일 시스템 및 커스텀 서버 등 외부 시스템과 연동하는 ADK(Agent Development Kit) 에이전트 예제가 포함되어 있습니다. 각 하위 폴더는 ADK 에이전트에서 MCP 기반 도구를 사용하는 다양한 방식을 보여줍니다.

---

## 하위 폴더 안내

### 1. `client_file_browser/` — MCP 클라이언트 파일 브라우저 에이전트
- MCP를 이용해 지정된 폴더 내 파일을 관리하고 탐색할 수 있도록 도와줍니다.
- `@modelcontextprotocol/server-filesystem`을 통해 파일 시스템 서버에 연결합니다.
- 자세한 내용은 [`client_file_browser/README.md`](./client_file_browser/README.md) 참고.

### 2. `server_exchange_rate/` — MCP 서버 환율 정보 에이전트
- 커스텀 Python MCP 서버에 연결하여 `get_exchange_rate` 도구로 환율 정보를 조회합니다.
- 최신 금융 데이터를 위한 Python 기반 MCP 서버와 연동합니다.
- 자세한 내용은 [`server_exchange_rate/README.md`](./server_exchange_rate/README.md) 참고.

---

## 시작하기

1. 목적에 맞는 하위 폴더(`client_file_browser` 또는 `server_exchange_rate`)를 선택하세요.
2. 각 하위 폴더의 README를 참고해 환경 설정 및 사용법을 확인하세요.
3. 상위 폴더에 `.env` 파일을 위 환경 변수 예시대로 배치하세요.
4. 예제별 권장 명령어로 에이전트를 실행하세요.

---

# MCP 도구 예제 (ADK)

## 예제 개요
이 폴더는 ADK 에이전트에서 Model Context Protocol(MCP) 도구를 활용해 파일 시스템 및 커스텀 서버와 연동하는 방법을 보여줍니다.

- `client_file_browser/`: MCP 기반 파일 브라우저 에이전트
- `server_exchange_rate/`: 커스텀 MCP 서버 기반 환율 정보 에이전트

## 환경 설정
상위 폴더의 `.env` 파일에 다음 키를 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## 소스 코드 실행 방법
각 하위 폴더의 에이전트 코드와 실행법을 참고하세요. 예시:

```bash
mcp/adk web
```

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.