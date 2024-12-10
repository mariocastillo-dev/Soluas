from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.kpi_schema import KPICreate
from app.crud.kpi_crud import KPICRUD
from typing import Optional

router = APIRouter()

@router.post("/", response_model=dict)
def create_kpi(kpi: KPICreate, db: Session = Depends(get_db)):
    kpi_crud = KPICRUD(db)
    response = kpi_crud.create_kpi(
        name=kpi.name,
        description=kpi.description,
        category=kpi.category,
        value=kpi.value,
        unit=kpi.unit,
        customer_id=kpi.customer_id
    )
    
    if response == "KPI created successfully.":
        return {"status": "success", "message": response}
    else:
        raise HTTPException(status_code=400, detail=response)

@router.get("/", response_model=dict)
def get_kpis(customer_id: Optional[int] = None, category: Optional[str] = None, db: Session = Depends(get_db)):
    kpi_crud = KPICRUD(db)
    kpis = kpi_crud.get_kpis(customer_id, category)
    
    if isinstance(kpis, str):
        raise HTTPException(status_code=500, detail=kpis)
    
    return {"status": "success", "data": [kpi.as_dict() for kpi in kpis]}

@router.put("/{kpi_id}", response_model=dict)
def update_kpi(kpi_id: int, kpi: KPICreate, db: Session = Depends(get_db)):
    kpi_crud = KPICRUD(db)
    response = kpi_crud.update_kpi(
        kpi_id, 
        name=kpi.name,
        description=kpi.description,
        category=kpi.category,
        value=kpi.value,
        unit=kpi.unit,
        customer_id=kpi.customer_id
    )
    
    if response == "KPI updated successfully.":
        return {"status": "success", "message": response}
    elif response == "KPI not found.":
        raise HTTPException(status_code=404, detail=response)
    else:
        raise HTTPException(status_code=400, detail=response)

@router.delete("/{kpi_id}", response_model=dict)
def delete_kpi(kpi_id: int, db: Session = Depends(get_db)):
    kpi_crud = KPICRUD(db)
    response = kpi_crud.delete_kpi(kpi_id)
    
    if response == "KPI deleted successfully.":
        return {"status": "success", "message": response}
    elif response == "KPI not found.":
        raise HTTPException(status_code=404, detail=response)
    else:
        raise HTTPException(status_code=400, detail=response)