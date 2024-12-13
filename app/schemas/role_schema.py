from typing import Optional
from pydantic import BaseModel

class Role(BaseModel):
    id_role: int
    role: str

    class Config:
        from_attributes = True

class RoleResponse(BaseModel):
    status: str
    data: Optional[Role]