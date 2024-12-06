from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user_schema import UserCreate
from app.core.database import get_db
from app.crud.user_crud import UserCRUD
from app.core.security import verify_password, create_access_token
from datetime import timedelta
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register", response_model=dict)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user_crud = UserCRUD(db)
    response = user_crud.create_user(user.ID_documento, user.nombre, user.email, user.password, user.role_name)
    if response == "User registered successfully.":
        return {"status": "success", "message": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)

@router.post("/login", response_model=dict)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_crud = UserCRUD(db)
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.put("/change-password", response_model=dict)
def change_password(ID_documento: int, new_password: str, db: Session = Depends(get_db)):
    user_crud = UserCRUD(db)
    user = db.query(User).filter(User.ID_documento == ID_documento).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.hashed_password = get_password_hash(new_password)
    db.commit()
    return {"status": "success", "message": "Password updated successfully"}