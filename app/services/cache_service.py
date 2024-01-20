from redis_om import get_redis_connection
from app.core.config import settings


class CacheService:
    # Classe de serviço responsável por verificar cache 

    def conn(self, url:str = settings.REDIS_CACHE_URL):
        self.rd = get_redis_connection(
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

cache = CacheService()
