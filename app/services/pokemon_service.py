from app.services.utils import fetch_api_data 


class PokemonService:
    # Classe de serviço que se comunica com a PokeAPI

    @staticmethod
    async def get_pokemon_by_name(name:str, key:str, user_pk:str):
        # Obtém dados de um pokemon através do seu nome
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'

        response = await fetch_api_data(url, key, user_pk)

        return {name: response}

    @staticmethod
    async def get_pokemon_encounters(name:str, key:str, user_pk:str):
        # Obtém dados sobre os locais onde é possível encontrar um pokémon
        url = f'https://pokeapi.co/api/v2/pokemon/{name}/encounters'

        response = await fetch_api_data(url, key, user_pk)

        return {name: response}

    @staticmethod
    async def get_habitat_by_name(habitat: str, key: str, user_pk:str):
        # Obtém dados sobre os habitats do mundo pokémon através de seu nome
        url = f'https://pokeapi.co/api/v2/pokemon-habitat/{habitat}/'

        response = await fetch_api_data(url, key, user_pk)

        return {habitat: response}

    @staticmethod
    async def get_color_by_name(color: str, key: str, user_pk:str):
        # Obtém dados sobre uma determinada cor de pokémon
        url = f'https://pokeapi.co/api/v2/pokemon-color/{color}/'

        response = await fetch_api_data(url, key, user_pk)

        return {color: response}

    @staticmethod
    async def get_ability_by_name(ability: str, key: str, user_pk:str):
        # Obtém dados sobre uma determinada habilidade
        url = f'https://pokeapi.co/api/v2/ability/{ability}/'

        response = await fetch_api_data(url, key, user_pk)

        return {ability: response}

    @staticmethod
    async def get_type_by_name(pokemon_type: str, key: str, user_pk: str):
        # Obtém dados sobre um determinado tipo de pokémon
        url = f'https://pokeapi.co/api/v2/type/{pokemon_type}/'
        print(url)

        response = await fetch_api_data(url, key, user_pk)

        return {pokemon_type: response}

    @staticmethod
    async def get_species_by_name(species: str, key: str, user_pk: str):
        # Obtém dados sobre uma determinada espécie de pokemon
        url = f'https://pokeapi.co/api/v2/pokemon-species/{species}/'

        response = await fetch_api_data(url, key, user_pk)

        return {species: response}
