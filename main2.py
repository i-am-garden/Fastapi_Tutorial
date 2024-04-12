from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI(description="Fast API Tutorial : Part 7~8", version="0.1.0")

class Item(BaseModel):
    name: str
    description: Optional[str] = Field(None, title="The description of the item", max_length=300)
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

@app.put("/items/{item_id}")
async def update_item(*, item_id: int = Path(..., title="The ID of the item to update", ge=0, le=150), q: Optional[str] = None, item: Item, user: User):
    results = {"item_id": item_id, "item": item}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    return results