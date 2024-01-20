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

async def get_pokemon_data(url:str, key:str, user_pk: str):
    # Função que obtém os dados da API. Caso a pesquisa 
    # já tenha sido realizada, ela retornará os dados salvos em cache

    print('testando')
    cache_key = f"{user_pk}:{key}"
    cache_data = cache.get(cache_key)
    if cache_data:
        print('hit cache')
        return json.loads(cache_data)

    print('no cache')
    response = await get_response(url)
    print(f"response === {response.json()}")

    if not response.json():
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail="No content was returned")

    cache.set(cache_key, response.text)
    return response.json()
