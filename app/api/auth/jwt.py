from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.api.dependencies.user_deps import get_current_user
from app.core.security import create_access_token, create_refresh_token

from app.services.user_service import UserService
from app.schemas.auth_schema import TokenSchema
from app.schemas.user_schema import UserAuthentication
from app.models.user_model import User
from app.core.config import settings

from jose import jwt

from app.schemas.auth_schema import TokenPayload

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@auth_router.post("/login", response_model=TokenSchema)
async def login(data: OAuth2PasswordRequestForm = Depends()):
    user = await UserService.authenticate_user(
        email=data.username,
        password=data.password
    )

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="E-mail or password is incorrect")

    access_token = create_access_token(user.pk)
    refresh_token = create_refresh_token(user.pk)

    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }

@auth_router.post('/refresh', response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_SECRET_KEY,
            settings.ALGORITHM
        )

        token_data = TokenPayload(**payload)
    except:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="An error ocurred during token validation",
            headers = {'WWW-Authenticate':'Bearer'}
        )

    user = await UserService.get_user_by_id(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Unable to find user"
        )

    return {
        'access_token': create_access_token(user.pk),
        'refresh_token': create_refresh_token(user.pk)
    }
    
@auth_router.post('/test-token')
async def test_access_token(user: User = Depends(get_current_user)):
    return user


