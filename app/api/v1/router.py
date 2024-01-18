from fastapi import APIRouter
from api.v1.handlers import pokemon, user

router = APIRouter()

router.include_router(pokemon.pokemon_router)
router.include_router(user.user_router)
