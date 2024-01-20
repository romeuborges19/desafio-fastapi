from fastapi import APIRouter, Depends, Request

from app.api.dependencies.user_deps import get_current_user
from app.models.user_model import User
from app.services.pokemon_service import PokemonService

pokemon_router = APIRouter(
    prefix='/pokemon',
    tags=['pokemon']
)

@pokemon_router.get('/{name}', summary="Get pokémon data by name")
async def get_pokemon_data(name:str, request: Request, current_user: User = Depends(get_current_user)):
    url = str(request.url)
    response = await PokemonService.get_pokemon_by_name(name, url, current_user.pk)
    return response

@pokemon_router.get('/{name}/encounters', summary="Get pokémon encounter data by pokemon name")
async def get_pokemon_encounter_data(name:str, request: Request, current_user: User = Depends(get_current_user)):
    url = str(request.url)
    response = await PokemonService.get_pokemon_encounters(name, url)
    return response
