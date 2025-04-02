from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


@app.get("/")
def abc():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/{item_id}/name/{item_name}")
def read_item(item_id: int, item_name: str):
    return {"item_id": item_id, "item_name": item_name}

@app.get("/items/{item_id}/name/{item_name}/price/{item_price}")
def read_item(item_id: int, item_name: str, item_price: float):
    return {"item_id": item_id, "item_name": item_name, "item_price": item_price}


@app.get("/blogs")
def read_blogs(limit: int = 10, published: bool = True):
    blogs = ["blog1", "blog2", "blog3", "blog4", "blog5", "blog6", "blog7", "blog8", "blog9", "blog10", "blog11"]
    
    if published:
        return {"blogs": blogs[:limit], "limit": limit}

    return {"blogs": blogs}

