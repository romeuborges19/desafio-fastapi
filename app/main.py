from contextlib import asynccontextmanager

from fastapi import FastAPI
from redis_om import Migrator, get_redis_connection

from app.api.v1.router import router
from app.core.config import settings
from app.middleware.rate_limiter import RateLimiterMiddleware
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

app.add_middleware(RateLimiterMiddleware)

app.include_router(router, 
                   prefix=f'{settings.API_V1_STR}')

