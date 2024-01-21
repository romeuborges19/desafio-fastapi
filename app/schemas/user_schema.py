from pydantic import BaseModel, EmailStr, Field

# Dados esperados durante a criação de um usuário
class UserAuthentication(BaseModel):
    username: str = Field(..., min_length=5, max_length=50, description="User's username")
    email: EmailStr = Field(..., description="User's e-mail")
    password: str = Field(..., min_length=5, max_length=20, description="User's password")
