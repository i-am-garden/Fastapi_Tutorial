from fastapi import FastAPI, Query, Path
from enum import Enum
from typing import Optional
from pydantic import BaseModel

app = FastAPI(description="Fast API Tutorial : Part 1~6", version="0.1.0")


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def post_root():
    return {"message": "Hello World from the post route"}

@app.put("/")
async def put_root():
    return {"message": "Hello World from the put route"}


@app.get("/items")
async def read_items(q : str | None = Query(..., min_length=3, max_length=10, alias='item-query')): # Query parameter is required
    results = {"items": [{"item_id": "item1"}, {"item_id": "item2"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def get_item(item_id: str, q: str | None = None, short: bool=False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is a long description"})
    return item

@app.get("/users")
async def list_users():
    return {"list users route"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users/me")
async def get_current_user():
    return {"Message": "Your the current user"}

@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: str, item_id: str, q: Optional[str] = None, short: bool=False):
    item = {"item_id": item_id, "user_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is a long description"})
    return item


class FoodEnum(str, Enum):
    pizza = "pizza"
    burger = "burger"
    pasta = "pasta"
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.pizza:
        return {"food_name": food_name, "message": "Pizza is the best"}
    elif food_name == FoodEnum.burger:
        return {"food_name": food_name, "message": "Burger is the best"}
    elif food_name == FoodEnum.pasta:
        return {"food_name": food_name, "message": "Pasta is the best"}
    elif food_name == FoodEnum.fruits:
        return {"food_name": food_name, "message": "Fruits are the best"}
    elif food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "Vegetables are the best"}
    elif food_name == FoodEnum.dairy:
        return {"food_name": food_name, "message": "Dairy is the best"}
    
class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : Optional[float] = None

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump()   # Convert the item object to a dictionary
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.model_dump()}  # '**' is used to unpack the dictionary (dict 합칠때 사용)
    if q:
        result.update({"q": q})
    return result

@app.get("/item_validation/{item_id}")
async def get_item_validation(item_id: int = Path(..., title="id of the item to validate"), q: Optional[str] = Query(None, alias="item-query")):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    return result