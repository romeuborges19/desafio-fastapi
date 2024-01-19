import redis
from redis_om import redis
from api.v1.router import router
from fastapi import FastAPI 

REDIS_CACHE_URL='redis://localhost:6379'

app = FastAPI()
app.include_router(router)

@app.get('/')
def read_root():
    return {'Hello':'World'}
