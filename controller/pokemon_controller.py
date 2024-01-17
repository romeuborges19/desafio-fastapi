from typing import Union
from fastapi import APIRouter, Request
from controller.utils import get_request_url
from service.pokemon_service import *

from repository.pokemon_cache import Cache

pokemon_router = APIRouter(
    prefix='/pokemon',
    tags=['pokemon']
)

cache = Cache()

@pokemon_router.get('/')
async def get_pokemon_data(name:str, request: Request):
    response_data = []
    response_data = await get_pokemon_by_name(name)

    return response_data

@pokemon_router.get('/type')
async def get_pokemon_data_by_type(name:str, request: Request):
    url = get_request_url(request.url) 

    if cache.exists(url):
        response = cache.rd.get(url)
        return response

    response = await get_pokemon_type_data(name)
    return response
