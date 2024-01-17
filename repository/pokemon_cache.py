import redis
import requests
import json

# def read_pokemon_type(type_name:str, url:str):
#     cache = rd.get(type_name)
#     if cache:
#         return json.loads(cache)
#     else:
#         response = requests.get(url)
#         rd.set(type_name, response.text)
#         return response.json()

class Cache:
    def __init__(self) -> None:
        self.rd = redis.Redis(host="localhost", port=6379, db=0)

    def exists(self, key:str):
        cache = self.rd.get(key)

        if cache:
            return True
        return False

    def set_cache(self, key, value):
        self.rd.set(key, value)

