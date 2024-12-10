from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base

role_permissions = Table(
    'role_permissions',
    Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id_role'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permissions.id_permission'), primary_key=True)
)

class Permission(Base):
    __tablename__ = 'permissions'

    id_permission = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
