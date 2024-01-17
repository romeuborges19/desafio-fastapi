from typing import Union
from fastapi import FastAPI 
from server.router import pokemon_router
import httpx

app = FastAPI()

app.include_router(pokemon_router)


@app.get('/')
def read_root():
    return {'Hello':'World'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, "q": q}
