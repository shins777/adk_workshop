# ADK 메모리 대화 에이전트 - Memory

이 폴더는 ADK(Agent Development Kit) 프레임워크를 활용해 메모리 기능을 갖춘 대화형 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다. 이 에이전트는 Google 검색을 통해 사용자 질문에 답변할 수 있으며, 메모리 서비스를 통해 이전 세션의 정보를 기억하고 불러올 수 있습니다.

메모리 대화 에이전트의 주요 특징:
- 실시간 Google 검색과 메모리 리콜을 활용해 사용자 질문에 답변
- 완료된 세션을 메모리에 저장하고 이후에 불러오기 가능
- 인메모리 및 Vertex AI RAG 코퍼스 메모리 백엔드 지원
- 검색, 저장, 리콜의 다단계 워크플로우 시연

## .env 예시

`.env` 파일은 **상위 폴더**에 위치해야 합니다.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-gcp-project-id
PROJECT_NUMBER=your-gcp-project-number
LOCATION=us-central1
MODEL=gemini-2.5-flash

# RAG 엔진 메모리 저장용
CORPUS_ID = "55253532324830177280" <-- 본인 RAG Engine 코퍼스 ID로 변경
```

## 폴더 구조

```
adk/02-conversations/memory/
├── __init__.py
├── agent.py
├── main.py
├── runner.py
└── README.md
```

- `agent.py`  
  에이전트 정의, 지시문 템플릿 및 Google 검색/메모리 연동 포함
- `main.py`  
  메인 실행 파일
- `runner.py`  
  에이전트 실행 및 메모리 관리 스크립트
- `__init__.py`  
  파이썬 패키지로 폴더 지정
- `README.md`  
  문서 파일(본 파일)

## 에이전트 세부사항 (`agent.py`)

- **`search_agent`**
  - `google_search` 도구 사용
  - 구조화된 응답 형식 준수 (질문, 출처 정보, 답변)
- **`recall_agent`**
  - 메모리에서 정보 검색을 위해 `load_memory` 도구 사용
  - 이전에 저장된 세션을 기반으로 답변

---

## 실행기 스크립트 (`runner.py`)

- 워크플로우 조정:
  1. 전용 세션에서 검색 에이전트를 실행하고 세션을 메모리에 저장
  2. 새 세션에서 리콜 에이전트를 실행하여 메모리에서 정보 검색
- 검색 및 리콜 단계 모두에 대한 사용자 입력 처리
- 에이전트 응답 및 이벤트 세부정보 출력

---

## 메인 스크립트 (`main.py`)

- 워크플로우 실행을 위한 진입점
- `--memory_type` 인수를 통해 메모리 유형 선택 (`in_memory` 또는 `rag_corpus`)
- 세션 및 메모리 서비스 설정
- 사용자 지정 앱 이름 및 사용자 ID로 조정된 워크플로우 실행

### 사용 예시

#### 1. 명령줄에서 실행
```
uv run memory.main --memory_type [in_memory|rag_corpus]
```

####  2. 메모리 유형으로 `in_memory` 사용
```
uv run -m memory.main --memory_type in_memory 
```

####  3. 메모리 유형으로 `rag_corpus` 사용

먼저, Vertex AI에서 RAG 엔진을 설정해야 합니다.
```
CORPUS_ID = "552535334330177280"
```
그런 다음, GCP에 로그인하여 RAG 엔진에 접근합니다. 다음 명령어를 사용하세요.
```
gcloud auth application-default login
```
로그인 후, 다음 명령어를 실행합니다. 
```
uv run -m memory.main --memory_type rag_corpus 
```
RAG 엔진에 접근할 수 없는 경우, 다음과 같은 오류 메시지가 표시될 수 있습니다.
```
RuntimeError: ('Failed in indexing the RagFile due to: ', {'code': 403, 'message': "Permission 'aiplatform.ragFiles.upload' denied on resource '//aiplatform.googleapis.com/projects/ai-forus/locations/us-central1/ragCorpora/552535232177280' (or it may not exist)."
```

RuntimeError: ('Failed in indexing the RagFile due to: ', {'code': 7, 'message': "failed to list files, folders: ['vertex_rag_service_upload_rag_file_drop_target_prod_us_central1/881d20c5-c76e-42d6-b3fe-e81e18e26ea1'], files: [], error: 403 GET https://storage.googleapis.com/storage/v1/b/vertex_rag_service_upload_rag_file_drop_target_prod_us_central1?projection=noAcl&prettyPrint=false: gke-agent-us-central1@rag-rental-prod-400e3dd3.iam.gserviceaccount.com does not have storage.buckets.get access to the Google Cloud Storage bucket. Permission 'storage.buckets.get' denied on resource (or it may not exist)."})
