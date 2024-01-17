from os import stat
import requests
from controller.utils import get_response
import json


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
    @staticmethod
    async def get_pokemon_by_name(name:str):
        # Obtém dados de um pokemon através do seu nome
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = await get_response(url)
        return {name: response}


    @staticmethod
    async def get_pokemon_by_habitat(habitat:str):
        # Obtém dados dos pokemons de uma determinada localização
        url = f'https://pokeapi.co/api/v2/pokemon-habitat/{habitat}'
        response = await get_response(url)
        return {habitat: response}

    @staticmethod
    async def get_pokemon_type_data(pokemon_type:str):
        # Obtém informações sobre tipo
        url = f'https://pokeapi.co/api/v2/type/{pokemon_type}'
        response = read_pokemon_type(pokemon_type, url) 
        return {pokemon_type: response} 

    @staticmethod
    async def get_pokemon_list_by_type(pokemon_type:str):
        # Obtém lista de pokémons por tipo
        url = f'https://pokeapi.co/api/v2/type/{pokemon_type}'
        type_data = await get_response(url)

        response = []
        for pokemon in type_data['pokemon']:
            data = requests.get(pokemon['pokemon']['url'])
            response.append({pokemon['pokemon']['name']: json.loads(data.text)})

        return response

    @staticmethod
    async def get_pokemon_encounter_areas(encounter_areas_url:str):
        response = await get_response(encounter_areas_url)

        return response
