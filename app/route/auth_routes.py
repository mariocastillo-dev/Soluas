from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from app.schemas.auth_schema import AuthLogin, TokenResponse
from app.core.database import get_db
from app.models.user import User
from app.core.security import verify_password, create_access_token

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(credentials: AuthLogin, db: Session = Depends(get_db)):
    # Buscar el usuario por email
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    # Verificar password
    if not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    # Crear el token
    access_token = create_access_token(data={
    "sub": user.email,
    "role_id": user.role_id,
    "nombre": user.nombre,
    "ID_documento": user.ID_documento
    })
    return {"access_token": access_token, "token_type": "bearer"}