from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from enum import Enum
from typing import Optional, Literal
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from uuid import UUID
from datetime import datetime, time, timedelta

app = FastAPI(description="Fast API Tutorial : Part 13~14 \ Response Body, Extra Models \ + 유저정보저장기초", version="0.2.0")

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

class UserInDB(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list[str] = []

items = {
    "foo" : {"name": "Foo", "price": 50.2},
    "bar" : {"name": "Bar", "description": "The Bartenders","price": 62.5, "tax": 20.2},
    "baz" : {"name": "Baz", "price": 50.2, "tax": "2"},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True, response_model_exclude= {"tax"})    # response_model_exclude_unset=True will exclude the unset values from the response
async def read_item(item_id: Literal["foo", "bar", "baz"]): # Literal is used to restrict the item_id to only foo, bar, baz
    return items[item_id]

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in : UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    print("userin.dict", user_in.model_dump())
    return user_in_db

@app.post("/user", response_model=UserOut)
async def create_user(user: UserIn):
    user_saved = fake_save_user(user)
    return user_saved