from pydantic.v1 import EmailStr
from models.user_model import User
from schemas.user_schema import UserAuthentication
from services.user_service import UserService
from fastapi import APIRouter, Depends

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@user_router.post('/create/')
async def create_user(user_data: UserAuthentication):
    # print(f'tipo do email: {type(user_data.email)}')
    user_data.email = EmailStr(user_data.email)
    print(user_data.email)
    user = await UserService.create_user(user_data) 

    return {'data': user}
