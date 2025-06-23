# ADK 루프 워크플로우 에이전트 예제

## 1. 예제 개요
이 폴더는 Agent Development Kit(ADK)를 활용한 루프 기반 워크플로우 에이전트 예제를 제공합니다. 이 에이전트는 사용자 입력을 반복적으로 처리하며, 반복 개선, 다회 질문, 다단계 작업 등에 적합합니다. 조건이 충족될 때까지 반복적으로 사용자와 상호작용하거나 여러 단계를 수행해야 하는 시나리오에 유용합니다.

## 2. 환경 설정
상위 폴더(`adk/04-workflow/`)에 아래와 같이 `.env` 파일을 생성하세요. (값은 환경에 맞게 수정)

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-project-id
PROJECT_NUMBER=your-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
```

## 3. 실행 방법
1. `pyproject.toml` 또는 `requirements.txt`에 명시된 의존성을 설치하세요.
2. 터미널에서 `adk/04-workflow/` 디렉터리로 이동합니다.
3. ADK 러너 또는 제공된 스크립트로 에이전트를 실행합니다. 예시:
   ```bash
   adk web
   ```
   또는, 러너 스크립트가 제공된 경우:
   ```bash
   uv run -m loop.runner
   ```
4. 웹 인터페이스 또는 터미널 프롬프트에서 에이전트와 상호작용할 수 있습니다.

## 4. 라이선스 안내
이 프로젝트는 Apache License 2.0 하에 배포됩니다.
