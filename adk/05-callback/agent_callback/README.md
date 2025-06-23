# ADK 에이전트 콜백 예제

## 1. 예제 개요
이 폴더는 ADK(Agent Development Kit) 에이전트에서 에이전트 레벨의 전/후처리 콜백을 구현하는 방법을 보여줍니다. 메인 에이전트 로직 실행 전후에 흐름을 가로채고 수정할 수 있어 고급 제어, 맞춤 응답, 상태 기반 로직 구현이 가능합니다.

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

## 3. 소스코드 실행 방법
1. `pyproject.toml` 또는 `requirements.txt`에 명시된 의존성 설치
2. 터미널에서 `adk/05-callback/` 디렉토리로 이동
3. ADK 러너 또는 제공된 스크립트로 에이전트 실행. 예시:
   ```bash
   adk web
   ```
   또는 러너 스크립트가 제공된 경우:
   ```bash
   uv run -m agent_callback.runner --command [skip_agent|check_response] --query 'Explain about Generative AI' 
   ```

   
4. 웹 인터페이스 또는 터미널 프롬프트로 에이전트와 상호작용

## 4. 라이선스 정보
이 프로젝트는 Apache License 2.0을 따릅니다.
