from contextlib import asynccontextmanager

from redis_om import get_redis_connection
from api.v1.router import router
from fastapi import FastAPI
from core.config import settings

from models.user_model import User 
from services.cache_service import cache


@asynccontextmanager
async def lifespan(app: FastAPI):
    User.Meta.database = get_redis_connection(
        url=settings.REDIS_DATA_URL,
        decode_responses=True
    )

    cache.conn(url=settings.REDIS_CACHE_URL)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)

@app.get('/')
def read_root():
    return {'Hello':'World'}
