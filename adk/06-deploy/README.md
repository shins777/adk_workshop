# ADK 배포 예제

## 1. 예제 개요
이 디렉토리는 Agent Development Kit(ADK)와 Vertex AI Agent Engine을 활용해 멀티 에이전트 파이프라인을 배포, 관리, 실행하는 고급 예제를 포함하고 있습니다. 각 하위 폴더는 다양한 배포 및 세션 관리 시나리오를 보여주며, 로컬 및 원격 실행, GCP 연동, 에이전트 엔진 관리 스크립트를 제공합니다.

- **agent_engine/**: SequentialAgent와 Vertex AI Agent Engine을 활용해 멀티 에이전트 파이프라인을 구축, 배포, 실행하는 방법 시연
- **agent_session/**: 세션 관리, 배포, 업데이트, 대화 연속성 유지 등 다양한 시나리오 시연

## 2. 환경 설정
상위 폴더(`adk/06-deploy/`)에 아래와 같이 `.env` 파일을 생성하세요. (값은 필요에 따라 수정)

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-gcp-project-id
PROJECT_NUMBER=your-gcp-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
STAGING_BUCKET=gs://your-bucket-name
```

## 3. 소스코드 실행 방법
1. `pyproject.toml` 또는 `requirements.txt`에 명시된 의존성 설치
2. GCP 인증:
   ```bash
   gcloud auth application-default login
   ```
3. 터미널에서 `adk/06-deploy/` 디렉토리로 이동
4. 각 하위 폴더의 README.md 파일을 참고해 시나리오별 배포, 업데이트, 실행 방법 확인

## 4. 라이선스 정보
이 프로젝트는 Apache License 2.0을 따릅니다.
