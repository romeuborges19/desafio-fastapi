from datetime import datetime
from typing import Optional
from fastapi import HTTPException, status

from redis_om import NotFoundError

from app.core.security import get_password, verify_password
from app.models.user_model import User
from app.schemas.user_schema import UserAuthentication


class UserService:
    # Classe de serviço responsável por se comunicar com o model User
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
            try:
                user = User.get(user.first().pk)
            except NotFoundError:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
        else:
            user = None

        return user

    @staticmethod
    async def get_user_by_id(user_pk: str) -> Optional[User]:
        try:
            user = User.get(user_pk)
        except NotFoundError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    @staticmethod
    async def authenticate_user(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email)

        if not user:
            return None
        
        if not verify_password(password=password, hashed_password=user.hash_password):
            return None

        return user
