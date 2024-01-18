from app.core.security import get_password
from app.models.user_model import User
from app.schemas.user_schema import UserAuthentication


class UserService:
    @staticmethod
    def create_user(user_data: UserAuthentication):
        user = User(
            username=user_data.username,
            email=user_data.email,
            hash_password=get_password(user_data.password)
        ) 

        return user.save()
