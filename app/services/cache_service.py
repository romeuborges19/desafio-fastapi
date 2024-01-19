import redis
from redis_om import get_redis_connection

class CacheService:
    # Service class for cache lookup
    def __init__(self) -> None:
        self.rd = get_redis_connection() 

    def get(self, key):
        cache = self.rd.get(key)

        if cache:
            return cache 
        return None 

    def set(self, key, value):
        self.rd.set(key, value)

