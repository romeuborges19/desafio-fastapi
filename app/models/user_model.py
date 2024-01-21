import datetime

from redis_om import Field, HashModel, get_redis_connection

from app.core.config import settings

# ORM de usuário no banco de dados
class User(HashModel):
    username: str 
    email: str = Field(index=True)
    hash_password: str
    created_at: datetime.datetime

    def __repr__(self) -> str:
        return f'<User {self.email}>'

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, object: object) -> bool:
        if isinstance(object, User):
            return self.email == object.email
        return False

    class Meta:
        database = get_redis_connection(url=settings.REDIS_DATA_URL)
