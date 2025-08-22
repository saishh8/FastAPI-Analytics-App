from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from src.api.events import router as event_router

app = FastAPI()
app.include_router(event_router, prefix="/api/events")


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool,None] = None

@app.get("/")
async def read_root():
    return {"Hello": "Worlder"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_price':item.price}

@app.get('/healthz')
async def read_api_health():
    return {'status':'OK'}