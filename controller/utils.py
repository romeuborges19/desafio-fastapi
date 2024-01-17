import httpx

async def get_response(url:str):
    async with httpx.AsyncClient() as http_client:
        response = await http_client.get(url)

        if response.status_code == 200:
            return response
        else: 
            return 'Erro na requisição'

def get_request_url(url):
    url = str(url)
    url = url.replace('http://127.0.0.1:8000', '')
    return url
