# ADK 02-Conversations 예제

이 디렉토리는 Agent Development Kit(ADK)를 활용한 고급 대화형 에이전트 예제를 포함하고 있습니다. 각 하위 폴더는 세션 관리, 메모리, 이벤트 스트리밍, 상태 기반 에이전트 설계 등 다양한 접근 방식을 보여줍니다.

## 배경
### 세션, 이벤트, 상태

<img src="https://github.com/ForusOne/adk_agent/blob/main/images/session_state_events.png?raw=true" alt="drawing" width="600"/>

## 하위 폴더 개요

### 1. `event/` — 이벤트 기반 대화 에이전트

- Google 검색을 활용해 사용자 질문에 답변하고 구조화된 응답 제공
- 대화의 각 단계별 상세 이벤트 정보 스트리밍
- 자세한 내용은 [`event/README.md`](./event/README.md) 참고

### 2. `memory/` — 메모리 기반 대화 에이전트

- 검색 에이전트와 리콜 에이전트를 결합해 정보 저장 및 검색 시연
- 인메모리 및 Vertex AI RAG 코퍼스 메모리 백엔드 지원
- 자세한 내용은 [`memory/README.md`](./memory/README.md) 참고

### 3. `session/` — 세션 인식 대화 에이전트

- 세션 관리 시연, 여러 턴과 세션에 걸친 대화 지속 가능
- 인메모리, 데이터베이스, Vertex AI 세션 백엔드 지원
- 자세한 내용은 [`session/README.md`](./session/README.md) 참고

### 4. `state/` — 상태 기반 대화 에이전트

- 암시적/명시적 상태 관리를 통해 대화 중 상태 추적 및 갱신
- 출력 키와 이벤트를 활용한 세션 상태 관리 시연
- 자세한 내용은 [`state/README.md`](./state/README.md) 참고

## 시작하기

1. 필요에 따라 하위 폴더(`event`, `memory`, `session`, `state`)를 선택하세요.
2. 각 폴더의 README에서 구체적인 설정 및 사용법을 확인하세요.
3. `.env` 파일을 상위 폴더에 위치시키세요.
4. 해당 예제에 권장되는 명령어로 에이전트를 실행하세요.

---

자세한 내용은 각 하위 폴더의 README 파일을 참조하세요.
