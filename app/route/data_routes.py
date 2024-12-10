
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.facts import Facts
from app.core.security import get_current_user, has_permission
from app.models.user import User

router = APIRouter()

@router.get("/facts", response_model=dict)
def get_facts_data(year: int, customer_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not has_permission(current_user, "read_data"):
        raise HTTPException(status_code=403, detail="Not authorized to read data")
    try:
        query = db.query(Facts).filter(Facts.year == year, Facts.customer_id == customer_id)
        result = query.all()
        return {"status": "success", "data": [fact.as_dict() for fact in result]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")