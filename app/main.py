from contextlib import asynccontextmanager

from redis_om import Migrator, get_redis_connection
from app.api.v1.router import router
from fastapi import FastAPI
from app.core.config import settings

from app.models.user_model import User 
from app.services.cache_service import cache


@asynccontextmanager
async def lifespan(app: FastAPI):
    Migrator().run()

    User.Meta.database = get_redis_connection(
        url=settings.REDIS_DATA_URL,
        decode_responses=True
    )

    cache.conn(url=settings.REDIS_CACHE_URL)
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
    lifespan=lifespan)
app.include_router(router, 
                   prefix=f'{settings.API_V1_STR}')

@app.get('/')
def read_root():
    return {'Hello':'World'}
