
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.facts import Facts

router = APIRouter()

@router.get("/facts", response_model=dict)
def get_facts_data(year: int = None, month: int = None, db: Session = Depends(get_db)):
    try:
        query = db.query(Facts)
        if year:
            query = query.filter(Facts.year == year)
        if month:
            query = query.filter(Facts.month == month)
        
        result = query.all()
        return {"status": "success", "data": [fact.as_dict() for fact in result]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
