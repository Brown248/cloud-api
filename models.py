from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from database import Base  

# ตาราง temperature_records
class Temperature(Base):
    __tablename__ = "temperature"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)   
    value = Column(Float, nullable=False)    
    unit = Column(String, default="celsius") 
    recorded_at = Column(DateTime, server_default=func.now())

# ตาราง sales_records
class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    recorded_at = Column(DateTime, server_default=func.now())

# ตาราง general data (เก็บข้อมูล key-value)

class DataRecord(Base):
    __tablename__ = "DataRecord"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)
    recorded_at = Column(DateTime, server_default=func.now())


   