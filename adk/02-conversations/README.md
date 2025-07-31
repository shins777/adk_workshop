# ADK 02-conversations 전체 가이드

이 디렉토리는 ADK(Agent Development Kit)에서 대화 흐름, 세션, 메모리, 이벤트, 상태 관리 등 다양한 대화형 에이전트 기능을 제공합니다. 각 서브 폴더는 대화의 주요 구성요소별로 분리되어 있으며, 아래에 각 기능의 개요와 환경설정 방법을 안내합니다.

## 폴더 및 기능 요약

### _memory
메모리 기반 대화 에이전트 예제. Google 검색, 메모리 리콜, 세션 정보 저장/불러오기, 인메모리 및 Vertex AI RAG 메모리 백엔드 지원 등 다양한 메모리 기능을 제공합니다.

### event
이벤트 기반 대화 에이전트 예제. 사용자와 에이전트 간 커뮤니케이션 과정에서 발생하는 다양한 이벤트 정보를 활용하여 제어 및 결과 표현이 가능합니다.

### session
세션 인식 대화 에이전트 예제. 여러 번의 사용자 상호작용 동안 세션 상태와 기록을 유지하며, 인메모리/SQLite/Vertex AI 세션 백엔드 지원, 각 턴별 상세 정보 및 이벤트 출력 기능을 제공합니다.

### state
상태 기반 대화 에이전트 예제. 세션 내에서 상태(state)의 변화와 활용 방법을 안내하며, 고급 컨텍스트 및 흐름 제어가 가능합니다.

## 공통 환경설정 (.env)
모든 대화 예제는 상위 폴더(02-conversations)에 `.env` 파일을 위치시키고, 각 서브 폴더의 README.md에 안내된 환경 변수(API 키, 프로젝트 정보 등)를 등록해야 합니다.

### 주요 환경 변수 예시
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-gcp-project-id
PROJECT_NUMBER=your-gcp-project-number
LOCATION=us-central1
# 각 예제별 추가 환경 변수는 각 README.md 참고
```

## 참고
각 서브 폴더의 README.md를 참고하여 상세 사용법, 예제 코드, 환경설정 방법을 확인하세요.
