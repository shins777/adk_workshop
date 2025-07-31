# LiteLLM 에이전트 예제 (ADK)

## 예제 개요
이 예제는 ADK 프레임워크에서 외부 LLM 제공자를 LiteLLM을 통해 연동하는 방법을 보여줍니다. OpenAI GPT-4o와 Anthropic Claude 모델을 모두 지원합니다.

## 환경 설정
`.env` 파일에 아래와 같이 키를 설정하세요.

```
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
```

## 실행 방법

`08-model` 폴더에서 아래 명령어를 실행후 adk web 실행 후 화면에서 테스트를 진행하시면 됩니다. 

```
adk_workshop/adk/08-model$ adk web
```

`llm.py` 파일을 수정하여 사용할 모델(`gpt` 또는 `claude`)을 선택할 수 있습니다.

## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
