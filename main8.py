from fastapi import FastAPI, Query, Path, Body, Cookie, Header, Form , File, UploadFile, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from enum import Enum
from typing import Optional, Literal
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import *
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from uuid import UUID
from datetime import datetime, time, timedelta


app = FastAPI(
    description=
        "Fast API Tutorial : Part 22~ 25\\"
        "Dependencies \\"
        "Dependencies Class\\"
        "Sub-dependencies\\"
        "Dependencies in path operation decorators, global dependencies\\",
    version="0.1.0")

# 자주 사용되는 매개 변수를 함수로 만들어서 사용할 수 있다.
async def Hello(word : str = "World"):
    return "Hello" + word
async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 10, abc: str = Depends(Hello)):
    return {"q": q, "skip": skip, "limit": limit}

class Common_Query_Params():
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 10):
        self.q = q
        self.skip = skip
        self.limit = limit
    def __call__(self, q: Optional[str] = None, skip: int = 0, limit: int = 10):
        return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/", deprecated=True)
async def read_items(args: dict = Depends(common_parameters)):
    """
    This page read items
    """
    return args

@app.get("/users/")
async def read_users(args: dict = Depends(common_parameters)):
    return args

@app.get("/items2/")
async def read_items2(args: Common_Query_Params = Depends()):
    return args


async def verify_token(x_token: str = Header(None)):
    if x_token == "fake":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    
async def verify_key(x_key: str = Header(None)):
    if x_key == "fake_key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    
# dependencies를 decoration에 넣어서 사요앟며 Verification을 할 수 있다.
@app.get("/items3/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items3():
    return {"items": "items"}