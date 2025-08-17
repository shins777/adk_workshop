# Ollama 에이전트 예제 (ADK)

## 예제 개요
이 예제는 ADK 프레임워크에서 로컬 Ollama 모델(Llama 3, Gemma 등)을 LLM 에이전트로 연동하는 방법을 보여줍니다.

## 환경 설정
`.env` 파일에 아래와 같이 키를 설정하세요.

```
OLLAMA_API_BASE=http://localhost:11434
```


## 실행 방법

ollama 설치 후 간단한 단위테스트 

```
/Users/hangsik$ ollama list
NAME               ID              SIZE      MODIFIED     
gemma3:latest      a2af6cc3eb7f    3.3 GB    3 weeks ago     
llama3.2:latest    a80c4f17acd5    2.0 GB    2 months ago    
gemma3:4b          a2af6cc3eb7f    3.3 GB    2 months ago    
/Users/hangsik$ ollama run gemma3
>>> 
>>> what is the generative ai ?
Okay, let's break down what Generative AI is. It's a really hot topic 
right now, and it's evolving rapidly, but here's a clear explanation:
**1. What is AI (Artificial Intelligence)?**
First, let's quickly recap AI in general. AI refers to computer systems 
that can perform tasks that typically require human intelligence.
```

## 예제 실행

`08-model` 폴더에서 아래 명령어를 실행후 adk web 실행 후 화면에서 테스트를 진행하시면 됩니다. 

```
adk_workshop/adk/08-model$ adk web
```

`agent.py` 파일을 수정하여 사용할 모델(`gemma` 또는 `llama`)을 선택할 수 있습니다.

python 코드로 단위테스트는 
```
python ollama_unittest.py

```

## 라이센스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
