# ADK 세션 대화 에이전트 - Session, Event, State

이 폴더는 ADK(Agent Development Kit) 프레임워크를 활용해 세션 인식 대화형 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다. 사용자와의 다양한 커뮤니케이션을 하기 위해서는 Session을 사용할 수 있습니다. 이 에이전트는 Google 검색을 통해 사용자 질문에 답변하며, 여러 세션 백엔드를 지원하면서 상호작용 내내 세션 상태를 유지합니다. 

세션 대화 에이전트의 주요 특징:
- 자체 지식과 실시간 Google 검색 결과를 활용해 사용자 질문에 답변
- 여러 번의 사용자 상호작용 동안 세션 상태와 기록 유지
- 인메모리, SQLite 데이터베이스, Vertex AI 세션 백엔드 지원
- 각 턴 이후 상세 세션 속성과 이벤트 출력

## .env 설정.

`.env` 파일은 현재 runtime 폴더의 **상위 폴더(02-conversations)**에 위치해야 합니다.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-gcp-project-id
PROJECT_NUMBER=your-gcp-project-number
LOCATION=us-central1
MODEL=gemini-2.5-flash

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

- `agent.py` : 에이전트 정의, 지시문 템플릿 및 Google 검색 툴 연동 포함
- `runner.py` : 에이전트 실행 및 세션 관리 스크립트
- `main.py` : 메인 실행 파일
- `__init__.py` :  파이썬 패키지로 폴더 지정


### 1.실행 스크립트 (`runner.py`)

- 에이전트를 비동기적으로 실행하여 세션 인식 대화 루프를 수행
- 기존 세션 확인 후 계속하거나 새로 생성
- 사용자 입력을 프롬프트하고, 에이전트에 전송하며, 에이전트의 응답 출력
- 각 턴 이후 세션 속성과 이벤트 출력

### 2. 메인 스크립트 (`main.py`)
- 에이전트 실행을 위한 진입점
- `--type` 인수를 통해 세션 백엔드 선택 (`in_memory`, `database`, `vertexai`)
- 적절한 세션 서비스 설정
- 사용자 지정 앱 이름, 사용자 ID 및 세션 ID로 세션 인식 대화 루프 실행



### 사용 예시

본 예제 실행 방법은 아래와 같이 크게 3가지 타입으로 세션을 설정할 수 있습니다. 

```
uv run -m session.main --type <session_type> --session_id <session_id>
```
사용 가능한 세션 타입 : in_memory, database, vertexai

테스트 하는 방법은 세션이 유지되는 동안(초기 실행하면 자동으로 세션이 생성) 기존 History(멀티턴)에 대화했던 정보를 참고로 질문이나 기타 답변의 내용을 참고할수 있습니다.
참고로 세션 타입을 database 또는 vertexai 를 사용할 경우에는 해당 프로세스가 종료된 이후에 재 기동했을 때 동일한 세션 정보(app name, user id, session id) 를 갖는다면 해당 정보를 기반으로 연계된 멀티턴을 사용할 수 있습니다.

참고:  
* 세션을 생성하거나 조회할때 Session id 정보를 사용할수 없음, session id 는 현재 자동으로 생성됨.
* 결국 세션 생성, 조회는 app_name, user_id 를 사용해서 처리.

#### 1. 타입이 in_memory인 경우

이 방법은 세션 정보가 메모리에만 존재하기 때문에 프로세스 종료후 모든 세션 정보가 삭제됩니다.
결국 프로세스 기동 중에만 사용이 가능한 세션입니다. 

```
uv run -m session.main --type in_memory --app_name ai_assist --user_id forus
```
#### 2. 타입이 database인 경우

이 방법은 세션 정보를 database에 저장하는 경우입니다. 
데이터베이스는 관계형 데이터 베이스(e.g., PostgreSQL, MySQL, SQLite)를 사용하여 해당 세선 정보를 테이블에 저장할 수 있습니다.

```
uv run -m session.main --type database --app_name ai_assist --user_id forus
```

버그 참고 : 
 * 2025년 6월 1일 기준 버그 : https://github.com/google/adk-python/issues/885  
    ```
    sqlalchemy.exc.StatementError: (builtins.TypeError) Object of type GroundingMetadata is not JSON serializable
    ```

 * 2025년 6월 22일 기준 버그 Fix 되었음 : https://github.com/google/adk-python/commit/bf27f22a9534279b942bb8047d747effc9e7dd7a

#### 3. 타입이 vertexai인 경우

Agent Engine에 물리적인 접근을 위해서 GCP에 아래와 같이 로그인을 해야 합니다. 
GCP 로그인을 위해서 다음 명령어를 사용하세요. 정상적인 접근을 위해서 사용하는 계정은 Agent Engine 을 사용할 수 있는 권한이 있어야 합니다. GCP 권한 설정 부분 참고하세요. 

```
gcloud auth application-default login
```

이 방법은 데이터베이스와 같이 물리적인 서버를 활용하는 방법으로 구글의 Agent Engine 을 사용하는 방법입니다.
Agent Engine에 세션을 저장하려면 먼저 Agent Engine 을 구성하고 ID를 환경파일인 .env 파일에 추가해야 합니다.

```
AGENT_ENGINE_ID = "17699933548393804800"
```

테스트 방법은 아래와 같습니다. 테스트시에는 아래의 app_name, user_id 을 동일하게 주어야 해당 정보를 가지고 동일한 세션 정보를 가져오게 됩니다.

```
uv run -m session.main --type vertexai --app_name ai_assist --user_id forus

```


## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
