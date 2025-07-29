# ADK 런타임 에이전트 예제 - ADK 런타임 이해하기

이 폴더는 ADK(Agent Development Kit) 프레임워크를 활용해 서브 에이전트와 에이전트 툴을 사용한 고급 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다.   
이 예제는 Runner class 사용법에 대해서 설명합니다. 이 처리 방식은 adk web 형태로 실행하는 방식이 아닌 API를 통해서 실행하는 방식으로 실제 프로젝트에서 presentation layer 에서 호출하는 형태입니다. 결국 Production 환경에서 customized 된 UI에서 Runner를 사용해서 호출을 하게 됩니다. 

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

`.env` 파일은 현재 폴더의 `상위 폴더(01-agent)` 에 위치해야 합니다.  환경파일내 들어갈 내용은 아래 URL을 참고하세요.    
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model 

아래 환경설정은 기업에서 `Vertex AI`기반에서 ADK를 사용할때 적용되는 예제입니다.    

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 를 참고해서 변경.
GOOGLE_CLOUD_LOCATION="global"                  # Global Endpoint 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 현재 Gemini 최신 버전.
```

참고로 `AI Studio`를 사용하는 일반 사용자 버전은 아래와 같이 GOOGLE_API_KEY 를 셋팅해야 합니다.  

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
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

루트 에이전트는 ADK `Agent` 클래스를 사용해 정의되며, 해당 Agent는 아래와 같이 sub_agent를 포함합니다.
아래 sub agent는 root_agent 에 의해서 사용자의 질문이 분석이 되고, 그 질문에 맞는 sub agent가 호출이 됩니다.

```
    agent = Agent(
        name = "root_agent",
        model = os.getenv("MODEL"),
        description = "사용자 질의에 대한 질문에 답변하는 에이전트",
        instruction = INSTRUCTION,
        sub_agents = [positive_critic, negative_critic],
    ) 
```

## 예제 실행
### 1. google.adk.runners.Runner 클래스를 통해서 실행

gcloud 명령어를 통해서 Google Cloud 실행 환경 로그인 설정합니다.

```
gcloud auth application-default login
```

```
adk_workshop/adk/01-agent$ uv run -m runtime.runner
```

또는 web browser를 통해서 실행.
```
ai_agent/adk/01-agent$ adk web
```

## 라이선스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.