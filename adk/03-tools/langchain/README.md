# LangChain 툴 예제 (ADK)

이 폴더는 ADK(Agent Development Kit)에서 LangChain 기반 툴을 연동하는 방법을 보여줍니다. Tavily Search 등 다양한 LangChain 툴을 활용해 에이전트의 기능을 확장할 수 있습니다.

## 환경 설정
상위 폴더의 `.env` 파일에 필요한 키를 설정하세요.

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
TAVILY_API_KEY=your_tavily_api_key
```

## 실행 방법
각 하위 폴더의 예제와 안내를 참고하세요. 예시:

```bash
uv run python tavily_search/agent.py
```

## 라이센스 정보
이 프로젝트는 Apache License 2.0에 따라 라이센스가 부여됩니다. 자세한 내용은 [LICENSE](../../LICENSE) 파일을 참조하세요.
