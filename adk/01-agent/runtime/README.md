# ADK 런타임 에이전트 예제 - ADK 런타임 이해하기

이 폴더는 ADK(Agent Development Kit) 프레임워크를 활용해 서브 에이전트와 에이전트 툴을 사용한 고급 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다. 특히 Runner class 사용법에 대해서 설명합니다. 

## 배경

### ADK 런타임의 이벤트 루프
아래 이미지는 ADK 런타임에서 가장 중요한 개념인 이벤트 루프를 설명합니다. 이 이벤트 루프 메커니즘은 파이썬의 비동기 이벤트 루프와 유사합니다.
![event loop](https://google.github.io/adk-docs/assets/event-loop.png)
이미지 출처: https://google.github.io/adk-docs/runtime/#core-idea-the-event-loop

### 호출 흐름

![invocation flow](https://google.github.io/adk-docs/assets/invocation-flow.png)
이미지 출처: https://google.github.io/adk-docs/runtime/#how-it-works-a-simplified-invocation

## 개요
`runtime` 에이전트 예제는 다음을 보여줍니다:
- 긍정 및 부정 평가를 위한 서브 에이전트를 포함하는 루트 에이전트 정의
- 선택적으로 에이전트 툴을 사용해 서브 에이전트 래핑
- 환경 변수로 설정값 불러오기
- Runner class 를 활용하여 실행.

## .env 설정.

`.env` 파일은 현재 runtime 폴더의 **상위 폴더(01-agent)**에 위치해야 합니다.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-gcp-project-id
PROJECT_NUMBER=your-gcp-project-number
LOCATION=us-central1
MODEL=gemini-2.5-flash
```

## 파일 구조
```
adk/01-agent/runtime/
├── __init__.py
├── agent.py
├── runner.py
├── sub_agent.py
└── README.md
```

- `agent.py` :서브 에이전트 및 에이전트 툴 연동을 포함한 루트 에이전트의 빌드 및 설정 코드를 포함합니다.
- `runner.py` : 사용자 입력 및 에이전트 응답 처리를 위한 대화 루프 실행 스크립트를 제공합니다.
- `sub_agent.py` : 긍정 및 부정 크리틱 서브 에이전트를 정의합니다.
- `__init__.py` : 폴더를 파이썬 패키지로 지정합니다.

## 작동 방식

루트 에이전트는 ADK `Agent` 클래스를 사용해 정의됩니다. 두 가지 모드로 설정할 수 있습니다:
- **서브 에이전트 모드:** 에이전트가 크리틱 작업을 `positive_critic` 및 `negative_critic` 서브 에이전트에 위임합니다.
- **에이전트 툴 모드:** 에이전트가 `AgentTool` 래퍼를 사용해 서브 에이전트를 호출 가능한 툴로 노출합니다.

에이전트의 지시문은 다음을 안내합니다:
- 사용자 질문의 의도 정리
- 긍정 또는 부정 크리틱에 적절한 서브 에이전트/툴 사용
- 항상 사용자가 질문한 언어와 동일한 언어로 답변

## 예제 실행
```
ai_agent/adk/01-agent$ uv run -m runtime.runner
```

## 라이선스

이 프로젝트는 Apache License 2.0을 따릅니다.