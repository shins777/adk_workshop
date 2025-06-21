# ADK 에이전트 엔진 배포 예제

## 1. 예제 개요
이 폴더는 Agent Development Kit(ADK)와 Vertex AI Agent Engine을 활용해 멀티 에이전트 파이프라인을 구축, 관리, 배포, 실행하는 방법을 보여줍니다. 로컬 테스트, Vertex AI 배포, 원격 실행을 위한 스크립트와 유틸리티를 제공합니다. SequentialAgent를 활용해 여러 서브 에이전트(긍정, 부정, 리뷰 크리틱)를 오케스트레이션하고, Google Cloud Vertex AI에 에이전트를 배포 및 관리하는 방법을 시연합니다.

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
1. GCP 로그인
```
gcloud auth application-default login
```
2. GCP 인증:
   ```bash
   gcloud auth application-default login
   ```
3. 터미널에서 `adk/06-deploy/` 디렉토리로 이동
4. 에이전트를 로컬에서 실행하거나 Vertex AI에 배포:
   - 로컬 테스트 및 배포:
     ```bash
     uv run -m agent_engine.deploy --query 'What is Generative AI?' --agent_name my_agent --user_id user1 --session_id 12345
     ```
   - 배포된 에이전트를 원격으로 실행:
     ```bash
     uv run -m agent_engine.run --resource_name <resource_name> --user_id user1 --session_id 12345 --query 'What is Generative AI?'
     ```
     참고: resource_name에는 프로젝트 번호를 사용해야 합니다.
     예시: uv run -m agent_engine.run --resource_name projects/721521243942/locations/us-central1/reasoningEngines/2417773292921290752 --user_id user1 --session_id 12345 --query 'What is Generative AI?'
     

     ```
5. Interact with the agent via the terminal prompt or remote API.

## 4. License Information
This project is licensed under the Apache License 2.0.
