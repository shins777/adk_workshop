# Schema 기반 Output 예제

## 예제 개요
이 폴더는 ADK(Agent Development Kit)에서 Pydantic 기반의 output schema를 활용하여, 에이전트가 구조화된 형태로 답변을 생성하는 방법을 보여줍니다.  
검색 결과, 질의 의도, 답변 등 명확한 필드를 갖는 JSON 스키마를 통해 일관된 결과를 제공합니다.

## .env 환경 설정.

상위 폴더(`adk/07-output/`)에 아래와 같이 `.env` 파일을 생성하세요. 

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

## 소스 코드 실행 방법
gcloud 명령어를 통해서 Google Cloud 실행 환경 로그인 설정합니다.
```
gcloud auth application-default login
```

**07-output** 폴더에서 아래 명령어를 실행하세요. 실행 하면 UI 접속 URL을 통해서 단위테스트를 할 수 있습니다.

```
adk_workshop/adk/07-output$ adk web
```

### 예제 Output 스키마
```json
{
  "query": "검색어 또는 질문",
  "intention": "질문 의도",
  "result": "검색 결과 또는 답변"
}
```

### 예제 기능
- 사용자의 질의와 의도를 명확히 분리하여 구조화된 답변 제공
- output_schema를 활용한 일관된 JSON 결과 반환
- 다양한 검색/질의 응답 시나리오에 확장 가능

## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
