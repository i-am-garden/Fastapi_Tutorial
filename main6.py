from fastapi import FastAPI, Query, Path, Body, Cookie, Header, Form , File, UploadFile, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from enum import Enum
from typing import Optional, Literal
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from uuid import UUID
from datetime import datetime, time, timedelta

app = FastAPI(description="Fast API Tutorial : Part 17~19 \ Request Forms and Files \ handling errors", version="0.2.0")

class Body1(BaseModel):
    name: str = " "
    description: Optional[str] = None
    
@app.post("/files")
async def create_file(files: list[bytes], token: str, body31351 : Body1 = Body(...)):
    if not files:
        return {"msg": "No file"}
    return {"file": files, "token": token, "hello": body31351}

@app.post("/uploadfile")
async def upload_file(files: UploadFile = None):
    if files:
        print(files)
        # contents = await file.read()
    if not files:
        print(files)
        return {"msg": "No file"}
    return {"file_headers": files.headers}

@app.get("/items/{item_id}")
async def read_items(item_id: int = Path(..., title="The ID of the item to update", ge=0)):
    if item_id not in [1111, 2222, 3333]:
        raise HTTPException(status_code=404, detail="Item not found")   # 'raise' 가 실행되는 순간 해당 함수는 종료된다.
    return {"item_id": item_id}


@app.post("/bodytest")
async def body_test(body: Body1 = Body(...)):
    return {"body" : body}

@app.get("/")
async def main():
    #파일을 업로드할 수 있는 html버튼을 만들어줘
    content = """
    <form action="/files" enctype="applicaiton/json" method="post">
    <input name="files" type="file" multiple>
    <input name="token" type="text">
    <input name="body" type="text">
    </form>
    """
    return HTMLResponse(content=content)
    
# Custom Exception인 UnicornException을 정의
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

# UnicornException이 발생했을 때 처리하는 핸들러
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request = Request, exc = UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."}
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}

# RequestValidationError가 발생했을 때 처리하는 핸들러
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request : Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}))

@app.get("/validation/{item_id}")
async def read_item(item_id: int):
    if item_id not in [1111, 2222, 3333]:
        # raise HTTPException(status_code=418, detail="NONOENOEPE")
        raise RequestValidationError("Item not found")
    return {"item_id": item_id}