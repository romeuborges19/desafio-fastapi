from jose import jwt
from app.core.config import settings
from datetime import datetime, timedelta
from typing import Any, Union
from passlib.context import CryptContext

password_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

def get_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return password_context.verify(password, hashed_password)

def create_acess_token(subject: Union[str, Any], expires_delta: timedelta | None = None):
    if expires_delta:
        exp = datetime.utcnow() + expires_delta
    else:
        exp = datetime.utcnow() + timedelta(
            minutes=settings.ACESS_TOKEN_EXPIRE_MINUTES
        )

    info_jwt = {
        'exp': exp,
        'sub': str(subject)
    }

    jwt_encoded = jwt.encode(
        info_jwt,
        settings.JWT_SECRET_KEY,
        settings.ALGORITHM
    )

    return jwt_encoded

def create_refresh_token(subject: Union[str, Any], expires_delta: timedelta | None = None):
    if expires_delta:
        exp = datetime.utcnow() + expires_delta
    else:
        exp = datetime.utcnow() + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )

    info_jwt = {
        'exp': exp,
        'sub': str(subject)
    }

    jwt_encoded = jwt.encode(
        info_jwt,
        settings.JWT_REFRESH_SECRET_KEY,
        settings.ALGORITHM
    )

    return jwt_encoded
