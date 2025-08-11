# Toolbox 에이전트 예제 (ADK)

이 폴더는 ADK(Agent Development Kit) 환경에서 Toolbox for database의 ToolboxSyncClient를 활용하여 BigQuery 등 외부 데이터 소스와 연동하는 툴박스 에이전트 예제를 제공합니다.

아래 예제를 실행하기 위해서 먼저 MCP Toolbox for Database 에 대한 이해와 설치가 필요합니다.

* MCP Toolbox for Databases 
    * https://googleapis.github.io/genai-toolbox/getting-started/introduction/

* MCP Toolbox설치
    * 설치 방법은 MCP Toolbox github 참고하세요. 
    * https://github.com/googleapis/genai-toolbox

    ```
    # MacOs 사용자
    brew install mcp-toolbox
    ```

## .env 설정.

`.env` 파일은 현재 폴더의 `상위 폴더(03-tools)` 에 위치해야 합니다.  환경파일 내 들어갈 내용은 아래 URL을 참고하세요.   
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model 

아래 환경설정은 기업에서 `Vertex AI`기반에서 ADK를 사용할때 적용되는 예제입니다.    

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 를 참고해서 변경.
GOOGLE_CLOUD_LOCATION="global"                  # Global Endpoint 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 현재 Gemini 최신 버전.

# Toolbox configuration
TOOLBOX_SYNC_CLIENT = "http://127.0.0.1:5000"

```

참고로 `AI Studio`를 사용하는 일반 사용자 버전은 아래와 같이 GOOGLE_API_KEY 를 셋팅해야 합니다.  

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE

```

## tools.yaml 예시

toolbox 에서 tool을 세팅하기 위해서는 아래와 같이 yaml 파일을 구성해야 합니다.  파일명은 일반적으로 tools.yaml 라고 합니다.  
BigQuery를 위한 설정 파일은 아래 URL 참고하세요. 
* https://googleapis.github.io/genai-toolbox/samples/bigquery/mcp_quickstart/


```yaml
sources:
  bigquery-bbc:
    kind: "bigquery"
    project: "ai-hangsik"

tools:
  query_bbc:
    kind: "bigquery-sql"
    source: "bigquery-bbc"
    statement:
      SELECT category, count(*) 
      FROM `ai-hangsik.bbc_news.fulltext` 
      group by category
    description: "BBC 뉴스 카테고리별 기사 수를 조회합니다."

toolsets:
 my_bq_toolset:
   - query_bbc
```
## 예제 실행

gcloud 명령어를 통해서 Google Cloud 실행 환경 로그인 설정합니다.

```
gcloud auth application-default login
```

### MCP Toolbox 실행
console 창을 하나 새롭게 열어서 아래와 같이 toolbox 를 기동합니다.
```
toolbox --tools-file "tools.yaml" 
```

### Agent 실행
마찬가지로 해당 shell 에서도 아래와 같이 GCP 인증이 필요합니다. 
```
gcloud auth application-default login
```
아래 명령어로 Tookbox 도구 예제를 실행할 수 있습니다
```
adk_workshop/adk/03-tools$ adk web
```      
toolbox agent 선택후에 "BBC 테이블 조회해줘" 라고 질문해보세요. 


## 라이센스

이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
