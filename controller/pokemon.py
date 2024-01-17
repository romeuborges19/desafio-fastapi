import httpx

async def get_pokemon_by_name(name:str):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    url_request = f'{url}{name}'

    async with httpx.AsyncClient() as http_client:
        response = await http_client.get(url_request)

        if response.status_code == 200:
            json = response.json()
            return {name: json}
        else: 
            return {'Erro': 'Erro na requisição'}
