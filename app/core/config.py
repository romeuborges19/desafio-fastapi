from typing import List
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
from decouple import config

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    JWT_SECRET_KEY: str = config('JWT_SECRET_KEY', cast=str)
    JWT_REFRESH_SECRET_KEY: str = config('JWT_REFRESH_SECRET_KEY', cast=str)
    ALGORITHM: str = "HS256"
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60*24*7
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Pokémon FastAPI"
    REDIS_CACHE_URL: str = config('REDIS_CACHE_URL', cast=str)
    REDIS_RATELIMIT_URL: str = config('REDIS_RATELIMIT_URL', cast=str)
    REDIS_DATA_URL: str = config('REDIS_DATA_URL', cast=str)
    RATE_LIMIT_LIMIT: int = config('RATE_LIMIT_LIMIT', default=10)
    RATE_LIMIT_PERIOD: int = config('RATE_LIMIT_PERIOD', default=60)
    TEST_USERNAME:str = "romeu"
    TEST_EMAIL:str = "romeuborges19@gmail.com"
    TEST_PASSWORD:str = "romeuzao"


    class Config:
        case_sensitive = True

settings = Settings()
