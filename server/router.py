from typing import Union
from fastapi import APIRouter, Request
from service.pokemon_service import *
from controller.utils import get_request_url
from repository.pokemon_cache import Cache 

pokemon_router = APIRouter(
    prefix='/pokemon',
    tags=['pokemon']
)

cache = Cache()

router = APIRouter()
router.include_router(pokemon_router)
@pokemon_router.get('/')
async def get_pokemon_data(name: Union[str, None] = None, habitat: Union[str, None] = None):
    response_data = []

    if name:
        response_data = await get_pokemon_by_name(name)

    if habitat:
        response_data = await get_pokemon_by_habitat(habitat)

    return response_data

@pokemon_router.get('/type')
async def get_pokemon_data_by_type(name:str, request: Request):
    url = get_request_url(request.url) 

    if cache.exists(url):
        response = cache.rd.get(url)
    else: 
        response = await get_pokemon_type_data(name)

    return response
