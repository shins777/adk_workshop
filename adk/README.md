# ADK(Agent Development Kit) 기반 AI 에이전트 개발 환경 구성

ADK는 로컬환경에서 편리하게 개발 할 수 있는 환경을 제공하기 때문에, 개발환경을 로컬 환경에서 진행하는것을 추천 드립니다.
예를들어 "adk web" 명령어를 사용하면 복잡한 데이터 흐름을 쉽게 이해하고 분석 및 디버그를 할 수 있습니다.
혹시 python notebook 환경에서 빠른 기술 검증이 필요하다면, notebooks에 있는 코드를 참고하기 바랍니다. 단, 해당 폴더에는 모든 기능에 대한 코드 예제가 들어있지 않습니다. 

소스 코드는 VS Code에서 개발되었으나, 특정 IDE에 종속적이지 않습니다. 개발자의 환경에 맞게 git clone 해서 사용하시면 됩니다.  
참고로 VS Code 사용 시 다음 URL에서 설치할 수 있습니다: https://code.visualstudio.com/

## git 클론
먼저 github의 소스를 활용하기 위해서는 아래와 같이 git clone 명령어를 통해서 로컬 환경에 소스를 가져옵니다.  
```
git clone https://github.com/shins777/adk_workshop.git
```

## uv 패키지 매니저 설치

이 프로젝트는 Python 패키지 매니저로 uv를 사용합니다.  
uv는 Rust로 작성된 매우 빠르고 편리한 Python 패키지 및 프로젝트 매니저입니다. 좀더 자세한 내용은 아래 링크를 참고하세요.
* 참고: https://github.com/astral-sh/uv

uv 설치는 아래와 같이 두가지 방법중 하나로 설치를 해주시면 됩니다. 
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
또는
```
pip install uv
```

## 2. uv 초기화 및 가상환경 설정

uv 사용할때는 파이썬 가상환경을 사용하는게 효율적입니다. uv는 아래와 같은 방법으로 쉽게 python 가상환경을 만들수 있습니다. 
만일 위에서 언급한 git clone 이 정상적으로 처리가 되었다면, **/adk_agent/adk** 디렉토리에 **pyproject.toml** 파일이 존재해야 합니다. 이 pyproject.toml 파일은 /adk_agent/adk 안에 가상환경을 구성하여, 하위 폴더에 있는 코드 실행시 모두 해당 패키지 기반에서 실행된다고 생각하시면 됩니다. (참고, adk 와 동일 폴더 위치에 있는 a2a 폴더의 경우 실행 시에는 따로 해당 실행환경에 맞는 가상환경을 만듭니다.)

가급적 python 버전은 3.12 환경에서 개발하도록 권고합니다. 

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

## 3. 간단한 ADK 에이전트 유닛 테스트

런타임 가상환경이 제대로 설정되었는지 확인하려면, 간단한 ADK 에이전트를 실행해보세요.


### 1. adk 패키지 설치:  
* ADK 패지는 아래 url 에서 확인할 수 있으면 현재 기준(2025년 6월) google-adk 1.4.2 버전을 기준으로 합니다.
* https://pypi.org/project/google-adk/

```
(adk) /adk_agent/adk/01-agent$ uv add google-adk[vertexai]==1.4.2
```

### 2. .env 파일 생성:

.env 파일은 ADK를 실행할때 필요한 환경정보가 들어 있습니다. 이곳에는 api key를 비롯해서 실행환경에서 실시간으로 참조할 수 있는 constant 값을 포함하고 있습니다. 

간단한 단위테스트를 위해서 아래와 같이 **adk_agent/adk/01-agent/** 디렉토리에 .env 파일을 생성하세요.

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
GCP 프로젝트에서 API 키를 가져오는 방법은 아래와 같습니다.
* 참고: https://ai.google.dev/gemini-api/docs/api-key

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PROJECT_ID=your-gcp-project-id
PROJECT_NUMBER=your-gcp-project-number
LOCATION=us-central1
MODEL=gemini-2.0-flash
```

### 3. 단위테스트 실행:

```
(adk) /adk_agent/adk/01-agent$ adk web
```

채팅창에 "What is Generative AI ?"를 입력해보세요.

테스트가 정상적으로 동작하면 아래와 같은 화면을 볼 수 있습니다.  
![adk_web](https://github.com/ForusOne/adk_agent/blob/main/images/adk_web.png?raw=true)