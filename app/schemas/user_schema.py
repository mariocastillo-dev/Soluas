from pydantic import BaseModel

class UserCreate(BaseModel):
    ID_documento: int
    nombre: str
    email: str
    password: str
    role_name: str