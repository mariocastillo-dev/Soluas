from sqlalchemy import Column, Integer, String, Float
from .base import Base

class Facts(Base):
    __tablename__ = "facts"

    id_facts = Column(Integer, primary_key=True, autoincrement=True, index=True)
    customer_id = Column(Integer, nullable=False)
    customer_name = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    field = Column(String(100), nullable=False)
    expense = Column(Float, nullable=False)
    budget = Column(Float, nullable=False)

    # Método para convertir a diccionario para facilitar la respuesta JSON
    def as_dict(self):
        return {
            "id": self.id_facts,
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "year": self.year,
            "month": self.month,
            "field": self.field,
            "expense": self.expense,
            "budget": self.budget
        }