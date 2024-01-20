from datetime import datetime

from aredis_om import get_redis_connection
from fastapi import HTTPException, Request, status
from jose import jwt

from app.core.config import settings
from app.schemas.auth_schema import TokenPayload


client = get_redis_connection(url=settings.REDIS_RATELIMIT_URL, decode_responses=True)


class JWTTokenRequest:
    @staticmethod
    def get_bearer_token(request: Request):
        auth_token = request.headers.get('Authorization')

        if 'Bearer' in auth_token:
            bearer_token: str = auth_token.split('Bearer')[1].strip()
            return bearer_token
        else:
            return None

    @staticmethod
    def get_current_user_id(request: Request):
        jwt_token = JWTTokenRequest.get_bearer_token(request)

        if jwt_token:
            payload = jwt.decode(
                jwt_token,
                settings.JWT_SECRET_KEY,
                settings.ALGORITHM
            )

            token_data = TokenPayload(**payload)
            user_id = token_data.sub

            return user_id
        else:
            return None

async def is_rate_limited(user_id: str, limit:int, period:int):
    if not client:
        raise Exception("REDIS-RATELIMIT client was not initialized properly.")

    current_minute = datetime.now()
    current_minute = current_minute.strftime("%H:%M")

    key = f"ratelimit:{user_id}:{current_minute}"

    try:
        request_count = await client.incr(key)

        if request_count > limit:
            return True

        if request_count == 1:
            await client.expire(key, period)
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Error while checking rate limit")

    return False


async def rate_limiter(user_id: str):
    limit, period = settings.RATE_LIMIT_LIMIT, settings.RATE_LIMIT_PERIOD
    if await is_rate_limited(
        user_id=user_id,
        limit=limit,
        period=period):

        return True

    return False
