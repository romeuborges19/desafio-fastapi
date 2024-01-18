from fastapi import APIRouter
from controller.pokemon_controller import pokemon_router


router = APIRouter()
router.include_router(pokemon_router)
