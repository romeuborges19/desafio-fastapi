import json
from fastapi import HTTPException, status
import httpx

from service.cache_service import CacheService

cache = CacheService()

async def get_response(url:str):
    # Função que obtém resposta da API
    async with httpx.AsyncClient() as http_client:
        response = await http_client.get(url)

        if response.status_code == 200:
            return response.json()
        else: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Pokemon not found.") 

def get_request_url(url):
    # Função que gera chave para armazenar pesquisas em cache
    url = str(url)
    url = url.replace('http://127.0.0.1:8000', '')
    return url

async def get_data_from_api(url:str, key:str):
    # Função que verifica, através do parâmetro 'key', se a pesquisa já foi realizada
    cache_data = cache.get(key)
    if cache_data:
        print('cache')
        return cache_data

    print('sem cache')
    response = await get_response(url)

    if not response:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail="No content was returned")

    cache.set(key, json.dumps(response))
    return response
