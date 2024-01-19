from fastapi import APIRouter
from app.api.auth import jwt
from app.api.v1.handlers import pokemon, user

router = APIRouter()

router.include_router(pokemon.pokemon_router)
router.include_router(user.user_router)
router.include_router(jwt.auth_router)
