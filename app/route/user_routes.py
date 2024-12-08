from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.user_schema import UserCreate
from app.core.database import get_db
from app.crud.user_crud import UserCRUD
from app.core.security import verify_password, create_access_token, get_password_hash
from datetime import timedelta
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/create-user", response_model=dict)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_crud = UserCRUD(db)
    response = user_crud.create_user(user.ID_documento, user.nombre, user.email, user.password, user.role_name)
    if response == "User registered successfully.":
        return {"status": "success", "message": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)

@router.get("/", response_model=dict)
def get_users(db: Session = Depends(get_db)):
    user_crud = UserCRUD(db)
    users = user_crud.get_all_users()
    if isinstance(users, str):
        raise HTTPException(status_code=500, detail=users)
    data = []
    for u in users:
        data.append({
            "ID_documento": u.ID_documento,
            "nombre": u.nombre,
            "email": u.email,
            "role_id": u.role_id
        })
    return {"status": "success", "data": data}

@router.get("/{ID_documento}", response_model=dict)
def get_user(ID_documento: int, db: Session = Depends(get_db)):
    user_crud = UserCRUD(db)
    user = user_crud.get_user_by_ID_documento(ID_documento)
    if isinstance(user, str):
        raise HTTPException(status_code=500, detail=user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "status": "success",
        "data": {
            "ID_documento": user.ID_documento,
            "nombre": user.nombre,
            "email": user.email,
            "role_id": user.role_id
        }
    }

@router.put("/{ID_documento}", response_model=dict)
def update_user(ID_documento: int, nombre: Optional[str] = None, email: Optional[str] = None, db: Session = Depends(get_db)):
    user_crud = UserCRUD(db)
    response = user_crud.update_user(ID_documento, nombre=nombre, email=email)
    if response == "User updated successfully.":
        return {"status": "success", "message": response}
    elif response == "User not found.":
        raise HTTPException(status_code=404, detail=response)
    elif response == "Another user with this email already exists.":
        raise HTTPException(status_code=400, detail=response)
    else:
        raise HTTPException(status_code=500, detail=response)

@router.delete("/{ID_documento}", response_model=dict)
def delete_user(ID_documento: int, db: Session = Depends(get_db)):
    user_crud = UserCRUD(db)
    response = user_crud.delete_user(ID_documento)
    if response == "User deleted successfully.":
        return {"status": "success", "message": response}
    elif response == "User not found.":
        raise HTTPException(status_code=404, detail=response)
    else:
        raise HTTPException(status_code=500, detail=response)
