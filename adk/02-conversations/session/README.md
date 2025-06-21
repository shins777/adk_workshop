# ADK 세션 대화 에이전트 - Session

이 폴더는 ADK(Agent Development Kit) 프레임워크를 활용해 세션 인식 대화형 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다. 이 에이전트는 Google 검색을 통해 사용자 질문에 답변하며, 여러 세션 백엔드를 지원하면서 상호작용 내내 세션 상태를 유지합니다.

세션 대화 에이전트의 주요 특징:
- 자체 지식과 실시간 Google 검색 결과를 활용해 사용자 질문에 답변
- 여러 번의 사용자 상호작용 동안 세션 상태와 기록 유지
- 인메모리, SQLite 데이터베이스, Vertex AI 세션 백엔드 지원
- 각 턴 이후 상세 세션 속성과 이벤트 출력

---

## .env 예시

`.env` 파일을 상위 폴더(예: `adk/02-conversations/`)에 위치시키세요. 예시:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-project-id
PROJECT_NUMBER=your-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
AGENT_ENGINE_ID=your-agent-engine-id  # vertexai 세션 타입에서만 필요
```

## 폴더 구조

```
adk/02-conversations/session/
├── __init__.py
├── agent.py
├── main.py
├── runner.py
└── README.md
```

- `agent.py`  
  에이전트 정의, 지시문 템플릿 및 Google 검색 툴 연동 포함
- `runner.py`  
  에이전트 실행 및 세션 관리 스크립트
- `main.py`  
  메인 실행 파일
- `__init__.py`  
  파이썬 패키지로 폴더 지정
- `README.md`  
  문서 파일(본 파일)

---

## 실행 스크립트 (`runner.py`)

- 에이전트를 비동기적으로 실행하여 세션 인식 대화 루프를 수행
- 기존 세션 확인 후 계속하거나 새로 생성
- 사용자 입력을 프롬프트하고, 에이전트에 전송하며, 에이전트의 응답 출력
- 각 턴 이후 세션 속성과 이벤트 출력

---

## 메인 스크립트 (`main.py`)

- 에이전트 실행을 위한 진입점
- `--type` 인수를 통해 세션 백엔드 선택 (`in_memory`, `database`, `vertexai`)
- 적절한 세션 서비스 설정
- 사용자 지정 앱 이름, 사용자 ID 및 세션 ID로 세션 인식 대화 루프 실행

```
uv run -m session.main --type <session_type> --app_name <app_name> --user_id <user_id> --session_id <session_id>
```
사용 가능한 세션 타입 : in_memory, database, vertexai

### 사용 예시

#### 1. 타입이 in_memory인 경우

```
uv run -m session.main --type in_memory --app_name Search_Assistant --user_id forusone --session_id session_id_01
```
#### 2. 타입이 database인 경우
```
uv run -m session.main --type database --app_name Search_Assistant --user_id forusone --session_id session_id_01
```

현재 버그가 있습니다 : https://github.com/google/adk-python/issues/885  
향후 수정될 예정입니다. (2025년 6월 1일 기준)

```
sqlalchemy.exc.StatementError: (builtins.TypeError) Object of type GroundingMetadata is not JSON serializable
```

#### 3. 타입이 vertexai인 경우
에이전트 엔진에 세션을 저장하려면 먼저 에이전트 엔진을 구성하고 ID를 .env 파일에 추가해야 합니다.
```
AGENT_ENGINE_ID = "17699933548393804800"
```

그런 다음, GCP에 로그인하여 RAG 엔진에 접근합니다. 다음 명령어를 사용하세요.
```
gcloud auth application-default login
```
로그인 후, 다음 명령어를 실행합니다. 

```
uv run -m session.main --type vertexai --app_name Search_Assistant --user_id forusone --session_id session_id_01
```
---

## 라이센스

이 프로젝트는 Apache License 2.0에 따라 라이센스가 부여됩니다.


