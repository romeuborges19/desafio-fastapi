import json

from fastapi import HTTPException, status
import httpx

from app.services.cache_service import cache

async def get_response(url:str):
    # Função que obtém resposta da API
    async with httpx.AsyncClient() as http_client:
        response = await http_client.get(url)

        if response.status_code == 200:
            return response
        else: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Pokemon not found.") 

def get_key(url):
    # Função que gera chave para armazenar pesquisas em cache
    key = str(url)
    key = key.replace('http://127.0.0.1:8000', '')
    return key

async def get_pokemon_data(url:str, key:str):
    # Função que obtém os dados da API. Caso a pesquisa 
    # já tenha sido realizada, ela retornará os dados salvos em cache

    key = get_key(key)
    cache_data = cache.get(key)
    if cache_data:
        return json.loads(cache_data)

    response = await get_response(url)

    if not response:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail="No content was returned")

    cache.set(key, response.text)
    return response.json()
