from redis_om import get_redis_connection
from app.core.config import settings


class CacheService:
    # Classe de serviço responsável por verificar cache 
    def __init__(self):
        self.rd = self.conn()

    def conn(self, url:str = settings.REDIS_CACHE_URL):
        return get_redis_connection(
            url=url,
            decode_responses=True
        )

    def get(self, key):
        cache = self.rd.get(key)

        if cache:
            return cache 
        return None 

    def set(self, key, value):
        self.rd.set(key, value)

    def add_to_user(self, key, value):
        self.rd.sadd(key, value)

    def get_from_user(self, user_pk, key):
        results = self.rd.sscan(name=user_pk, match=f"*{key}*")
        return results

cache = CacheService()
