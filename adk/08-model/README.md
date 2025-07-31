# ADK 08-model 전체 가이드

이 디렉토리는 ADK(Agent Development Kit)에서 다양한 LLM(대형 언어 모델) 연동 예제를 제공합니다. 각 서브 폴더는 외부 또는 로컬 LLM을 ADK와 연동하는 방법을 안내합니다.

## 폴더 및 기능 요약

### litellm
외부 LLM(OpenAI GPT-4o, Anthropic Claude 등)을 LiteLLM을 통해 연동하는 예제입니다. 환경설정(.env) 및 API 키 등록 방법, 실행 방법이 포함되어 있습니다.

### ollama_agent
로컬 Ollama 모델(Llama 3, Gemma 등)을 LLM 에이전트로 연동하는 예제입니다. 환경설정(.env) 및 Ollama API 연동 방법, 실행 및 테스트 방법이 포함되어 있습니다.

## 공통 환경설정 (.env)
모든 모델 예제는 상위 폴더(08-model)에 `.env` 파일을 위치시키고, 각 서브 폴더의 README.md에 안내된 환경 변수(API 키, 엔드포인트 등)를 등록해야 합니다.

### 주요 환경 변수 예시
```
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
OLLAMA_API_BASE=http://localhost:11434
# 각 모델별 추가 환경 변수는 각 README.md 참고
```

## 실행 방법
각 모델 예제는 폴더 내 명령어(adk web, ollama list 등)와 함께 실행 및 테스트할 수 있습니다. 상세 사용법은 각 서브 폴더의 README.md를 참고하세요.

## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
