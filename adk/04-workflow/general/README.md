# ADK 일반 워크플로우 에이전트 예제

## 1. 예제 개요
이 폴더는 Agent Development Kit(ADK)를 활용한 일반 워크플로우 에이전트 예제를 제공합니다. 이 에이전트는 다양한 비즈니스 시나리오에 맞게 확장하거나 커스터마이즈할 수 있는 구성 가능한 워크플로우를 통해 사용자 입력을 처리합니다. ADK에서 다단계 또는 멀티 에이전트 워크플로우를 어떻게 구조화할 수 있는지 이해하는 데 적합한 예제입니다.

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
   uv run -m general.runner
   ```
4. 웹 인터페이스 또는 터미널 프롬프트에서 에이전트와 상호작용할 수 있습니다.

## 4. 라이선스 안내
이 프로젝트는 Apache License 2.0 하에 배포됩니다.
