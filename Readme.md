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
