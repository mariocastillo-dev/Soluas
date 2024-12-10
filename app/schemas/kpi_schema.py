from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class KPICreate(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    value: float
    unit: str
    customer_id: int