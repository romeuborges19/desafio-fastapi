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
        elif response.status_code == 404: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Pokémon not found or does not exist") 
        else:
            raise HTTPException(status_code=response.status_code,
                    detail="Error while fetching data from API") 

def get_key(url):
    # Função que obtém parte da url de pesquisa para gerar 
    # chave para armazenamento em cache
    key = str(url)
    index = key.index('/api')
    key = key[index:]

    return key

async def get_pokemon_data(url:str, key:str, user_pk: str):
    # Função que obtém os dados da API. Caso a pesquisa 
    # já tenha sido realizada, ela retornará os dados salvos em cache

    key = get_key(key)
    cache_key = f"{user_pk}:{key}"
    cache_data = cache.get(cache_key)
    if cache_data:
        return json.loads(cache_data)

    response = await get_response(url)

    if not response:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail="No content was returned")

    cache.set(cache_key, response.text)
    return response.json()
