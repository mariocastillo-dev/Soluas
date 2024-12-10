from sqlalchemy.orm import Session
from app.models.role import Role

class RoleCRUD:
    def __init__(self, session: Session):
        self.session = session

    def create_role(self, role_name):
        try:
            existing_role = self.session.query(Role).filter(Role.role == role_name).first()
            if existing_role:
                return "Role already exists."
            new_role = Role(role=role_name)
            self.session.add(new_role)
            self.session.commit()
            return "Role created successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"

    def get_all_roles(self):
        try:
            roles = self.session.query(Role).all()
            return roles
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def get_role_by_id(self, role_id: int):
        try:
            role = self.session.query(Role).filter(Role.id_role == role_id).first()
            return role
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def update_role(self, role_id: int, new_role_name: str):
        try:
            role = self.session.query(Role).filter(Role.id_role == role_id).first()
            if not role:
                return "Role not found."
            # Verificar si el nuevo nombre ya existe
            existing_role = self.session.query(Role).filter(Role.role == new_role_name).first()
            if existing_role and existing_role.id_role != role_id:
                return "Another role with this name already exists."

            role.role = new_role_name
            self.session.commit()
            return "Role updated successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"

    def delete_role(self, role_id: int):
        try:
            role = self.session.query(Role).filter(Role.id_role == role_id).first()
            if not role:
                return "Role not found."
            self.session.delete(role)
            self.session.commit()
            return "Role deleted successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"