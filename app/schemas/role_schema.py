from pydantic import BaseModel

class RoleCreate(BaseModel):
    role: str