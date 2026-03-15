from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ---------- Temperature ----------
class TemperatureCreate(BaseModel):
    location: str
    value: float
    unit: Optional[str] = "celsius"

class TemperatureResponse(BaseModel):
    id: int
    location: str
    value: float
    unit: str
    recorded_at: datetime

    model_config = {"from_attributes": True}  # Pydantic V2


# ---------- Sales ----------
class SaleCreate(BaseModel):
    product: str
    amount: float
    quantity: Optional[int] = 1

class SaleResponse(BaseModel):       # ← ชื่อนี้ต้องตรงกับ main.py
    id: int
    product: str
    amount: float
    quantity: int
    recorded_at: datetime

    model_config = {"from_attributes": True}


# ---------- Data ----------
class DataCreate(BaseModel):
    key: str
    value: str

class DataResponse(BaseModel):
    id: int
    key: str
    value: str
    recorded_at: datetime

    model_config = {"from_attributes": True}