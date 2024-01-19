from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_acess_token, create_refresh_token

from app.services.user_service import UserService

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@auth_router.post("/login")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    user = await UserService.authenticate_user(
        email=data.username,
        password=data.password
    )

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="E-mail or password is incorrect")

    access_token = create_acess_token(user.pk)
    refresh_token = create_refresh_token(user.pk)

    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }
