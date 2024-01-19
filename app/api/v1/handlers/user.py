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
    user = await UserService.create_user(user_data) 

    return {'data': user}
