from decouple import os
from fastapi import HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.middleware.utils import JWTTokenRequest, rate_limiter


class RateLimiterMiddleware(BaseHTTPMiddleware):
    # Middleware de rate limit que segue um algoritmo de 
    # fixed-window rate limiting
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        testing = os.environ.get('PYTEST_CURRENT_TEST')
        if testing:
            return await call_next(request)

        if request.headers.get('Authorization'):
            # A verificação é realizada em endpoints que exigem autenticação,
            # ou seja, nas requisições que se comunicam com a PokéAPI
            user_id = JWTTokenRequest.get_current_user_id(request)
            is_limited = await rate_limiter(user_id)

            if not is_limited:
                return await call_next(request)
        else:
            return await call_next(request)

        raise HTTPException(status_code=429,
                            detail="Rate limit exceeded")
