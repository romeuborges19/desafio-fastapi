import datetime
from core.config import settings
from pydantic import EmailStr, Field
from redis_om import HashModel, get_redis_connection

class User(HashModel):
    username: str 
    email: str = Field(EmailStr)
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

    class Config:
        orm_mode = True
