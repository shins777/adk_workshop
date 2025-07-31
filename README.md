# ADK Workshop 전체 가이드

이 프로젝트는 Google Agent Development Kit(ADK)와 A2A(Agent-to-Agent) 프로토콜, 다양한 AI/LLM 에이전트 예제, 배포 및 워크플로우, 콜백, 모델 연동 등 실전 환경에서 활용 가능한 모든 구성요소를 포함합니다.

## 폴더 구조 및 주요 기능

- **a2a/** : A2A 프로토콜 및 ADK 연동 예제. 에이전트 간 통신, 메시지 변환, Google Search 등 다양한 A2A 기능 구현.
- **adk/** : ADK 기반의 모든 에이전트, 툴, 워크플로우, 콜백, 배포, 모델 연동 예제. 각 하위 폴더별로 기능별 예제와 진입점 README.md가 제공됩니다.
- **images/** : ADK 구조, 에이전트 비교, 세션/상태/이벤트 등 주요 아키텍처 다이어그램 및 시각 자료.
- **notebooks/** : ADK 및 각종 에이전트/워크플로우/엔진/세션/툴 예제의 Jupyter Notebook. 실습 및 테스트에 활용.

## 주요 하위 폴더 안내 (adk/)

- **01-agent/** : 기본 에이전트 및 런타임, 서브에이전트, 검색 등 다양한 에이전트 예제.
- **02-conversations/** : 세션, 메모리, 이벤트, 상태 관리 등 대화 흐름 예제.
- **03-tools/** : 다양한 툴(코드 실행, 함수 호출, 검색, RAG 등) 연동 예제.
- **04-workflow/** : 커스텀/일반/루프/병렬/순차 워크플로우 예제.
- **05-callback/** : 에이전트/모델/툴 실행 전후 콜백 예제.
- **06-deploy/** : 에이전트 엔진 구축, 배포, 운영 예제.
- **07-output/** : 출력 스키마 및 결과 예제.
- **08-model/** : 외부 및 로컬 LLM 모델 연동 예제(LiteLLM, Ollama 등).

## 설치 및 환경설정

1. **Git Clone**
   ```
   git clone https://github.com/shins777/adk_workshop.git
   ```
2. **uv 패키지 매니저 설치**
   - Rust 기반의 빠르고 편리한 Python 패키지 매니저
   - 참고: https://github.com/astral-sh/uv

3. **.env 환경설정**
   - 각 폴더별 README.md의 환경 변수 예시 참고
   - ADK 공식 가이드: https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

## 참고 및 진입점

- 각 폴더의 README.md에서 상세 예제, 실행 방법, 환경설정, 코드 설명을 확인하세요.
- 주요 구조/흐름/엔진/세션/에이전트 비교 등은 images/ 폴더의 다이어그램 참고.
- 실습 및 테스트는 notebooks/ 폴더의 Jupyter Notebook 활용.
