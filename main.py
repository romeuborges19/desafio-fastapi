from typing import Union
from fastapi import FastAPI 
from server.router import pokemon_router
import redis

rd = redis.Redis(host="localhost", port=5432, db=0)

app = FastAPI()

app.include_router(pokemon_router)


@app.get('/')
def read_root():
    return {'Hello':'World'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, "q": q}
