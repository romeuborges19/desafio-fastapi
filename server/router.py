from fastapi import APIRouter
import httpx
from controller.pokemon import get_pokemon_by_name

pokemon_router = APIRouter(
    prefix='/pokemon',
    tags=['pokemon']
)

@pokemon_router.get('/{name}')
async def read_pokemon_by_name(name:str):
    response = await get_pokemon_by_name(name)
    return response 
