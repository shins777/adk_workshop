# ADK 01-Agent 예제

이 디렉토리는 Agent Development Kit(ADK)를 활용한 에이전트 구현 예제를 포함하고 있습니다. 각 하위 폴더는 기본 설정부터 고급 런타임, 검색 기능이 포함된 에이전트까지 다양한 구축 방식을 보여줍니다.

## ADK 컴포넌트
아래 이미지는 ADK의 주요 컴포넌트를 설명합니다.
![adk component](https://github.com/ForusOne/adk_agent/blob/main/images/adk_components.png?raw=true)

## 에이전트 계층 구조
ADK는 **하나의 프로세스** 내에서 멀티 에이전트 시스템을 구성할 수 있는 프레임워크입니다. 여러 서브 에이전트와 툴을 조합해 멀티 에이전트 시스템을 구현할 수 있지만, 모든 처리는 단일 프로세스 내에서 모놀리식하게 이루어집니다.
![Agent Hierarchy](https://github.com/ForusOne/adk_agent/blob/main/images/multi-agent.png?raw=true)

## 하위 폴더 개요

### 1. `basic/` — 기본 에이전트 예제

간단한 ADK 에이전트 정의 및 실행 예제.

- **주요 특징:**
  - 맞춤 지시문 및 설명
  - 환경 변수 기반 설정
  - ADK `Agent` 객체 인스턴스화 및 반환
  - 예시 `.env` 구성 제공
- **실행 방법:**
  - `.env` 파일을 상위 폴더에 위치
  - `01-agent` 디렉토리에서 `adk web` 실행

자세한 내용은 [`basic/README.md`](./basic/README.md) 참고.

---

### 2. `runtime/` — 런타임 에이전트 예제

루트 에이전트와 긍정/부정 크리틱 서브 에이전트, 선택적 에이전트 툴 통합 등 고급 예제.

- **주요 특징:**
  - 루트 에이전트와 서브 에이전트 구조
  - 크리틱 작업용 에이전트 툴
  - 대화형 루프 실행 스크립트
  - 예시 `.env` 구성 제공
- **실행 방법:**
  - `.env` 파일을 상위 폴더에 위치
  - 제공된 실행기 스크립트를 사용한 대화형 세션

자세한 내용은 [`runtime/README.md`](./runtime/README.md) 참고.

---

### 3. `search/` — 검색 에이전트 예제

Google 검색을 활용하여 사용자 쿼리에 답변하고, 출처 참조와 함께 최신 정보를 제공하는 에이전트.

- **주요 특징:**
  - Google 검색 툴 통합
  - 질문, 출처 및 응답 형식으로 답변 포맷팅
  - 예시 `.env` 구성 제공
- **실행 방법:**
  - `.env` 파일을 상위 폴더에 위치
  - `01-agent` 디렉토리에서 `adk web` 실행

자세한 내용은 [`search/README.md`](./search/README.md) 참고.

---

## 공통 요구 사항

- Python 3.8 이상
- `python-dotenv`
- ADK 및 Google ADK 라이브러리 (반드시 `google.adk`가 설치 및 구성되어 있어야 함)
- Google API 키 및 프로젝트 구성 (.env 예제는 각 하위 폴더에 있음)

---

## 예시 `.env` 파일
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE 
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY 

PROJECT_ID=your-project-id 
PROJECT_NUMBER=your-project-number 
LOCATION=us-central1 
MODEL=gemini-2.0-flash
```

## 시작하기

1. 필요에 따라 `basic`, `runtime` 또는 `search` 하위 폴더 중 하나를 선택합니다.
2. 해당 하위 폴더의 README 파일을 검토하여 특정 설정 및 사용 지침을 확인합니다.
3. 위에 설명된 대로 상위 폴더에 `.env` 파일을 배치합니다.
4. 해당 예제에 권장되는 명령어로 에이전트를 실행합니다.

---

자세한 정보는 각 하위 폴더의 개별 README 파일을 참조하십시오.



## 라이센스

이 프로젝트는 Apache License 2.0에 따라 라이센스가 부여됩니다.