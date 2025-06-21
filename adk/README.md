# ADK(Agent Development Kit) 기반 AI 에이전트

이 저장소의 소스 코드는 VS Code에서 개발되었으나, IDE에 종속적이지 않습니다.  
VS Code는 다음 URL에서 설치할 수 있습니다: https://code.visualstudio.com/

## git 클론
```
git clone https://github.com/ForusOne/adk_agent.git
```

## uv 패키지 매니저 설치
### 1. uv 설치

이 프로젝트는 Python 패키지 매니저로 uv를 사용합니다.  
uv는 Rust로 작성된 매우 빠른 Python 패키지 및 프로젝트 매니저입니다.  
참고: https://github.com/astral-sh/uv

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
또는
```
pip install uv
```

## 2. uv 초기화 및 가상환경 설정

**pyproject.toml** 파일이 **같은 디렉토리**에 있어야 합니다.  
**/adk_agent/adk** 디렉토리에 **pyproject.toml** 파일이 존재해야 합니다.

```
/adk_agent/adk$ uv venv --python 3.12
```

가상환경 활성화:
```
/adk_agent/adk$ source .venv/bin/activate
(adk) adk_agent/adk$
```

테스트가 끝난 후에는 가상환경을 비활성화할 수 있습니다.
```
/adk_agent/adk$ deactivate
```

### 3. 간단한 ADK 에이전트 유닛 테스트

런타임 가상환경이 제대로 설정되었는지 확인하려면, 간단한 ADK 에이전트를 실행해보세요.

adk 패키지 설치:
```
(adk) /adk_agent/adk/01-agent$ uv add google-adk[vertexai]==1.1.1
```

**adk_agent/adk/01-agent/** 디렉토리에 .env 파일을 생성하세요.

```
(adk) /adk_agent/adk/01-agent$ ls -al
total 16
drwxr-xr-x   7 forus  pgroup   224 Jun  2 08:26 .
drwxr-xr-x  18 forus  pgroup   576 Jun  2 08:21 ..
-rw-r--r--   1 forus  pgroup   198 Jun  2 08:26 .env
-rw-r--r--   1 forus  pgroup  3178 Jun  2 08:20 README.md
drwxr-xr-x   6 forus  pgroup   192 Jun  2 08:25 basic
drwxr-xr-x   8 forus  pgroup   256 Jun  2 08:20 runtime
drwxr-xr-x   7 forus  pgroup   224 Jun  2 08:26 search
(adk) /adk_agent/adk/01-agent$
```

아래는 .env 파일 예시입니다. 본인의 GCP 프로젝트 정보와 API 키로 변경하세요.

참고: https://ai.google.dev/gemini-api/docs/api-key

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=AIzaSyD6ugbCWYZVM2uZh6Bd8

PROJECT_ID = "ai-forus"
PROJECT_NUMBER = "721523942"
LOCATION = "us-central1"
MODEL = "gemini-2.0-flash"
```

유닛 테스트 실행:
```
(adk) /adk_agent/adk/01-agent$ adk web
```

채팅창에 "What is Generative AI ?"를 입력해보세요.

테스트가 정상적으로 동작하면 아래와 같은 화면을 볼 수 있습니다.  
![adk_web](https://github.com/ForusOne/adk_agent/blob/main/images/adk_web.png?raw=true)