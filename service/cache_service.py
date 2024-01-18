import redis

class CacheService:
    # Service class for cache lookup
    def __init__(self) -> None:
        self.rd = redis.Redis(host="localhost", port=6379, db=0)

    def get(self, key):
        cache = self.rd.get(key)

        if cache:
            return cache 
        return None 

    def set(self, key, value):
        self.rd.set(key, value)

