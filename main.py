from typing import Union
from fastapi import FastAPI 
from server.router import pokemon_router

app = FastAPI()
app.include_router(pokemon_router)

@app.get('/')
def read_root():
    return {'Hello':'World'}
