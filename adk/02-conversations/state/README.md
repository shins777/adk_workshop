# 상태 기반 대화 예제 (ADK)

## 예제 개요
이 폴더는 ADK 프레임워크를 활용해 상태 기반 대화형 에이전트를 구축하는 방법을 보여줍니다. 이를 통해 고급 컨텍스트 및 흐름 제어가 가능합니다.

## 환경 설정
상위 폴더의 `.env` 파일에 아래와 같이 키를 설정하세요.

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## 소스코드 실행 방법
상태 기반 대화 에이전트 실행:

```bash
uv run -m state.output_key --app_name <app_name> --user_id <user_id> --session_id <session_id>

python main.py --app_name <app_name> --user_id <user_id> --session_id <session_id>
```

## 라이선스 정보
이 프로젝트는 Apache License 2.0을 따릅니다. 자세한 내용은 [LICENSE](../../../LICENSE) 파일을 참고하세요.
