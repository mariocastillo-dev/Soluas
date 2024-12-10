from sqlalchemy.orm import Session
from app.models.kpi import KPI
from datetime import datetime

class KPICRUD:
    def __init__(self, session: Session):
        self.session = session

    def create_kpi(self, name: str, description: str, category: str, 
                   value: float, unit: str, customer_id: int):
        try:
            new_kpi = KPI(
                name=name, 
                description=description, 
                category=category,
                value=value, 
                unit=unit, 
                customer_id=customer_id,
                created_at=datetime.now()
            )
            self.session.add(new_kpi)
            self.session.commit()
            return "KPI created successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"
        finally:
            self.session.close()

    def get_kpis(self, customer_id: int = None, category: str = None):
        try:
            query = self.session.query(KPI)
            if customer_id:
                query = query.filter(KPI.customer_id == customer_id)
            if category:
                query = query.filter(KPI.category == category)
            return query.all()
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def update_kpi(self, kpi_id: int, **kwargs):
        try:
            kpi = self.session.query(KPI).filter(KPI.id_kpi == kpi_id).first()
            if not kpi:
                return "KPI not found."
            
            for key, value in kwargs.items():
                setattr(kpi, key, value)
            
            self.session.commit()
            return "KPI updated successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"
        finally:
            self.session.close()

    def delete_kpi(self, kpi_id: int):
        try:
            kpi = self.session.query(KPI).filter(KPI.id_kpi == kpi_id).first()
            if not kpi:
                return "KPI not found."
            
            self.session.delete(kpi)
            self.session.commit()
            return "KPI deleted successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"
        finally:
            self.session.close()