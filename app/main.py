from api.v1.pokemon_handler import pokemon_router
from fastapi import FastAPI 

app = FastAPI()
app.include_router(pokemon_router)

@app.get('/')
def read_root():
    return {'Hello':'World'}
