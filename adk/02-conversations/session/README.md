# ADK 세션 대화 에이전트 - Session, Event, State

이 폴더는 ADK(Agent Development Kit) 프레임워크를 활용해 세션 인식 대화형 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다. 사용자와의 다양한 커뮤니케이션을 하기 위해서는 Session을 사용할 수 있습니다. 이 에이전트는 Google 검색을 통해 사용자 질문에 답변하며, 여러 세션 백엔드를 지원하면서 상호작용 내내 세션 상태를 유지합니다. 

세션 대화 에이전트의 주요 특징:
- 자체 지식과 실시간 Google 검색 결과를 활용해 사용자 질문에 답변
- 여러 번의 사용자 상호작용 동안 세션 상태와 기록 유지
- 인메모리, SQLite 데이터베이스, Vertex AI 세션 백엔드 지원
- 각 턴 이후 상세 세션 속성과 이벤트 출력

## .env 설정.

`.env` 파일은 현재 runtime 폴더의 `상위 폴더(02-conversations)` 에 위치해야 합니다.  환경파일내 들어갈 내용은 아래 URL을 참고하세요.    
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model 

아래 환경설정은 기업에서 `Vertex AI`기반에서 ADK를 사용할때 적용되는 예제입니다.    
참고 : Gemini 의 Endpoint location 과 Agent Engine 의 Location 은 다르게 설정할 수 있습니다. 

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 를 참고해서 변경.
GOOGLE_CLOUD_LOCATION="global"              # Global Endpoint 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 현재 Gemini 최신 버전.

AGENT_ENGINE_ID=your-agent-engine-id            # vertexai 세션 타입에서만 필요
AGENT_ENGINE_LOCATION = "us-central1"            # vertexai 세션 타입에서만 필요

```

참고로 `AI Studio`를 사용하는 일반 사용자 버전은 아래와 같이 GOOGLE_API_KEY 를 셋팅해야 합니다.  

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
AGENT_ENGINE_ID=your-agent-engine-id            # vertexai 세션 타입에서만 필요
```



## 폴더 구조

```
adk/02-conversations/session/
├── __init__.py
├── agent.py
├── runner.py
└── README.md
```

- `agent.py` : 에이전트 정의, 지시문 템플릿 및 Google 검색 툴 연동 포함
- `runner.py` : 에이전트 실행 및 세션 관리 스크립트
- `__init__.py` :  파이썬 패키지로 폴더 지정

## 예제 실행

gcloud 명령어를 통해서 Google Cloud 실행 환경 로그인 설정합니다.

```
gcloud auth application-default login
```

본 예제 실행 방법은 아래와 같이 크게 3가지 타입으로 세션을 설정할 수 있습니다. 

```
uv run -m session.runner --type <session_type> --app_name <app_name> --user_id <user_id>
```
사용 가능한 세션 타입 : in_memory, database, vertexai

테스트 하는 방법은 세션이 유지되는 동안(초기 실행하면 자동으로 세션이 생성) 기존 History(멀티턴)에 대화했던 정보를 참고로 질문이나 기타 답변의 내용을 참고할수 있습니다.
참고로 세션 타입을 database 또는 vertexai 를 사용할 경우에는 해당 프로세스가 종료된 이후에 재 기동했을 때 동일한 세션 정보(app name, user id, session id) 를 갖는다면 해당 정보를 기반으로 연계된 멀티턴을 사용할 수 있습니다.

참고:  
* 세션을 생성하거나 조회할때 Session id 정보를 사용할수 없음, session id 는 현재 자동으로 생성됨.
* 결국 세션 생성, 조회는 app_name, user_id 를 사용해서 처리.

### 1. 타입이 in_memory인 경우

이 방법은 세션 정보가 메모리에만 존재하기 때문에 프로세스 종료후 모든 세션 정보가 삭제됩니다.
결국 프로세스 기동 중에만 사용이 가능한 세션입니다. 

```
uv run -m session.runner --type in_memory --app_name ai_assist --user_id forus
```
### 2. 타입이 database인 경우

이 방법은 세션 정보를 database에 저장하는 경우입니다. 
데이터베이스는 관계형 데이터 베이스(e.g., PostgreSQL, MySQL, SQLite)를 사용하여 해당 세선 정보를 테이블에 저장할 수 있습니다.

```
uv run -m session.runner --type database --app_name ai_assist --user_id forus
```
테스트가 정상적으로 처리되면 파일로 adk_database.db 파일이 생성되고 해당 정보를 확인 할수가 있습니다. 해당 파일은 SQLite 로써 VS code 에서 Extension을 설치하면 해당 파일 내용을 확인 할 수 있습니다.

### 3. 타입이 vertexai인 경우

이 방법은 Vertex AI의 Agent Engine과 같은 물리적인 서버를 활용하는 방법입니다. 
Agent Engine 은 독립적으로 기동되는 서버이며, AI Agent를 포팅해서 처리하도록 설계된 Cloud Run기반의 시스템입니다. 
Agent Engine에 세션을 저장하려면 먼저 Agent Engine 을 구성하고 ID 와 해당 Location을 아래와 같이 환경파일인 .env 파일에 추가해야 합니다.

```
AGENT_ENGINE_ID = "1769934533233804800"    # Vertex AI에 배포된 Agent Engine ID.
AGENT_ENGINE_LOCATION = "us-central"       # Vertex AI에 배포된 Agent Engine의 Locatoin.

```

테스트 방법은 아래와 같습니다. 테스트시에는 아래의 app_name, user_id 을 동일하게 주어야 해당 정보를 가지고 동일한 세션 정보를 가져오게 됩니다.

```
uv run -m session.runner --type vertexai --app_name ai_assist --user_id forus

```
테스트가 정상적으로 되었다면 Vertex AI 에서 Agent Engine 화면에서 session 이 forus 로 생성되어 있는것을 볼수 있습니다. 명시적으로 지우지 않으면 해당 정보는 계속 유지가 되고, 위의 app name 와 user id 로 동일하게 접속을 할 경우에는 기존 저장된 세션 정보를 context로 계속 사용할 수 있습니다. 


## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
