from fastapi import FastAPI, Query, Path, Body, Cookie, Header, Form , File, UploadFile, HTTPException, Request
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
        "Fast API Tutorial : Part 20~21 \\"
        "Path Operation Configuration \\"
        "JSON Compatible Encoder and Body Updates(patch에서 DB Partial Update)\\",
    version="0.1.0")

class Item(BaseModel):
    name: str = " "
    description: Optional[str] = None
    price: float = 0
    tax: Optional[float] = None
    tags: list[str] = []

class tags(Enum):
    items = "items"
    users = "users"

@app.post(
        "/items",
        response_model=Item,
        status_code=HTTP_201_CREATED,
        tags = [tags.items],
        summary= "Create Items",
        )
async def create_item(item: Item):
    """
    Create an item with all the information:
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: optional
    - **tags**: a list of string tags for this item
    """
    return item

@app.get("/items", tags = [tags.items])
async def read_items():
    return {"items": "items"}

@app.get("/users", tags = [tags.users])
async def read_users():
    return {"users": "users"}

fake_items_db = {
    1: {"name": "Foo", "price": 50.2},
    2: {"name": "Bar", "price": 62.5, "description": "The Bartenders"},
    3: {"name": "Baz", "price": 50.2, "tax": 2},
}

@app.get('/items/{item_id}', tags = [tags.items], response_model=Item)
async def read_item(item_id: int):
    return fake_items_db[item_id]

@app.put('/items/{item_id}', tags = [tags.items])
async def update_item(item_id: int, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_items_db[item_id] = json_compatible_item_data
    print(fake_items_db)
    return {"item_id": item_id, "item": item}

#patch 는 전달된 데이터만 (일부)업테이트
@app.patch('/items/{item_id}', tags=[tags.items], response_model=Item)
async def path_item(item_id: int, item: Item):
    stored_item_data = fake_items_db.get(item_id)
    if stored_item_data is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # 제공된 데이터에서 설정된 필드만 가져와서 기존 데이터를 업데이트
    updated_data = item.model_dump(exclude_unset=True)  # exclude_unset=True : 기본값이 아닌 값만 가져옴
    stored_item_data.update(updated_data)

    return stored_item_data


