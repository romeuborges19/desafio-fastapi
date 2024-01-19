from datetime import datetime
from typing import Optional

from redis_om import Migrator
from app.core.security import get_password, verify_password
from app.models.user_model import User
from app.schemas.user_schema import UserAuthentication


class UserService:
    @staticmethod
    async def create_user(user_data: UserAuthentication):
        user = User(
            username=user_data.username,
            email=user_data.email,
            hash_password=get_password(user_data.password),
            created_at=datetime.now(),
        ) 

        user.save()
        return user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = User.find(User.email == email)       

        if user.count():
            user = User.get(user.first().pk)
        else:
            user = None

        return user

    @staticmethod
    async def get_user_by_username(username: str) -> Optional[User]:
        user = User.find(User.username == username).first()
        user = User.get(user.pk)

        return user

    @staticmethod
    async def authenticate_user(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email)

        if not user:
            return None
        
        if not verify_password(password=password, hashed_password=user.hash_password):
            return None

        return user
