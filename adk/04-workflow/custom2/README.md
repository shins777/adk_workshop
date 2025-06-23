# 커스텀 워크플로우 CriticAgent 예제 (ADK)

## 예제 개요
이 폴더는 Agent Development Kit(ADK)를 활용하여 커스텀 다단계 비평 에이전트를 구축하고 운영하는 방법을 보여줍니다. 에이전트는 긍정/부정 비평을 각각의 서브 에이전트에 위임하고, 그 결과를 조율하여 워크플로우를 완성합니다.

- `agent.py`: 긍정/부정 비평을 위한 서브 에이전트들을 활용해 전체 워크플로우를 조율하는 루트 `CriticAgent`를 정의합니다.
- `critic.py`: 각 단계별 서브 에이전트의 이벤트를 순차적으로 실행 및 yield하는 커스텀 `CriticAgent` 클래스를 구현합니다.
- `sub_agent.py`: 다음과 같은 서브 에이전트들을 정의합니다:
    - `positive_critic_agent`: 긍정적 리뷰 생성
    - `negative_critic_agent`: 부정적 리뷰 생성

## 환경 설정
상위 폴더에 위치한 `.env` 파일에 다음과 같은 키를 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_project_id
PROJECT_NUMBER=your_project_number
LOCATION=your_location
MODEL=your_model_name
```

## 실행 방법
아래 명령어로 에이전트 예제를 실행할 수 있습니다:

```bash
adk web
```

워크플로우 로직은 `critic.py`에서, 서브 에이전트의 동작은 `sub_agent.py`에서 자유롭게 커스터마이즈할 수 있습니다.

## 라이선스 안내
이 프로젝트는 Apache License 2.0 하에 배포됩니다. 자세한 내용은 [LICENSE](../../LICENSE) 파일을 참고하세요.
