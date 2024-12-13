from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.user import User
from app.models.role import Role
from app.core.security import get_password_hash

class UserCRUD:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, ID_documento, nombre, email, password, role_name):
        try:
            # Check if the role exists
            role = self.session.query(Role).filter(Role.role == role_name).first()
            if not role:
                return "Role does not exist. Please create the role first."

            # Check if the user already exists
            existing_user = self.session.query(User).filter(or_(User.ID_documento == ID_documento, User.email == email)).first()
            if existing_user:
                return "User with this ID_documento or email already exists."

            # Hash the password
            hashed_password = get_password_hash(password)

            # Create and store the new user
            new_user = User(ID_documento=ID_documento, nombre=nombre, email=email, hashed_password=hashed_password, role_id=role.id_role)
            self.session.add(new_user)
            self.session.commit()
            return "User registered successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"

    def get_all_users(self):
        try:
            users = self.session.query(User).all()
            return users
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def get_user_by_ID_documento(self, ID_documento: int):
        try:
            user = self.session.query(User).filter(User.ID_documento == ID_documento).first()
            return user
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def update_user(self, ID_documento, nombre=None, email=None):
        try:
            user = self.session.query(User).filter(User.ID_documento == ID_documento).first()
            if not user:
                return "User not found."

            # Update user details if new values are provided
            if nombre:
                user.nombre = nombre
            if email:
                # Verificar que el nuevo email no exista ya en otro usuario
                existing_user = self.session.query(User).filter(User.email == email, User.ID_documento != ID_documento).first()
                if existing_user:
                    return "Another user with this email already exists."
                user.email = email
            
            self.session.commit()
            return "User updated successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"

    def delete_user(self, ID_documento):
        try:
            user = self.session.query(User).filter(User.ID_documento == ID_documento).first()
            if not user:
                return "User not found."

            self.session.delete(user)
            self.session.commit()
            return "User deleted successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"