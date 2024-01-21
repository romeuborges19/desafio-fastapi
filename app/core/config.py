from pydantic_settings import BaseSettings
from decouple import config

class Settings(BaseSettings):
    # API settings
    PROJECT_NAME: str = "Pokémon FastAPI"
    API_V1_STR: str = '/api/v1'

    # JWT settings
    JWT_REFRESH_SECRET_KEY: str = config('JWT_REFRESH_SECRET_KEY', cast=str)
    JWT_SECRET_KEY: str = config('JWT_SECRET_KEY', cast=str)
    ALGORITHM: str = "HS256"
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60*24*7

    # Redis connection settings
    REDIS_CACHE_URL: str = config('REDIS_CACHE_URL', cast=str)
    REDIS_RATELIMIT_URL: str = config('REDIS_RATELIMIT_URL', cast=str)
    REDIS_DATA_URL: str = config('REDIS_DATA_URL', cast=str)

    # Rate limiting settings
    RATE_LIMIT_LIMIT: int = config('RATE_LIMIT_LIMIT', default=10)
    RATE_LIMIT_PERIOD: int = config('RATE_LIMIT_PERIOD', default=60)

    # Test settings
    TEST_USERNAME: str = config("TEST_NAME", default="test_user")
    TEST_EMAIL: str = config("TEST_EMAIL", default="test.mail@gmail.com")
    TEST_PASSWORD: str = config("TEST_PASSWORD", default="test124")

    class Config:
        case_sensitive = True

settings = Settings()
