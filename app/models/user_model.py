from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from redis_om import JsonModel

class User(JsonModel):
    username: str = Field(..., max_length=30)
    email: EmailStr
    hash_password: str
    created_at: datetime = Field(default_factory=datetime.now)

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
