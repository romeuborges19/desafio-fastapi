from fastapi import APIRouter, Request
from services.pokemon_service import PokemonService

pokemon_router = APIRouter(
    prefix='/pokemon',
    tags=['pokemon']
)

@pokemon_router.get('/{name}')
async def get_pokemon_data(name:str, request: Request):
    url = str(request.url)
    response = await PokemonService.get_pokemon_by_name(name, url)
    return response

@pokemon_router.get('/{name}/encounters')
async def get_pokemon_encounter_data(name:str, request: Request):
    url = str(request.url)
    response = await PokemonService.get_pokemon_encounters(name, url)
    return response

# @pokemon_router.get('/type')
# async def get_pokemon_type_data(name:str, request: Request):
#     key = str(request.url)
#     response = await PokemonService.get_pokemon_type_data(name, key)
#     return response

# @pokemon_router.get('/habitat')
# async def get_habitat_data(name:str, request: Request):
#     response = await PokemonService.get_habitat_data(name)
#     return response
