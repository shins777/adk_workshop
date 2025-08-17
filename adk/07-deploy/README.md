# ADK 06-deploy 전체 가이드

이 디렉토리는 ADK(Agent Development Kit)에서 에이전트 엔진 및 배포 관련 기능을 제공합니다. 각 서브 폴더는 에이전트 엔진의 구축, 관리, 배포, 운영에 필요한 예제와 스크립트를 포함하고 있습니다.

## 폴더 및 기능 요약

### agent_engine
ADK와 Vertex AI Agent Engine을 활용하여 멀티 에이전트 파이프라인을 구축, 관리, 배포, 실행하는 방법을 제공합니다. 로컬 테스트, Vertex AI 배포, 원격 실행을 위한 스크립트와 유틸리티가 포함되어 있습니다.

### operation
Agent Engine을 다양한 형태로 생성하고 업데이트하는 예제입니다. 배포 후 운영, 실행, 관리에 필요한 스크립트와 유틸리티가 포함되어 있습니다.

## 공통 환경설정 (.env)
모든 배포 예제는 상위 폴더(06-deploy)에 `.env` 파일을 위치시키고, 아래 URL의 가이드를 참고하여 환경설정을 진행해야 합니다.

https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

각 배포별 환경설정 예시는 각 서브 폴더의 README.md에 상세히 안내되어 있습니다. 주요 환경 변수 예시는 다음과 같습니다:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 참고
GOOGLE_CLOUD_LOCATION="us-central1"             # Agent Engine 위치에 맞게 설정
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 최신 Gemini 버전
# 각 배포별 추가 환경 변수는 각 README.md 참고
```

## 참고
각 서브 폴더의 README.md를 참고하여 상세 사용법, 예제 코드, 환경설정 방법을 확인하세요.


## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.