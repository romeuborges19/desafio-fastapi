from pydantic import BaseModel

# Dados esperados no retorno de tokens de acesso por endpoints
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

# Dados esperados no retorno do payload de um token
class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None

