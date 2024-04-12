# {FASTAPI TUTORIAL}
- [{FASTAPI TUTORIAL}](#fastapi-tutorial)
- [Setting](#setting)
  - [가상환경 만들기](#가상환경-만들기)
  - [가상환경에 패키지 설치](#가상환경에-패키지-설치)
- [Background Knowledge](#background-knowledge)
  - [HTTP요청](#http요청)
  - [파이썬 함수 호출: 키워드 인자 vs 위치 인자](#파이썬-함수-호출-키워드-인자-vs-위치-인자)
    - [1. 위치 인자(Positional Argument):](#1-위치-인자positional-argument)
    - [2. 키워드 인자(Keyword Argument):](#2-키워드-인자keyword-argument)
    - [3. 위치 인자를 사용하지 않고 키워드 인자만 받기:](#3-위치-인자를-사용하지-않고-키워드-인자만-받기)
  - [Python 비동기 문법](#python-비동기-문법)
- [Fastapi Docs](#fastapi-docs)
  - [Outline](#outline)
    - [코드 작성법:](#코드-작성법)
- [URL](#url)
  - [URL Query Parameter](#url-query-parameter)
  - [fastapi Query](#fastapi-query)
  - [fastapi Query에서 python ellipsis 활용법](#fastapi-query에서-python-ellipsis-활용법)
  - [Path](#path)
- [Request](#request)
  - [Request body](#request-body)
  - [Pydantic](#pydantic)
  - [Regex Cheat Sheat](#regex-cheat-sheat)
  - [Cookie \& Header](#cookie--header)
    - [References](#references)
  - [Form](#form)
  - [Form 클래스 소개와 사용 방법](#form-클래스-소개와-사용-방법)
    - [Form 클래스 개요](#form-클래스-개요)
    - [Form 클래스 사용 방법](#form-클래스-사용-방법)
    - [Form 클래스의 장점](#form-클래스의-장점)
  - [Form VS application/json](#form-vs-applicationjson)
    - [다른 HTTP 데이터 형식들](#다른-http-데이터-형식들)
- [Status code](#status-code)
  - [Custom Exception](#custom-exception)
    - [Custom Exception 정의](#custom-exception-정의)
    - [UnicornException 처리](#unicornexception-처리)
    - [엔드포인트 정의](#엔드포인트-정의)
- [Response](#response)
  - [Response Validation](#response-validation)
    - [response\_model \& response\_class](#response_model--response_class)
- [Dependencies](#dependencies)
- [Securities](#securities)
  - [OAuth2PAsswordBearer](#oauth2passwordbearer)
  - [JWT](#jwt)
  - [JWT를 활용한 로그인 시스템](#jwt를-활용한-로그인-시스템)
- [Middleware](#middleware)
  - [여러개의 MiddleWare다루기](#여러개의-middleware다루기)
- [Database(SQL)](#databasesql)


# Setting
## 가상환경 만들기
1. **가상환경 만들기**:

가상환경을 만들기 위해 다음과 같이 명령 프롬프트(Windows)나 터미널(Linux/macOS)에서 `venv` 모듈을 사용합니다.

```bash
python -m venv myenv
```

위 명령은 `myenv`라는 이름의 가상환경을 만듭니다. 원하는 이름으로 변경할 수 있습니다.

2. **가상환경 활성화**:

가상환경을 만든 후, 해당 가상환경을 활성화해야 합니다.

   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```

   - **Linux/macOS**:
     ```bash
     source myenv/bin/activate
     ```

가상환경이 활성화되면 프롬프트나 터미널의 앞 부분에 (myenv)와 같은 표시가 나타납니다.

3. **가상환경에서 패키지 설치 및 사용**:

가상환경이 활성화된 상태에서는 `pip`을 통해 패키지를 설치하고 사용할 수 있습니다. 이렇게 하면 시스템 전역에 영향을 주지 않고 패키지를 사용할 수 있습니다.

가상환경을 사용 중에 필요한 패키지를 설치하려면 다음과 같이 합니다:

```bash
pip install package_name
```

4. **가상환경 비활성화**:

가상환경을 사용한 작업을 마치면 비활성화할 수 있습니다.

```bash
deactivate
```

## 가상환경에 패키지 설치
1. **터미널을 엽니다**:

   원하는 디렉토리에서 터미널을 엽니다.

2. **가상환경을 활성화합니다 (선택사항)**:

   가상환경을 사용 중이라면 해당 가상환경을 활성화합니다. 가상환경을 사용하지 않는다면 이 단계를 건너뛰어도 됩니다. 가상환경을 활성화하려면 터미널에서 다음 명령어를 실행합니다.

   ```bash
   source 가상환경이름/bin/activate
   ```

3. **Python 3을 사용하여 requirements.txt에 있는 패키지 설치**:

   다음 명령어를 사용하여 requirements.txt에 나열된 패키지들을 설치합니다. 이때 Python 3를 사용하여 설치해야 합니다.

   ```bash
   pip3 install -r requirements.txt
   ```

4. **패키지 설치 확인**:

   설치된 패키지를 확인하려면 `pip3 list` 명령어를 사용합니다.

   ```bash
   pip3 list
   ```

   이 명령어는 시스템에 설치된 모든 Python 패키지를 나열합니다. 여기에 requirements.txt에 나열된 패키지들도 포함되어야 합니다.

5. **가상환경 비활성화 (선택사항)**:

   작업을 마치고 가상환경을 비활성화하려면 다음 명령어를 사용합니다.

   ```bash
   deactivate
   ```
# Background Knowledge
## HTTP요청
1. **GET**:
   - 설명: 서버로부터 리소스를 가져오기 위한 요청입니다. 일반적으로 데이터를 가져오는 데 사용됩니다.
   - 예시: 웹 페이지를 요청할 때, 쿼리 매개변수를 전송할 때 등

2. **POST**:
   - 설명: 서버로 데이터를 제출하기 위한 요청입니다. 주로 데이터를 생성하거나 업데이트할 때 사용됩니다.
   - 예시: 로그인 정보를 서버로 전송할 때, 새로운 사용자를 생성할 때 등

3. **PUT**:
   - 설명: 서버의 리소스를 업데이트하기 위한 요청입니다. 전체 리소스를 업데이트합니다.
   - 예시: 이미 존재하는 사용자 정보를 전체적으로 업데이트할 때 등

4. **PATCH**:
   - 설명: 서버의 리소스를 부분적으로 업데이트하기 위한 요청입니다. 일부 필드만 업데이트할 때 사용됩니다.
   - 예시: 사용자 정보 중 일부 필드만 업데이트할 때 등

5. **DELETE**:
   - 설명: 서버의 리소스를 삭제하기 위한 요청입니다.
   - 예시: 데이터베이스에서 사용자를 삭제할 때 등

6. **OPTIONS**:
   - 설명: 서버가 지원하는 메서드들을 확인하기 위한 요청입니다.
   - 예시: CORS (Cross-Origin Resource Sharing)에서 브라우저가 사전 요청을 보낼 때 등

7. **HEAD**:
   - 설명: GET 요청과 유사하지만, 실제 데이터를 받지 않고 응답 헤더만을 받는 요청입니다. 일반적으로 리소스가 존재하는지 확인하거나, 리소스의 메타데이터를 가져오는 데 사용됩니다.
   - 예시: 파일의 존재 여부를 확인할 때 등

8. **TRACE**:
   - 설명: 클라이언트가 서버로 전송한 요청을 그대로 반환하는 요청입니다. 주로 디버깅 목적으로 사용됩니다.
   - 예시: 요청이 서버에서 어떻게 처리되는지 확인할 때 등

9. **CONNECT**:
   - 설명: 프록시를 통해 서버에 대한 터널을 만들기 위한 요청입니다. 주로 HTTPS 연결을 설정할 때 사용됩니다.
   - 예시: HTTPS 연결을 설정할 때 등

## 파이썬 함수 호출: 키워드 인자 vs 위치 인자

파이썬에서 함수를 호출할 때는 두 가지 타입의 인자를 사용할 수 있습니다: 키워드 인자(keyword argument)와 위치 인자(positional argument). 이 두 가지 인자의 주요 차이점을 알아보겠습니다.

### 1. 위치 인자(Positional Argument):

- 함수를 호출할 때 인자의 위치(순서)에 따라 값을 전달합니다.
- 인자의 순서가 매우 중요하며, 함수 정의에서 인자의 위치와 동일한 순서로 값을 전달해야 합니다.
- 인자를 전달할 때 이름을 지정하지 않으며, 단순히 값만 전달합니다.
- 예시: `func(1, 2, 3)`

### 2. 키워드 인자(Keyword Argument):

- 함수를 호출할 때 인자의 이름을 지정하여 값을 전달합니다.
- 인자의 순서가 중요하지 않으며, 함수 호출 시 인자의 이름을 명시하여 순서를 무시할 수 있습니다.
- 인자를 전달할 때 `인자이름=값`의 형식으로 전달합니다.
- 함수 정의에서 지정된 기본값을 덮어쓸 수 있으며, 이를 통해 필요한 인자만 전달할 수 있습니다.
- 예시: `func(a=1, b=2, c=3)`

### 3. 위치 인자를 사용하지 않고 키워드 인자만 받기:

함수 정의에서 `*`를 사용하여 위치 인자를 사용하지 않고 키워드 인자만 받도록 할 수 있습니다. 이렇게 하면 함수 호출 시에는 인자의 순서에 관계 없이 키워드를 지정할 수 있습니다.

```python
def my_func(*, a, b, c):
    print(a, b, c)

# 위치 인자를 사용하지 않고 키워드 인자만 사용한 함수 호출
my_func(a=1, b=2, c=3)  # 출력: 1 2 3
my_func(b=2, c=3, a=1)  # 출력: 1 2 3
```

위의 예제에서는 함수를 호출할 때 위치 인자를 사용하지 않고 키워드 인자만 사용하는 방법을 보여줍니다. 모든 인자는 키워드로 지정되어야 하며, 위치 인자를 사용할 수 없습니다.

## Python 비동기 문법
`await`는 비동기적인 작업을 수행할 때 사용되는 키워드입니다. 파이썬의 `asyncio` 라이브러리와 함께 사용되며, 비동기 함수나 코루틴 안에서 사용됩니다. 이 키워드를 사용하면 해당 작업이 완료될 때까지 실행이 일시 중지되고 다른 작업이 실행됩니다. 

일반적으로 다음과 같은 구조에서 사용됩니다:

```python
async def some_async_function():
    result = await some_other_async_function()
    # 이후 작업 수행
```

여기서 `some_other_async_function()`은 비동기 함수나 코루틴이며, `await` 키워드를 사용하여 호출됩니다. 이 호출은 해당 비동기 함수가 완료될 때까지 기다리고, 결과를 반환하고나서 비동기 함수의 실행을 계속합니다. 

`await`는 일반적으로 비동기적인 I/O 작업(예: 네트워크 호출, 파일 시스템 액세스 등)을 수행할 때 사용됩니다. I/O 작업을 수행하는 동안 프로그램이 다른 작업을 수행할 수 있도록 하기 위해 사용됩니다. 

코루틴 안에서만 `await`를 사용할 수 있으며, 코루틴은 `async def`로 선언된 함수입니다. 따라서 `await`를 사용하려면 해당 함수도 `async` 키워드로 선언되어야 합니다. 

요약하자면, `await`는 비동기적인 작업을 실행하고 그 결과를 기다리는 데 사용되며, 비동기 함수나 코루틴 안에서만 사용됩니다.

# Fastapi Docs
## Outline
FastAPI는 기본적으로 API 문서 생성을 지원합니다. 이를 통해 API에 대한 자동화된 문서를 생성하고, 이를 통해 사용자들이 API를 이해하고 사용할 수 있습니다. FastAPI의 주요 문서 기능은 다음과 같습니다.

1. **자동 API 문서 생성**:
   - FastAPI는 OpenAPI(Swagger) 형식의 API 문서를 자동으로 생성합니다. 이를 통해 API의 엔드포인트, 요청 및 응답 형식, 파라미터, 예제 등의 정보를 쉽게 확인할 수 있습니다.

2. **인터랙티브한 API 문서**:
   - 자동으로 생성된 API 문서는 인터랙티브하게 작동합니다. 사용자는 문서 페이지에서 엔드포인트를 시도해 볼 수 있고, 예상되는 응답을 확인할 수 있습니다.

3. **API 문서의 UI/UX 개선**:
   - FastAPI는 Swagger UI와 ReDoc와 같은 UI 라이브러리를 통해 보다 사용자 친화적인 API 문서를 제공합니다.

이제 각 기능을 구현하는 방법에 대해 설명하겠습니다.

### 코드 작성법:

1. **자동 API 문서 생성**:

   FastAPI에서 API 문서를 자동으로 생성하려면 각 엔드포인트에 대해 Pydantic 모델을 사용하여 요청 및 응답 형식을 정의해야 합니다. 이를 위해 다음과 같이 코드를 작성합니다.

   ```python
   from fastapi import FastAPI
   from pydantic import BaseModel

   app = FastAPI()

   class Item(BaseModel):
       name: str
       price: float

   @app.post("/items/")
   async def create_item(item: Item):
       return item
   ```

2. **인터랙티브한 API 문서**:

   FastAPI는 자동으로 생성된 API 문서를 `/docs` 엔드포인트에서 제공합니다. 서버를 실행한 후 브라우저에서 `http://localhost:8000/docs`와 같이 접속하면 인터랙티브한 API 문서를 확인할 수 있습니다.

3. **API 문서의 UI/UX 개선**:

   FastAPI는 기본적으로 Swagger UI를 사용하여 API 문서를 제공합니다. 만약 ReDoc를 사용하고 싶다면 FastAPI의 `openapi_url` 매개변수를 통해 설정할 수 있습니다.

   ```python
   from fastapi import FastAPI
   from fastapi.openapi.docs import get_redoc_html

   app = FastAPI()

   @app.get("/redoc", include_in_schema=False)
   async def redoc_html():
       return get_redoc_html(openapi_url="/openapi.json", title="FastAPI ReDoc")
   ```

이렇게 코드를 작성하면 FastAPI를 사용하여 API 문서를 자동으로 생성하고, 인터랙티브하게 제공할 수 있습니다. API 문서의 UI/UX를 개선하려면 적절한 옵션을 설정하여 Swagger UI 또는 ReDoc를 사용하면 됩니다.
###옵션
옵션을 설정하여 FastAPI의 API 문서를 조정하고 사용자 정의할 수 있습니다. 주요 옵션에는 다음과 같은 것들이 있습니다.

1. **title**:
   - API 문서 페이지의 제목을 설정합니다. 기본값은 "FastAPI"입니다.

2. **description**:
   - API 문서 페이지에 표시할 설명을 설정합니다.

3. **version**:
   - API의 버전 정보를 설정합니다.

4. **openapi_url**:
   - OpenAPI(Swagger) 스펙을 참조하는 URL을 지정합니다. 기본값은 `/openapi.json`입니다.

5. **redoc_url**:
   - ReDoc를 사용할 때 ReDoc UI의 URL을 지정합니다.

6. **swagger_ui_oauth2_redirect_url**:
   - Swagger UI에서 OAuth2 인증을 사용할 때 OAuth2 리다이렉트 URL을 지정합니다.

7. **oauth2_redirect_url**:
   - OAuth2 인증을 사용할 때 인증이 성공한 후 리다이렉트할 URL을 지정합니다.

8. **swagger_ui_init_oauth**:
   - Swagger UI에서 OAuth2 인증을 초기화하는 데 사용되는 정보를 지정합니다.

9. **swagger_ui_disable_cors**:
   - Swagger UI에서 CORS (Cross-Origin Resource Sharing)를 비활성화할지 여부를 지정합니다.

이러한 옵션들은 FastAPI 애플리케이션의 설정에서 사용됩니다. 예를 들어, 다음은 FastAPI 애플리케이션에 대한 API 문서의 제목과 설명을 설정하는 방법입니다.

```python
from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html

app = FastAPI(
    title="My Awesome API",
    description="This is an awesome API powered by FastAPI!",
    version="1.0.0",
)

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(openapi_url="/openapi.json", title="FastAPI ReDoc")
```

이렇게 설정하면 API 문서 페이지의 제목은 "My Awesome API"로, 설명은 "This is an awesome API powered by FastAPI!"로 설정됩니다. 이러한 옵션을 사용하여 API 문서를 보다 자세히 설명하고 사용자 정의할 수 있습니다.

# URL
## URL Query Parameter
URL의 쿼리 매개변수(query parameters)는 웹 요청에서 데이터를 전달하는 데 사용되는 매개변수입니다. 쿼리 매개변수는 URL의 끝에 `?`를 붙이고 그 뒤에 키(key)와 값(value)의 쌍을 `&`로 구분하여 나열합니다. 각 쌍은 `key=value` 형식으로 표시됩니다. 쿼리 매개변수는 서버에 데이터를 전달하거나 필터링, 정렬, 페이지네이션 등을 구현하는 데 자주 사용됩니다.

예를 들어, 다음과 같은 URL이 있다고 가정해봅시다.

```
https://www.example.com/search?q=python&sort=asc&page=1
```

위의 URL에서 `?` 이후의 부분이 쿼리 매개변수입니다. 이 URL에는 다음과 같은 세 개의 쿼리 매개변수가 포함되어 있습니다:

- `q=python`: 검색어는 "python"입니다.
- `sort=asc`: 결과를 오름차순으로 정렬하도록 지시합니다.
- `page=1`: 페이지 번호는 1번입니다.

Python에서는 `urllib.parse` 모듈의 `parse_qs()` 함수를 사용하여 URL의 쿼리 매개변수를 파싱할 수 있습니다. 이 함수는 쿼리 매개변수를 딕셔너리로 반환합니다. 각 키는 쿼리 매개변수의 이름을 나타내고, 해당 값은 해당 키의 값입니다.

예를 들어, 위의 URL에서 쿼리 매개변수를 파싱하는 코드는 다음과 같습니다.

```python
from urllib.parse import urlparse, parse_qs

url = "https://www.example.com/search?q=python&sort=asc&page=1"

# URL 파싱
parsed_url = urlparse(url)

# 쿼리 매개변수 파싱
query_params = parse_qs(parsed_url.query)

# 파싱된 쿼리 매개변수 출력
print(query_params)
```

위 코드를 실행하면 파싱된 쿼리 매개변수를 출력할 수 있습니다. 결과는 다음과 같을 것입니다:

```python
{'q': ['python'], 'sort': ['asc'], 'page': ['1']}
```

이제 우리는 URL의 쿼리 매개변수를 파싱하고 사용할 수 있습니다. 이를 통해 웹 애플리케이션에서 필요한 데이터를 전달하고 처리할 수 있습니다.

## fastapi Query
fastapi의 `Query` 클래스는 web 요청에서 사용되는 query의 유효성을 검사할 수 있는 좋은 패키지이다.
`Query` 클래스는 FastAPI에서 쿼리 매개변수를 처리할 때 사용되는 많은 옵션들을 제공합니다. 몇 가지 주요한 옵션들을 살펴보겠습니다.

1. **default**: 매개변수의 기본값을 설정합니다. 클라이언트가 해당 쿼리 매개변수를 제공하지 않을 경우 이 값이 사용됩니다.

```python
from fastapi import Query

@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3, max_length=50, default="default_value")):
    return {"q": q}
```

2. **min_length** 및 **max_length**: 매개변수의 최소 및 최대 길이를 제한합니다.

```python
from fastapi import Query

@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3, max_length=50)):
    return {"q": q}
```

3. **regex**: 매개변수 값의 정규 표현식을 지정하여 유효성을 검사합니다.

```python
from fastapi import Query

@app.get("/items/")
async def read_items(q: str = Query(None, regex="^[a-zA-Z0-9]+$")):
    return {"q": q}
```

4. **title**: 매개변수의 제목을 지정합니다. 이 값은 자동 생성된 문서에 사용됩니다.

```python
from fastapi import Query

@app.get("/items/")
async def read_items(q: str = Query(None, title="Query Parameter")):
    return {"q": q}
```

5. **description**: 매개변수에 대한 설명을 지정합니다. 이 값은 자동 생성된 문서에 사용됩니다.

```python
from fastapi import Query

@app.get("/items/")
async def read_items(q: str = Query(None, description="Query parameter for search")):
    return {"q": q}
```

6. **deprecated**: 매개변수가 더 이상 사용되지 않음을 표시합니다. 자동 생성된 문서에 이를 표시하고 사용자에게 경고합니다.

```python
from fastapi import Query

@app.get("/items/")
async def read_items(q: str = Query(None, deprecated=True)):
    return {"q": q}
```

7. **alias**: 매개변수에 대한 별칭을 지정합니다. 이 별칭은 API 요청시 사용되며 자동 생성된 문서에는 표시되지 않습니다.

```python
from fastapi import Query

@app.get("/items/")
async def read_items(q: str = Query(None, alias="search_query")):
    return {"q": q}
```

이러한 옵션들을 활용하여 쿼리 매개변수를 정의하고 유효성을 검사할 수 있으며, 자동 생성된 API 문서에도 문서화됩니다. 이를 통해 클라이언트가 올바른 방식으로 서버와 상호 작용할 수 있도록 도와줍니다.

## fastapi Query에서 python ellipsis 활용법
```python
import numpy as np

# 1차원 배열 예제
a = [1, 2, 3, 4, 5, 6]
print(a[:])  # 출력: [1, 2, 3, 4, 5, 6]

# 2차원 배열 예제
b = [[1, 2, 3], [4, 5, 6]]
print(b[:][:])  # 출력: [[1, 2, 3], [4, 5, 6]]
print(b[1][:])  # 출력: [4, 5, 6]

# numpy 배열로 변환
c = np.array(b)
print(c[:][:])  # 출력: [[1, 2, 3], [4, 5, 6]]

# 3차원 배열 예제
d = np.array([[[i + 2 * j + 8 * k for i in range(3)] for j in range(3)] for k in range(3)])
print(d[1, ...])  # 출력: [[ 8  9 10], [10 11 12], [12 13 14]]
print(d[..., 1])  # 출력: [[ 1  3  5], [ 9 11 13], [17 19 21]]
print(d[1, ..., 1])  # 출력: [ 9 11 13]

# Ellipsis를 사용한 함수 스텁
def do_something():
    ...

# FastAPI에서 Ellipsis를 사용하여 필수 항목 지정
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/something/")
async def something(q: str = Query(..., min_length=10)):
    return {"q": q}
```

이 코드는 다음을 수행합니다:

1. 기본 Python 리스트와 numpy 배열에서 슬라이싱을 보여줍니다.
2. Ellipsis를 사용하여 다차원 배열의 모든 차원을 선택하는 방법을 보여줍니다.
3. Ellipsis를 사용하여 함수 스텁을 만드는 방법을 보여줍니다.
4. FastAPI에서 Ellipsis를 사용하여 필수 쿼리 매개변수를 지정하는 방법을 보여줍니다.

## Path
Query와 비슷하게 작동하며 url path에 포함되어 있는 변수값을 가져올 때 사용된다.

# Request
## Request body
웹에서의 요청(request)은 종종 메시지 본문(body)을 포함할 수 있습니다. 이 본문은 클라이언트가 서버로 보내는 데이터를 포함하고 있습니다. 이러한 데이터는 주로 POST, PUT 및 PATCH 요청과 함께 전송되며, 종종 JSON, XML 또는 기타 형식으로 인코딩됩니다. 이 본문을 "요청 본문(Request Body)"이라고 합니다.

str이나 bool처럼 primitive type은 query로 보낼 수 있지만 더 복잡한 dictionary나 class는 request body로 보낸다.

HTTP 요청은 일반적으로 다음과 같은 형태를 가집니다.

```
POST /login HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: 36

{"username": "john_doe", "password": "secret"}
```

위의 예에서 볼 수 있듯이, 요청 본문은 요청 헤더와 요청 라인 다음에 따라옵니다. 이 경우 JSON 형식으로 인코딩된 데이터가 본문에 포함되어 있습니다.

웹 서버는 이러한 요청 본문을 읽고 분석하여 클라이언트가 보낸 데이터를 이해하고 처리합니다. 이러한 처리는 서버 측의 프로그래밍 언어 또는 프레임워크를 사용하여 이루어집니다. 대부분의 웹 프레임워크는 요청 본문을 쉽게 읽고 해석할 수 있는 도구를 제공합니다.

클라이언트는 요청 본문을 사용하여 서버로 데이터를 전송하고, 서버는 요청 본문을 사용하여 클라이언트가 제공한 데이터를 처리합니다. 이를 통해 웹 애플리케이션은 사용자 입력을 받아들이고, 데이터베이스에 저장하거나 다른 서비스와 상호 작용하여 동적으로 콘텐츠를 생성할 수 있습니다.

## Pydantic
Pydantic은 BaseModel 외에도 다양한 데이터 타입을 제공합니다. 몇 가지 주요한 데이터 타입을 살펴보겠습니다.

1. **Field**: 필드는 Pydantic 모델의 개별 속성을 정의하는 데 사용됩니다. 필드를 사용하여 속성의 유효성 검사 규칙, 기본값, 설명 등을 지정할 수 있습니다.

```python
from pydantic import Field

class User(BaseModel):
    id: int
    username: str = Field(..., description="User's username")
    email: str = Field(..., regex=r"[^@]+@[^@]+\.[^@]+", description="User's email address")
```

2. **Constraints**: Pydantic은 데이터의 값에 대한 제약을 정의하기 위한 여러 유효성 검사 함수를 제공합니다. 예를 들어, `gt`, `ge`, `lt`, `le` 등의 함수를 사용하여 숫자 필드에 대한 최소값 또는 최대값을 지정할 수 있습니다.

```python
from pydantic import constr

class User(BaseModel):
    username: constr(min_length=4, max_length=32)
```

3. **Validators**: Validators를 사용하여 데이터 필드에 대한 추가적인 유효성 검사를 수행할 수 있습니다. Validator는 메서드로 정의되며, 필드의 값을 검사하고 필요한 경우 예외를 발생시킵니다.

```python
from pydantic import validator

class User(BaseModel):
    password1: str
    password2: str

    @validator("password2")
    def passwords_match(cls, v, values):
        if "password1" in values and v != values["password1"]:
            raise ValueError("passwords do not match")
        return v
```

4. **Nested Models**: BaseModel을 사용하여 중첩된 데이터 모델을 정의할 수 있습니다. 이를 통해 복잡한 데이터 구조를 효율적으로 표현할 수 있습니다.

```python
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    username: str
    email: str
    address: Address
```

## Regex Cheat Sheat
다양한 정규식을 쓰는 것은 매우매우 힘들다, 따라서 다음 사이트를 활용하자.

[ihateregex](https://ihateregex.io/expr/url/)

## Cookie & Header
쿠키(Cookie)와 헤더(Header)는 웹 개발에서 중요한 개념입니다. 각각의 역할과 기능에 대해 간단히 설명해보겠습니다:

1. **쿠키(Cookie)**:
   - 쿠키는 클라이언트(웹 브라우저)에 저장되는 작은 데이터 조각입니다.
   - 주로 사용자의 상태를 유지하거나 사용자의 활동을 추적하는 데 사용됩니다.
   - 서버에서 클라이언트로 전송되며, 클라이언트 측에서 저장됩니다.
   - 쿠키는 이름, 값, 만료 날짜 및 경로 등의 속성을 포함할 수 있습니다.
   - 클라이언트가 서버에 요청을 보낼 때 쿠키는 자동으로 요청 헤더에 포함되어 서버에 전송됩니다.
   - 주로 사용자 인증, 세션 관리, 사용자 설정 저장 등에 사용됩니다.

2. **헤더(Header)**:
   - 헤더는 클라이언트와 서버 간에 전송되는 메타데이터입니다.
   - HTTP 요청 및 응답의 일부로 전송됩니다.
   - 각 헤더는 이름과 값의 쌍으로 구성됩니다.
   - 요청 헤더는 클라이언트가 서버에 요청을 보낼 때 정보를 전달하며, 응답 헤더는 서버가 클라이언트에 응답을 보낼 때 정보를 전달합니다.
   - 일반적인 요청 헤더에는 사용자 에이전트(User-Agent), 콘텐츠 유형(Content-Type), 인증 정보(Authorization) 등이 있습니다.
   - 일반적인 응답 헤더에는 콘텐츠 길이(Content-Length), 캐시 제어(Cache-Control), 콘텐츠 유형(Content-Type) 등이 있습니다.

### References
[쿠키 원리](https://velog.io/@msung99/%EC%9D%B8%EC%A6%9D%EA%B4%80%EB%A0%A8-Header-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EC%BF%A0%ED%82%A4Cookie)

[모든 HTTP 헤더 목록](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers)

[REST API 사용 가이드](https://sanghaklee.tistory.com/57)

## Form
## Form 클래스 소개와 사용 방법

Form 클래스는 FastAPI에서 HTML 폼 데이터를 처리하는 데 사용됩니다. HTML 폼에서 사용자가 입력한 데이터를 쉽게 처리하고 유효성을 검사하는 데 유용합니다. 이 문서에서는 Form 클래스의 개요와 사용 방법에 대해 설명합니다.

### Form 클래스 개요

Form 클래스는 Pydantic 라이브러리를 기반으로 하며, FastAPI에서 제공됩니다. 이 클래스를 사용하면 HTML 폼에서 제출된 데이터를 파이썬 객체로 쉽게 변환할 수 있습니다. 이를 통해 사용자 입력 데이터를 쉽게 처리하고 유효성을 검사할 수 있습니다.

### Form 클래스 사용 방법

Form 클래스를 사용하여 HTML 폼 데이터를 처리하는 방법은 다음과 같습니다:

1. **Form 인스턴스 생성**: 먼저 FastAPI의 Form 클래스를 import 하고, 해당 클래스의 인스턴스를 생성합니다.

    ```python
    from fastapi import FastAPI, Form

    app = FastAPI()

    @app.post("/submit/")
    async def submit_form(username: str = Form(...), password: str = Form(...)):
        return {"username": username, "password": password}
    ```

2. **HTML 폼과의 통합**: HTML 폼에서 제출된 데이터를 Form 클래스의 인스턴스로 변환합니다. HTML 폼에서 제출된 데이터는 Form 인스턴스의 각 필드에 자동으로 할당됩니다.

3. **유효성 검사**: Form 클래스는 Pydantic 모델을 기반으로 하므로 입력 데이터의 유효성을 검사할 수 있습니다. 모델의 유효성 검사 규칙을 적용하여 입력 데이터를 검증할 수 있습니다.

4. **인터페이스 일관성**: Form 클래스는 FastAPI의 사용자 인터페이스와 일관성을 유지합니다. FastAPI는 form 데이터를 처리하는 데 Form 클래스를 권장하므로 이를 따르면 코드가 더 일관성 있게 유지됩니다.

### Form 클래스의 장점

- 간편성: HTML 폼 데이터를 쉽게 처리할 수 있습니다.
- 유효성 검사: Pydantic 모델을 사용하여 입력 데이터의 유효성을 검사할 수 있습니다.
- 인터페이스 일관성: FastAPI의 사용자 인터페이스와 일관성을 유지합니다.

## Form VS application/json
frontend에서 request를 보낼 때 Form형식으로 보낼 수도 있고, json형식으로 보낼 수도 있다. 이 때, header에 form 형식인지 json형식인지 명시해준다.
form 데이터를 보낼 때는 일반적으로 `Content-Type` 헤더를 `application/x-www-form-urlencoded`로 설정합니다. 이는 HTML 폼의 기본 데이터 형식이기 때문입니다.

JSON 데이터를 보낼 때는 `Content-Type` 헤더를 `application/json`으로 설정해야 합니다. 이 헤더는 서버에게 요청 본문이 JSON 형식임을 알려줍니다.

1. form 데이터를 보낼 때:

```
Content-Type: application/x-www-form-urlencoded
```

2. JSON 데이터를 보낼 때:

```
Content-Type: application/json
```

Backend 서버에서는 header를 읽고 form인지, Json인지 판단한다. 이후에 데이터타입에 맞는 알맞은 parsing 법으로 데이터를 파싱해서 코드 인풋에 넣어준다.
Fastapi의 경우 다양한 데이터타입의 HTTP요청이 왔을 때 그에 맞는 파싱법으로 자동으로 파싱하게 유연하게 설정이 되어있다.
더 lower level에서 백엔드 코드를 짤 떄에 받는 데이터 타입을 명시해 주었다면 그에 맞지 않는 request가 왔을 때 오류가 발생할 수 있으니 주의해야 한다.

### 다른 HTTP 데이터 형식들
HTTP 요청의 본문에 사용될 수 있는 일반적인 미디어 타입(Content-Type)은 다음과 같습니다:

1. **application/json**: JSON 형식의 데이터를 전송하는 데 사용됩니다.
2. **application/xml**: XML 형식의 데이터를 전송하는 데 사용됩니다.
3. **application/x-www-form-urlencoded**: HTML 폼에서 사용되는 데이터를 전송하는 데 사용됩니다.
4. **multipart/form-data**: 파일 업로드와 함께 폼 데이터를 전송하는 데 사용됩니다.
5. **text/plain**: 텍스트 데이터를 전송하는 데 사용됩니다.
6. **application/octet-stream**: 이진 데이터를 전송하는 데 사용됩니다.
7. **application/pdf**: PDF 파일을 전송하는 데 사용됩니다.
8. **image/jpeg**, **image/png**, **image/gif**: 이미지 파일을 전송하는 데 사용됩니다.
9. **audio/mpeg**, **audio/wav**: 오디오 파일을 전송하는 데 사용됩니다.
10. **video/mp4**, **video/mpeg**: 비디오 파일을 전송하는 데 사용됩니다.

이 외에도 많은 미디어 타입이 있을 수 있으며, 요청의 목적과 데이터의 형식에 따라 적절한 미디어 타입을 선택해야 합니다. 요청 헤더의 `Content-Type` 필드를 사용하여 해당 미디어 타입을 지정할 수 있습니다.

# Status code
웹페이지의 상태를 Status code에 담아서 보내준다. 데이터가 실제로 전송에 성공되었더라도 (status :200), status code를 수동을 조작하여 다른 값을 보낸다면 브라우저는 이를 우선시한다!

[Statuscode 목록](https://www.whatap.io/ko/blog/40/)

## Custom Exception
### Custom Exception 정의

```python
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name
```

위 코드는 `UnicornException`이라는 사용자 정의 예외를 정의합니다. 이 예외는 `name`이라는 속성을 가집니다.

### UnicornException 처리

```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request, exc):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."}
    )
```

위 코드는 `UnicornException`이 발생했을 때 처리하는 핸들러를 정의합니다. `UnicornException`이 발생하면 418 상태 코드와 함께 특정 메시지를 반환하는 JSONResponse를 생성합니다.

### 엔드포인트 정의

```python
@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}
```

위 코드는 `/unicorns/{name}` 엔드포인트를 정의하고 있습니다. 해당 엔드포인트는 입력된 이름이 "yolo"인 경우 `UnicornException`을 발생시킵니다. 그렇지 않은 경우에는 입력된 이름을 반환합니다.

# Response
## Response Validation
### response_model & response_class
`response_model`과 `response_class`는 FastAPI에서 응답을 정의하는 데 사용되는 두 가지 옵션입니다.

1. `response_model`: 해당 엔드포인트가 반환하는 데이터 모델을 지정합니다. 이를 통해 FastAPI는 응답 데이터를 해당 모델에 따라 직렬화하고 검증합니다. 이를 통해 클라이언트가 예상대로 데이터를 수신할 수 있도록 보장합니다. 

예를 들어, 다음과 같이 사용할 수 있습니다:
```python
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    return {"name": "Foo", "description": "An amazing item!"}
```
위 코드에서 `/items/{item_id}` 엔드포인트는 `Item` 모델을 반환합니다. 반환된 데이터가 모델과 일치하지 않는 경우 FastAPI는 자동으로 데이터를 모델에 맞게 변환하거나 유효성을 검사합니다.

2. `response_class`: 해당 엔드포인트에서 사용할 응답 클래스를 지정합니다. 기본적으로 FastAPI는 JSONResponse 클래스를 사용합니다. 그러나 이 옵션을 사용하여 다른 유형의 응답 클래스를 지정할 수 있습니다. 이것은 파일 다운로드, HTML 응답 등과 같은 특수한 응답 형식을 다룰 때 유용합니다.

예를 들어, 다음과 같이 사용할 수 있습니다:
```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello, world!</h1>"
```
위 코드에서 `/` 루트 엔드포인트는 HTMLResponse 클래스를 사용하여 HTML 응답을 반환합니다.

# Dependencies
FastAPI에서는 의존성(dependency)을 사용하여 경로 처리 함수에 전달되는 매개변수를 초기화하거나 데이터를 검증하고 전처리할 수 있습니다. 의존성은 주로 `Depends` 클래스나 함수를 사용하여 정의됩니다.

1. **의존성 함수 예시:**

```python
from fastapi import Depends, FastAPI, Header

app = FastAPI()

def get_user_agent(user_agent: str = Header(None)):
    return user_agent or "No user-agent provided"

@app.get("/items/")
async def read_items(user_agent: str = Depends(get_user_agent)):
    return {"user_agent": user_agent}
```

위의 코드에서 `get_user_agent` 함수는 `Header`에 대한 의존성 함수로 정의되어 있습니다. 이 함수는 사용자 에이전트(User-Agent) 헤더를 반환하거나, 헤더가 제공되지 않으면 "No user-agent provided"를 반환합니다. `read_items` 경로 처리 함수는 `user_agent` 매개변수를 의존성으로 사용하며, 해당 의존성 함수인 `get_user_agent` 함수에 의해 초기화됩니다.

2. **전역 의존성 예시:**

```python
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()

async def get_api_key(header: str = Header(None)):
    if header and "api-key" in header:
        return header.split("api-key=")[1]
    else:
        raise HTTPException(status_code=400, detail="X-API-Key header not found")

app = FastAPI(dependencies=[Depends(get_api_key)])

@app.get("/items/")
async def read_items():
    return {"message": "Items retrieved successfully"}
```

위의 코드에서 `get_api_key` 함수는 `Header`에 대한 전역 의존성으로 정의되어 있습니다. 이 함수는 `X-API-Key` 헤더에서 API 키를 추출하고, 헤더가 제공되지 않거나 올바르지 않으면 `HTTPException`을 발생시킵니다. `app` 객체의 `dependencies` 속성을 사용하여 전역 의존성으로 등록되었으므로, 이 의존성은 모든 경로 처리 함수에 적용됩니다.

# Securities
## OAuth2PAsswordBearer
`OAuth2PasswordBearer`는 FastAPI에서 OAuth 2.0 비밀번호 인증 방식을 사용할 때 사용되는 보안 요청 객체입니다. 이 요청 객체는 클라이언트가 사용자의 자격 증명을 인증하기 위해 사용자 이름과 비밀번호를 보내는 데 사용됩니다.

일반적으로 클라이언트는 사용자 이름과 비밀번호를 `POST` 요청의 본문(body)에 JSON 형식으로 제공합니다. 그런 다음 서버는 이러한 자격 증명을 검증하고, 유효한 경우에는 액세스 토큰을 발급하여 보호된 엔드포인트에 대한 인증에 사용합니다.

`OAuth2PasswordBearer`를 사용하면 FastAPI 애플리케이션에서 사용자의 자격 증명을 검증하고, 인증된 사용자에게 액세스 토큰을 발급할 수 있습니다.

예를 들어, 다음은 `OAuth2PasswordBearer`를 사용하여 사용자의 자격 증명을 검증하고 인증된 사용자에게 액세스 토큰을 발급하는 FastAPI 애플리케이션의 간단한 예시입니다:

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_decode_token(token):
    return {"username": "testuser"}

def fake_hash_password(password: str):
    return "fakehashed" + password

def fake_check_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = fake_decode_token(token)
    if token_data is None:
        raise credentials_exception
    return token_data

@app.post("/token")
async def login(username: str, password: str):
    user = fake_decode_token(username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    hashed_password = fake_hash_password(password)
    if not hashed_password == "fakehashed" + password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token_data: dict = Depends(fake_check_token)):
    return token_data
```

위의 예시에서 `OAuth2PasswordBearer`를 사용하여 보안 요청 객체를 만들었습니다. 이를 사용하여 토큰을 가져올 수 있으며, 토큰이 유효한지 확인하는 데 사용할 수 있습니다. 요청에서 토큰을 가져오고, 유효한 경우 사용자의 자격 증명을 반환하여 인증된 사용자임을 확인합니다.

## JWT
[JWT Link](https://jwt.io/)
이곳에서 json파일을 암호화 및 복호화할 수 있다.
[Session vs Token Authentication in 100 Seconds](https://www.youtube.com/watch?v=UBUNrFtufWo)
[passlib.Context](https://passlib.readthedocs.io/en/stable/lib/passlib.context.html)

## JWT를 활용한 로그인 시스템

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from pydantic import BaseModel
from typing import Optional

# 임시 데이터베이스 대신에 사용할 사용자 모델
class User(BaseModel):
    username: str
    hashed_password: str

# 임시로 사용할 유저 데이터
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "hashed_password": "$2b$12$2Kk8d3M.8n.Tblq4v2hhwuqFpWbs7h10/t.DxOaEVZsGbBzw4X4GK"  # 패스워드는 'secret'입니다.
    }
}

# 비밀번호 해싱을 위한 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT 토큰 설정
SECRET_KEY = "a1f60a483c44714ffbd908727190bf99f50c929756f0f5b1fc0f9722d12d2da1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# FastAPI 인스턴스 생성
app = FastAPI()

# OAuth2 토큰 베어러 설정
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 사용자 비밀번호 검증 함수
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 사용자 조회 함수
def get_user(username: str):
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return User(**user_dict)

# 비밀번호 검증 및 사용자 정보 반환
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# 토큰 생성 함수
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 토큰 검증 함수
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username=username)
    if user is None:
        raise credentials_exception
    return user

# 로그인 라우터
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# 보호된 라우터
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
```

위의 코드는 FastAPI를 사용하여 사용자 인증을 구현하는 기본적인 방법을 보여줍니다. 이제 다른 파일에 비밀번호를 해싱하는 함수를 작성해보겠습니다.

```python
from passlib.context import CryptContext

# 비밀번호 해싱을 위한 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 비밀번호를 해싱하는 함수
def hash_password(password: str):
    return pwd_context.hash(password)
```

위 코드는 Passlib를 사용하여 비밀번호를 해싱하는 함수를 정의합니다. 필요한 곳에서 이 함수를 가져와서 사용하면 됩니다. 이제 이 두 파일을 사용하여 사용자 로그인 시스템을 구현할 수 있습니다. 필요에 따라 코드를 수정하여 데이터베이스와 연동하거나 보안을 더 강화할 수 있습니다.

# Middleware
Middleware는 FastAPI 애플리케이션의 요청과 응답을 처리하는 과정 사이에서 특정 작업을 수행하는 소프트웨어 레이어입니다. 요청이 들어오고 응답이 나가는 사이에 중간에서 요청을 가로채서 추가적인 처리를 할 수 있습니다. 이를 통해 로깅, 요청 검증, 보안 관련 작업, 세션 관리 등 다양한 기능을 구현할 수 있습니다.

Middleware는 FastAPI 애플리케이션의 모든 요청에 대해 실행되며, 요청 전후에 특정 작업을 실행할 수 있게 해줍니다. 예를 들어, 모든 요청에 대해 실행 시간을 측정하고 로깅하거나, 요청이 들어올 때마다 특정 헤더를 검사하는 등의 작업에서 미들웨어를 구현하는 방법은 상당히 간단합니다. `FastAPI` 인스턴스에 `.add_middleware` 메소드를 사용하여 미들웨어를 추가할 수 있습니다. 이 메소드는 미들웨어 컴포넌트를 첫 번째 인자로 받으며, 이 컴포넌트는 요청을 받아 처리한 후 응답을 반환하는 `call` 메소드를 구현해야 합니다.

아래는 FastAPI에서 간단한 미들웨어를 구현하는 예시 코드입니다. 이 예시에서는 모든 요청과 응답에 걸린 시간을 측정하고, 이를 로그로 기록하는 미들웨어를 생성합니다.

```python
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()  # 요청이 시작된 시간
        response = await call_next(request)  # 다음 미들웨어 또는 실제 요청 처리기를 호출
        process_time = time.time() - start_time  # 요청 처리 시간 계산
        response.headers['X-Process-Time'] = str(process_time)  # 응답 헤더에 처리 시간 추가
        print(f"Request: {request.url.path} completed in {process_time} seconds")  # 로그 출력
        return response

app = FastAPI()

# 미들웨어 추가
app.add_middleware(TimingMiddleware)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

위 코드에서 `TimingMiddleware` 클래스는 `BaseHTTPMiddleware`를 상속받아 구현되었습니다. `dispatch` 메소드는 실제 요청을 처리하기 전과 후에 원하는 작업을 수행할 수 있게 해줍니다. 여기서는 요청을 처리하기 전에 현재 시간을 기록하고, 요청이 처리된 후에는 처리 시간을 계산하여 응답 헤더에 추가하고 콘솔에 로그를 출력하고 있습니다.

`app.add_middleware(TimingMiddleware)`를 호출하여 애플리케이션에 미들웨어를 추가합니다. 이렇게 하면 애플리케이션의 모든 요청은 `TimingMiddleware`를 통과하게 되어, 요청과 응답 과정에 걸린 시간을 측정하고 로그로 남길 수 있게 됩니다.

## 여러개의 MiddleWare다루기
FastAPI에서 여러 개의 미들웨어를 사용할 때, 미들웨어는 추가된 순서대로 실행됩니다. 요청이 들어오면 첫 번째로 추가된 미들웨어가 가장 먼저 실행되고, 그 다음으로 추가된 미들웨어가 순차적으로 실행됩니다. 응답이 생성되어 클라이언트로 돌아갈 때는 미들웨어가 추가된 순서의 역순으로 실행됩니다. 즉, 마지막에 추가된 미들웨어가 응답을 가장 먼저 처리하고, 첫 번째로 추가된 미들웨어가 응답을 가장 마지막에 처리합니다.

이러한 방식은 미들웨어 간의 의존성을 관리하고, 특정 미들웨어가 다른 미들웨어의 결과를 기반으로 작업을 수행할 수 있게 합니다. 예를 들어, 보안 관련 미들웨어를 먼저 실행하여 요청의 유효성을 검증한 후, 로깅 미들웨어에서 요청에 대한 로깅을 수행할 수 있습니다.

아래는 두 개의 미들웨어를 사용하는 예시입니다: 하나는 요청과 응답에 걸린 시간을 측정하고, 다른 하나는 모든 요청에 특정 헤더를 추가합니다.

```python
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers['X-Process-Time'] = str(process_time)
        print(f"Request: {request.url.path} completed in {process_time} seconds")
        return response

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers['X-Custom-Header'] = "This is a custom header"
        return response

app = FastAPI()

# 미들웨어 추가 순서에 주목
app.add_middleware(TimingMiddleware)
app.add_middleware(CustomHeaderMiddleware)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

이 예시에서는 먼저 `TimingMiddleware`가 추가되어 요청 처리 시간을 측정하고, 그 다음으로 `CustomHeaderMiddleware`가 추가되어 모든 응답에 `"X-Custom-Header"`를 추가합니다.

요청이 처리되는 순서는 다음과 같습니다:
1. `TimingMiddleware`가 요청을 가로채서 처리 시간 측정을 시작합니다.
2. `CustomHeaderMiddleware`가 요청을 받아서 다음 단계로 넘깁니다.
3. 실제 요청 처리기(여기서는 `read_root`)가 요청을 처리합니다.
4. 응답이 생성되어 `CustomHeaderMiddleware`를 통해 반환되면서, `"X-Custom-Header"`가 응답 헤더에 추가됩니다.
5. 마지막으로 `TimingMiddleware`를 통해 반환되면서, 처리 시간이 응답 헤더에 추가되고, 로그가 출력됩니다.

이처럼 FastAPI에서는 미들웨어를 추가하는 순서가 중요하며, 이 순서에 따라 요청과 응답이 처리되는 방식이 결정됩니다.

[Client] --> |Request| --> [TimingMiddleware] --> [CustomHeaderMiddleware] --> |Request| --> [Server]
             |<-----------------------------------------------------------------------------------|
             |Response| <-- [TimingMiddleware] <-- [CustomHeaderMiddleware] <-- |Response| <-- [Server]


# Database(SQL)