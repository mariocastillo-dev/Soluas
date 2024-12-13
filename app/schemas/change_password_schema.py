from pydantic import BaseModel

class ChangePasswordRequest(BaseModel):
    ID_documento: int
    new_password: str