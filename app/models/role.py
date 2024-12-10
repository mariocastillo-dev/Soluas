from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .permission import role_permissions

class Role(Base):
    __tablename__ = "roles"
    id_role = Column(Integer, primary_key=True, autoincrement=True, index=True)
    role = Column(String(50), unique=True, nullable=False)

    users = relationship("User", back_populates="role")
    permissions = relationship("Permission", secondary=role_permissions, backref="roles")

