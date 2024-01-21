from fastapi import APIRouter

from app.schemas.user_schema import UserAuthentication
from app.services.user_service import UserService


user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user_router.post('/create/')
async def create_user(user_data: UserAuthentication):
    # Handler que processa pedido de criação de usuário
    user = UserService.create_user(user_data) 

    return {'data': user}
