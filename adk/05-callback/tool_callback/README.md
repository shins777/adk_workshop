# ADK 툴 콜백 예제

이 폴더는 ADK(Agent Development Kit)에서 툴 실행 전후에 콜백을 활용하는 방법을 보여줍니다. 인자 및 결과 조작, 맞춤 툴 흐름 구현 등 고급 제어가 가능합니다.

## 환경 설정
상위 폴더(`adk/05-callback/`)에 아래와 같이 `.env` 파일을 생성하세요. (값은 필요에 따라 수정)

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-project-id
PROJECT_NUMBER=your-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
```

## 실행 방법
1. 의존성 설치
2. `adk/05-callback/` 디렉토리로 이동
3. ADK 러너 또는 제공된 스크립트로 에이전트 실행
   ```bash
   adk web
   ```
   또는 러너 스크립트가 제공된 경우:
   ```bash
   uv run -m tool_callback.runner
   ```
4. 웹 인터페이스나 터미널 프롬프트를 통해 에이전트와 상호작용

## 라이센스 정보
이 프로젝트는 Apache License 2.0에 따라 라이센스가 부여됩니다.
