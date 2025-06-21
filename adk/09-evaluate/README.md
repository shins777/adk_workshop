# 평가 예제 (ADK)

## 예제 개요
이 폴더는 ADK 에이전트를 내장 평가 도구와 pytest를 활용해 평가하는 방법을 보여줍니다.

- `agent_eval/`: 에이전트 테스트를 위한 평가 데이터와 설정 파일 포함

## 환경 설정
필요한 환경 변수는 `.env` 파일에 설정하세요. 메인 프로젝트의 `.env` 파일을 참고하세요.

## 실행 방법
- ADK 평가 실행:
  ```bash
  adk eval agent_eval \
      agent_eval/data/conversation.test.json \
      --config_file_path=agent_eval/data/test_config.json \
      --print_detailed_results
  ```
- pytest 기반 테스트 실행:
  ```bash
  uv run pytest -m agent_eval
  ```
  (참고: 추가 pytest 플러그인이 필요할 수 있습니다.)

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다. 자세한 내용은 [LICENSE](../LICENSE) 파일을 참고하세요.