from sqlalchemy.orm import Session
from app.models.role import Role

class RoleCRUD:
    def __init__(self, session: Session):
        self.session = session

    def create_role(self, role_name):
        try:
            # Check if the role already exists
            existing_role = self.session.query(Role).filter(Role.role == role_name).first()
            if existing_role:
                return "Role already exists."

            # Create and store the new role
            new_role = Role(role=role_name)
            self.session.add(new_role)
            self.session.commit()
            return "Role created successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"
        finally:
            self.session.close()