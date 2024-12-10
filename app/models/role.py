from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Role(Base):
    __tablename__ = "roles"
    id_role = Column(Integer, primary_key=True, autoincrement=True, index=True)
    role = Column(String(50), unique=True, nullable=False)

    users = relationship("User", back_populates="role")