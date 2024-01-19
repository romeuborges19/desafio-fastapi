from redis_om import get_redis_connection

class CacheService:
    # Service class for cache lookup

    def conn(self, url:str = 'redis//localhost:6379'):
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
