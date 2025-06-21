# ADK 콜백 에이전트 예제

이 디렉토리는 ADK(Agent Development Kit)에서 콜백 메커니즘을 활용하여 에이전트, 모델, 툴의 동작을 제어하는 예제를 포함하고 있습니다. 각 하위 폴더는 다양한 콜백 시나리오를 보여주며, 에이전트 워크플로우의 여러 단계에서 실행을 가로채거나 수정, 차단할 수 있습니다.

---

## 1. 예제 개요

- **agent_callback/**: 에이전트 레벨 콜백을 통해 메인 에이전트 로직 전후로 처리. 고급 제어, 맞춤 응답, 상태 기반 대화 흐름 구현 가능.
- **model_callback/**: 모델(LLM) 레벨 콜백을 통해 LLM 호출 전후로 처리. 키워드 필터링, 콘텐츠 검열, 맞춤 흐름 구현 가능.
- **tool_callback/**: 툴 실행 전후로 콜백 처리. 인자/결과 조작 및 맞춤 툴 흐름 구현 가능.

각 예제는 메인 에이전트/모델/툴 로직 실행 전후에 흐름을 가로채고 수정하는 방법을 보여주며, 고급 제어와 커스터마이징이 가능합니다.

---

## 2. 환경 설정
상위 폴더(`adk/05-callback/`)에 아래와 같이 `.env` 파일을 생성하세요. (값은 필요에 따라 수정)

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-project-id
PROJECT_NUMBER=your-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
```

---

## 3. 소스코드 실행 방법
1. `pyproject.toml` 또는 `requirements.txt`에 명시된 의존성 설치
2. 터미널에서 `adk/05-callback/` 디렉토리로 이동
3. ADK 러너 또는 제공된 스크립트로 에이전트 실행. 예시:
   ```bash
   adk web
   ```
   또는 특정 콜백 예제 실행:
   ```bash
   uv run -m agent_callback.runner
   uv run -m model_callback.runner
   uv run -m tool_callback.runner
   ```
4. 웹 인터페이스나 터미널 프롬프트를 통해 에이전트와 상호작용

---

## 4. 라이센스 정보
이 프로젝트는 Apache License 2.0에 따라 라이센스가 부여됩니다.
