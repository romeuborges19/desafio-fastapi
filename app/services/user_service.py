from datetime import datetime
from core.security import get_password
from models.user_model import User
from schemas.user_schema import UserAuthentication


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
