# ADK 기본 에이전트 예제 - ADK의 기본 개념

이 폴더는 ADK(Agent Development Kit) 프레임워크를 활용해 간단한 AI 에이전트를 구축하고 실행하는 방법을 보여줍니다.

## 배경

### 에이전트 유형
비즈니스 시나리오에 따라 다양한 방식으로 멀티 에이전트와 툴을 조합할 수 있으며, 세 가지 유형의 에이전트를 사용할 수 있습니다.

![agent types](https://google.github.io/adk-docs/assets/agent-types.png)
이미지 출처 : https://google.github.io/adk-docs/agents/#agents

### 에이전트 비교
아래는 세 가지 에이전트 유형의 비교입니다.
![agent types](https://github.com/ForusOne/adk_agent/blob/main/images/agent_comparison.png?raw=true)
이미지 출처 : https://google.github.io/adk-docs/agents/#choosing-the-right-agent-type

## basic 에이전트 처리 구조.
`basic` 에이전트를 통해서 아래와 같은 순서로 Agent 구성 및 테스트를 진행합니다.
1. 맞춤 지시문과 설명으로 에이전트가 해야 할 일 정의  
2. 환경 변수로 LLM 모델 설정 값 불러오기  
3. "adk web" 명령어로 실행 후 웹상에서 사용자 질문에 답변.  

## .env 설정.

`.env` 파일은 현재 basic 폴더의 **상위 폴더(01-agent)**에 위치해야 합니다.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-gcp-project-id
PROJECT_NUMBER=your-gcp-project-number
LOCATION=us-central1
MODEL=gemini-2.5-flash
```

## basic 에이전트 파일 구조
```
adk/01-agent/basic/
├── __init__.py
├── agent.py
└── README.md
```

- `agent.py`  : 기본 에이전트의 빌드 및 설정 코드를 포함합니다.
- `__init__.py`  : 폴더를 파이썬 패키지로 지정합니다.

---

## 예제 실행
**01-agent** 폴더에서 아래 명령어를 실행후 adk web 화면에서 테스트를 진행하시면 됩니다. 

```
ai_agent/adk/01-agent$ adk web
```

## 라이선스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.