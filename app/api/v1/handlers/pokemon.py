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
    url = request.url.path
    response = await PokemonService.get_pokemon_by_name(name, url, current_user.pk)
    return response

@pokemon_router.get('/{name}/encounters', summary="Get pokémon encounter data by pokemon name")
async def get_pokemon_encounter_data(name:str, request: Request, current_user: User = Depends(get_current_user)):
    url = request.url.path
    response = await PokemonService.get_pokemon_encounters(name, url, current_user.pk)
    return response

@pokemon_router.get('/habitat/{habitat}', summary="Get habitat data by its name")
async def get_habitat_data(habitat: str, request: Request, current_user: User = Depends(get_current_user)):
    url = request.url.path
    response = await PokemonService.get_habitat_by_name(habitat, url, current_user.pk)
    return response

@pokemon_router.get('/color/{color}', summary="Get color data by its name")
async def get_color_data(color: str, request: Request, current_user: User = Depends(get_current_user)):
    url = request.url.path
    response = await PokemonService.get_color_by_name(color, url, current_user.pk)
    return response

@pokemon_router.get('/ability/{ability}', summary="Get ability data by its name")
async def get_ability_data(ability: str, request: Request, current_user: User = Depends(get_current_user)):
    url = request.url.path
    response = await PokemonService.get_ability_by_name(ability, url, current_user.pk)
    return response

@pokemon_router.get('/type/{pokemon_type}', summary="Get a pokémon type data by its name")
async def get_type_data(pokemon_type: str, request: Request, current_user: User = Depends(get_current_user)):
    url = request.url.path
    response = await PokemonService.get_type_by_name(pokemon_type, url, current_user.pk)
    return response

@pokemon_router.get('/species/{species}', summary="Get pokémon species data by its name")
async def get_species_data(species: str, request: Request, current_user: User = Depends(get_current_user)):
    url = request.url.path
    response = await PokemonService.get_species_by_name(species, url, current_user.pk)
    return response
