from fastapi import HTTPException, Request
from jose import jwt
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.core.config import settings
from app.middleware.utils import rate_limiter
from app.schemas.auth_schema import TokenPayload


class RateLimiterMiddleware(BaseHTTPMiddleware):
    # Middleware de rate limit que segue um algoritmo de 
    # fixed-window rate limiting
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        user_id = JWTTokenRequest.get_current_user_id(request)
        print(f'middleware top. user id = {user_id}')
        if user_id:
            is_limited = await rate_limiter(user_id)

            if not is_limited:
                return await call_next(request)
        else:
            return await call_next(request)

        raise HTTPException(status_code=429,
                            detail="Rate limit exceeded")

class JWTTokenRequest:
    @staticmethod
    def get_bearer_token(request: Request):
        auth_token = request.headers.get('Authorization')

        if auth_token:
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
