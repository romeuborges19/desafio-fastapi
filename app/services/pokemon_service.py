from app.api.utils import get_pokemon_data


class PokemonService:
    # Classe de serviço que se comunica com a PokeAPI

    @staticmethod
    async def get_pokemon_by_name(name:str, key:str):
        # Obtém dados de um pokemon através do seu nome
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'

        response = await get_pokemon_data(url, key)

        return {name: response}

    @staticmethod
    async def get_pokemon_encounters(name:str, key:str):
        # Obtém dados sobre os locais onde é possível encontrar um pokémon
        url = f'https://pokeapi.co/api/v2/pokemon/{name}/encounters'

        response = await get_pokemon_data(url, key)

        return {name: response}

