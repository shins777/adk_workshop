# ADK 01-Agent 예제

이 디렉토리는 Agent Development Kit(ADK)를 활용한 에이전트 구현 예제를 포함하고 있습니다. 각 하위 폴더는 기본 설정부터 고급 런타임, 검색 기능이 포함된 에이전트까지 다양한 구축 방식을 보여줍니다.

## ADK 컴포넌트
아래 이미지는 ADK의 주요 컴포넌트를 설명합니다.
![adk component](https://github.com/ForusOne/adk_agent/blob/main/images/adk_components.png?raw=true)

## 에이전트 계층 구조
ADK는 **하나의 프로세스** 내에서 멀티 에이전트 시스템을 구성할 수 있는 프레임워크입니다. 여러 서브 에이전트와 툴을 조합해 멀티 에이전트 시스템을 구현할 수 있지만, 모든 처리는 단일 프로세스 내에서 모놀리식하게 이루어집니다.
![Agent Hierarchy](https://github.com/ForusOne/adk_agent/blob/main/images/multi-agent.png?raw=true)

## 하위 폴더 개요

### 1. `basic/` — 기본 에이전트 예제
간단한 ADK 에이전트 정의 및 실행 예제.

### 2. `runtime/` — 런타임 에이전트 예제
루트 에이전트와 긍정/부정 크리틱 서브 에이전트, 선택적 에이전트 툴 통합 등 고급 예제.

### 3. `search/` — 검색 에이전트 예제
Google 검색을 활용하여 사용자 쿼리에 답변하고, 출처 참조와 함께 최신 정보를 제공하는 에이전트.


## .env 설정.
환경파일내 들어갈 내용은 아래 URL을 참고하세요.    
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

## 시작하기

1. 필요에 따라 `basic`, `runtime` 또는 `search` 하위 폴더 중 하나를 선택합니다.
2. 해당 하위 폴더의 README 파일을 검토하여 특정 설정 및 사용 지침을 확인합니다.
3. 위에 설명된 대로 상위 폴더에 `.env` 파일을 배치합니다.
4. 해당 예제에 권장되는 명령어로 에이전트를 실행합니다.

자세한 정보는 각 하위 폴더의 개별 README 파일을 참조하십시오.

## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.