from sqlalchemy import Column, Integer, String, Float, DateTime
from .base import Base

class KPI(Base):
    __tablename__ = "kpis"

    id_kpi = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    category = Column(String(50), nullable=False)
    value = Column(Float, nullable=False)
    unit = Column(String(20), nullable=False)
    customer_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def as_dict(self):
        return {
            "id": self.id_kpi,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "value": self.value,
            "unit": self.unit,
            "customer_id": self.customer_id,
            "created_at": self.created_at.isoformat()
        }