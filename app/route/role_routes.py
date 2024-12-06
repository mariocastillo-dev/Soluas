from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.role_schema import RoleCreate
from app.core.database import get_db
from app.crud.role_crud import RoleCRUD
from app.models.user import User
from app.core.security import verify_password
from app.core.database import get_db

router = APIRouter()

@router.post("/create-role", response_model=dict)
def create_role(role: RoleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_db)):
    if current_user.role != "Admin":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    role_crud = RoleCRUD(db)
    response = role_crud.create_role(role.role)
    if response == "Role created successfully.":
        return {"status": "success", "message": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)