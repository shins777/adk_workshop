# 함수형 툴 예제 (ADK)

## 예제 개요
이 폴더는 ADK 에이전트에서 함수형 툴을 활용해 외부 API를 호출하는 방법을 보여줍니다. 단일 및 다중 함수형 툴 호출 예제가 포함되어 있습니다.

- `single_call/`: 단일 함수형 툴(예: 환율)
- `multiple_call/`: 다중 함수형 툴(예: 환율, 주가)

## 환경 설정
상위 폴더의 `.env` 파일에 아래와 같이 키를 설정하세요.

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
STOCK_API_KEY=your_stock_api_key
```

## 소스코드 실행 방법
각 하위 폴더의 에이전트 코드와 안내를 참고하세요. 예시:

```bash
function/single_call/adk web
```

## 라이선스 정보
이 프로젝트는 Apache License 2.0을 따릅니다. 자세한 내용은 [LICENSE](../../LICENSE) 파일을 참고하세요.
