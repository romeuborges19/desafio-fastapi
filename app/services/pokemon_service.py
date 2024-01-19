from api.utils import get_data_from_api

"""
TODO:

1 - Pesquisar por nome FEITO
2 - Pesquisar por região 
3 - Pesquisar por habitat
4 - Pesquisar por cor
5 - Pesquisar por espécie
6 - Pesquisar por tipo FEITO
7 - Pesquisar por habilidades
"""

class PokemonService:
    # Service class for Pokemon Data  

    @staticmethod
    async def get_pokemon_by_name(name:str, key:str):
        # Obtém dados de um pokemon através do seu nome
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'

        response = await get_data_from_api(url, key)

        return {name: response}

    @staticmethod
    async def get_pokemon_encounters(name:str, key:str):
        # Obtém dados sobre os locais onde é possível encontrar um pokémon
        url = f'https://pokeapi.co/api/v2/pokemon/{name}/encounters'

        response = await get_data_from_api(url, key)

        return {name: response}


    # @staticmethod
    # async def get_habitat_data(habitat:str):
    #     # Obtém dados dos pokemons de uma determinada localização
    #     url = f'https://pokeapi.co/api/v2/pokemon-habitat/{habitat}'
    #     response = await get_response(url)
    #     return {habitat: response}

    # @staticmethod
    # async def get_pokemon_type_data(pokemon_type:str, key:str):
    #     # Obtém informações sobre tipo

    #     if cache.exists(key):
    #         data = cache.get(key)
    #         return {pokemon_type: data}
    #     url = f'https://pokeapi.co/api/v2/type/{pokemon_type}'
    #     response = await get_response(url)

    #     return {pokemon_type: response} 

    # @staticmethod
    # async def get_pokemon_list_by_type(pokemon_type:str):
    #     # Obtém lista de pokémons por tipo
    #     url = f'https://pokeapi.co/api/v2/type/{pokemon_type}'
    #     type_data = await get_response(url)

    #     response = []
    #     for pokemon in type_data['pokemon']:
    #         data = requests.get(pokemon['pokemon']['url'])
    #         response.append({pokemon['pokemon']['name']: json.loads(data.text)})

    #     return response

