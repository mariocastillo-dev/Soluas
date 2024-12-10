from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.role_schema import Role
from app.core.database import get_db
from app.crud.role_crud import RoleCRUD
from app.models.user import User
from app.core.security import get_current_user, has_permission

router = APIRouter()

@router.post("/create-role", response_model=dict)
def create_role(role: Role, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not has_permission(current_user, "create_role"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to create roles")
    role_crud = RoleCRUD(db)
    response = role_crud.create_role(role.role)
    if response == "Role created successfully.":
        return {"status": "success", "message": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)

@router.get("/", response_model=dict)
def get_roles(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not has_permission(current_user, "read_roles"):
        raise HTTPException(status_code=403, detail="Not authorized to read roles")
    role_crud = RoleCRUD(db)
    roles = role_crud.get_all_roles()
    if isinstance(roles, str):
        raise HTTPException(status_code=500, detail=roles)
    data = [{"id_role": r.id_role, "role": r.role} for r in roles]
    return {"status": "success", "data": data}


@router.get("/{role_id}", response_model=dict)
def get_role(role_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not has_permission(current_user, "read_roles"):
        raise HTTPException(status_code=403, detail="Not authorized to read roles")
    role_crud = RoleCRUD(db)
    role = role_crud.get_role_by_id(role_id)
    if isinstance(role, str):
        # Hubo un error
        raise HTTPException(status_code=500, detail=role)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"status": "success", "data": {"id_role": role.id_role, "role": role.role}}

@router.put("/{role_id}", response_model=dict)
def update_role(role_id: int, new_role_name: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not has_permission(current_user, "update_role"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update roles")
    role_crud = RoleCRUD(db)
    response = role_crud.update_role(role_id, new_role_name)
    if response == "Role updated successfully.":
        return {"status": "success", "message": response}
    elif response == "Role not found.":
        raise HTTPException(status_code=404, detail=response)
    elif response == "Another role with this name already exists.":
        raise HTTPException(status_code=400, detail=response)
    else:
        raise HTTPException(status_code=500, detail=response)

router.delete("/{role_id}", response_model=dict)
def delete_role(role_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not has_permission(current_user, "delete_role"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete roles")
    role_crud = RoleCRUD(db)
    response = role_crud.delete_role(role_id)
    if response == "Role deleted successfully.":
        return {"status": "success", "message": response}
    elif response == "Role not found.":
        raise HTTPException(status_code=404, detail=response)
    else:
        raise HTTPException(status_code=500, detail=response)