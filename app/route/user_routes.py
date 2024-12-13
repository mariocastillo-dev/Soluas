from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.schemas.user_schema import UserCreate
from app.core.database import get_db
from app.crud.user_crud import UserCRUD
from app.core.security import get_password_hash, get_current_user, has_permission
from app.models.user import User

router = APIRouter()

@router.post("/create-user", response_model=dict)
def create_user(user: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not has_permission(current_user, "create_user"):
        raise HTTPException(status_code=403, detail="Not authorized to create users")
    user_crud = UserCRUD(db)
    response = user_crud.create_user(user.ID_documento, user.nombre, user.email, user.password, user.role_name)
    if response == "User registered successfully.":
        return {"status": "success", "message": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)

@router.get("/", response_model=dict)
def get_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Verificar permiso
    if not has_permission(current_user, "read_users"):
        raise HTTPException(status_code=403, detail="Not authorized to read users")

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
def get_user(ID_documento: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Verificar permiso
    if not has_permission(current_user, "read_users"):
        raise HTTPException(status_code=403, detail="Not authorized to read user")

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
def update_user(ID_documento: int, nombre: Optional[str] = None, email: Optional[str] = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not has_permission(current_user, "update_user"):
        raise HTTPException(status_code=403, detail="Not authorized to update users")
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
def delete_user(ID_documento: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not has_permission(current_user, "delete_user"):
        raise HTTPException(status_code=403, detail="Not authorized to delete users")
    user_crud = UserCRUD(db)
    response = user_crud.delete_user(ID_documento)
    if response == "User deleted successfully.":
        return {"status": "success", "message": response}
    elif response == "User not found.":
        raise HTTPException(status_code=404, detail=response)
    else:
        raise HTTPException(status_code=500, detail=response)

@router.put("/change-password", response_model=dict)
def change_password(ID_documento: int, new_password: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Verificar permiso (opcional si solo admin puede cambiar contraseñas de otros usuarios)
    if not has_permission(current_user, "update_password"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to change passwords")

    # Buscar al usuario en la base de datos
    user_crud = UserCRUD(db)
    user = user_crud.get_user_by_ID_documento(ID_documento)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    try:
        # Generar el hash de la nueva contraseña
        hashed_password = get_password_hash(new_password)

        # Actualizar la contraseña del usuario
        user.hashed_password = hashed_password
        db.commit()

        return {
            "status": "success",
            "message": "Password updated successfully."
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred: {str(e)}")