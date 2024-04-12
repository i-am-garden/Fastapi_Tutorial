from fastapi import FastAPI, Query, Path, Body, File, Header, Cookie, Form
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI(description="Fast API Tutorial : Part 9~10 \ Body, Field 사용 및 example, examples, fastapi_examples 사용법", version="0.1.0")

class Image(BaseModel):
    url: HttpUrl
    # url: str = Field(..., pattern= '^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)$')
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = Field(None, title="The description of the item", max_length=3000)
    price: float = Field(..., gt=0)
    tax: Optional[float] = None
    tags: set[str] = set()
    image : list[Image] = None

class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: list[Item]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(  # Body is used to embed the request body in the request
        ...,
        openapi_examples={
            "normal": {
                "summary": "An example of a normal item",
                "description": "This is an example of an item that has a name, description and price",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": "35.4",
                    "tags": ["rock", "metal", "bar"]
                },
            },
            "example_converted":{
                "summary": "An example of a converted item",
                "description": "Price is written in string format",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tags": ["rock", "metal", "bar"]
                },
            },
        },),):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/offers")
async def create_offer(offer: Offer = Body(...,
    examples=[
        {
            "summary": "An example of an offer",
            "description": "This is an example of an offer that includes items",
            "value": {
                "name": "Foo",
                "description": "The description",
                "price": 35.4,
                "items": [
                    {
                        "name": "Item1",
                        "description": "The description",
                        "price": 9.2
                    }
                ]
            }
        }
    ])):   # embed=True is used to embed the request body in the request
    return offer

@app.post("/images/multiple")
async def create_multiple_images(images: list[Image] = Body(..., embed=True)):
    return images