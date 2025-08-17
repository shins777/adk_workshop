
# ADK 04-workflow 전체 가이드

비즈니스 시나리오에 따라 다양한 방식으로 멀티 에이전트와 툴을 조합할 수 있으며, 세 가지 유형의 에이전트를 사용할 수 있습니다.

![agent types](https://google.github.io/adk-docs/assets/agent-types.png)
이미지 출처 : https://google.github.io/adk-docs/agents/#agents

## 폴더별 워크플로우 예제

### 1. custom
- **목적**: 긍정/부정/종합 리뷰 비평 에이전트(CriticAgent) 워크플로우 예제
- **주요 파일**: agent.py, critic.py, sub_agent.py
- **설명**: 각 서브 에이전트가 긍정, 부정, 종합 리뷰를 수행하며, 결과를 종합해 전체 워크플로우를 완성합니다.

### 2. general
- **목적**: 일반 워크플로우 에이전트 예제
- **주요 파일**: agent.py, sub_agent.py
- **설명**: 다양한 비즈니스 시나리오에 맞게 워크플로우를 확장하거나 커스터마이즈할 수 있습니다.

### 3. loop
- **목적**: 반복(Loop) 워크플로우 에이전트 예제
- **주요 파일**: agent.py, sub_agent.py
- **설명**: 사용자 입력을 반복적으로 처리하며, 반복 개선, 다회 질의, 다단계 작업 등에 적합합니다.

### 4. parallel
- **목적**: 병렬(Parallel) 워크플로우 에이전트 예제
- **주요 파일**: agent.py, sub_agent.py
- **설명**: 여러 작업 또는 서브 에이전트를 병렬로 처리하여 빠른 완료 또는 멀티 에이전트 협업이 가능합니다.

### 5. sequencial
- **목적**: 순차(Sequencial) 워크플로우 에이전트 예제
- **주요 파일**: agent.py, sub_agent.py
- **설명**: 여러 단계 또는 서브 에이전트를 정해진 순서대로 처리하는 시나리오에 적합합니다.

## 환경 설정 (.env)
상위 폴더(`adk/04-workflow/`)에 `.env` 파일을 생성하여 아래와 같이 환경을 설정하세요.

- Vertex AI 기반 예시:
  ```
  GOOGLE_GENAI_USE_VERTEXAI=TRUE
  GOOGLE_CLOUD_PROJECT="ai-hangsik"
  GOOGLE_CLOUD_LOCATION="global"
  GOOGLE_GENAI_MODEL = "gemini-2.5-flash"
  ```
- AI Studio(일반 사용자) 예시:
  ```
  GOOGLE_GENAI_USE_VERTEXAI=FALSE
  GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
  ```

자세한 환경설정은 [ADK 공식 문서](https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model)를 참고하세요.

## 실행 방법
Google Cloud 환경 인증:
```
gcloud auth application-default login
```
서버/에이전트 도구 예제 실행:
```
adk_workshop/adk/04-workflow$ adk web
```
각 워크플로우 폴더의 README.md 및 소스코드를 참고하여, 목적에 맞는 에이전트/서버를 실행하세요.

## 라이선스 안내
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
