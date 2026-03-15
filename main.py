from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import engine, get_db

# สร้างตารางใน Database อัตโนมัติตอนรันครั้งแรก
models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="My Cloud API",
    description="API สำหรับเก็บข้อมูล Temperature, Sales และ Data",
    version="1.0.0"
)


# TEMPERATURE ENDPOINTS

@app.post("/temperature", response_model=schemas.TemperatureResponse, tags=["Temperature"])
def create_temperature(data: schemas.TemperatureCreate, db: Session = Depends(get_db)):
    """บันทึกค่าอุณหภูมิใหม่"""
    record = models.Temperature(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@app.get("/temperature", response_model=List[schemas.TemperatureResponse], tags=["Temperature"])
def get_all_temperatures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """ดึงข้อมูลอุณหภูมิทั้งหมด"""
    records = db.query(models.Temperature).offset(skip).limit(limit).all()
    return records


@app.get("/temperature/{id}", response_model=schemas.TemperatureResponse, tags=["Temperature"])
def get_temperature_by_id(id: int, db: Session = Depends(get_db)):
    """ดึงข้อมูลอุณหภูมิตาม ID"""
    record = db.query(models.Temperature).filter(models.Temperature.id == id).first()
    if not record:
        raise HTTPException(status_code=404, detail="ไม่พบข้อมูล")
    return record


@app.delete("/temperature/{id}", tags=["Temperature"])
def delete_temperature(id: int, db: Session = Depends(get_db)):
    """ลบข้อมูลอุณหภูมิตาม ID"""
    record = db.query(models.Temperature).filter(models.Temperature.id == id).first()
    if not record:
        raise HTTPException(status_code=404, detail="ไม่พบข้อมูล")
    db.delete(record)
    db.commit()
    return {"message": f"ลบข้อมูล ID {id} สำเร็จ"}


# SALES ENDPOINTS

@app.post("/sales", response_model=schemas.SaleResponse, tags=["Sales"])
def create_sale(data: schemas.SaleCreate, db: Session = Depends(get_db)):
    """บันทึกข้อมูลการขายใหม่"""
    record = models.Sales(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@app.get("/sales", response_model=List[schemas.SaleResponse], tags=["Sales"])
def get_all_sales(db: Session = Depends(get_db)):
    """ดึงข้อมูลการขายทั้งหมด"""
    return db.query(models.Sales).all()


@app.get("/sales/summary", tags=["Sales"])
def get_sales_summary(db: Session = Depends(get_db)):
    """สรุปยอดขายรวม"""
    sales = db.query(models.Sales).all()
    total_revenue = sum(s.amount * s.quantity for s in sales)
    total_items   = sum(s.quantity for s in sales)
    return {
        "total_orders":  len(sales),
        "total_items":   total_items,
        "total_revenue": round(total_revenue, 2)
    }


# DATA ENDPOINTS

@app.post("/data", response_model=schemas.DataResponse, tags=["Data"])
def create_data(data: schemas.DataCreate, db: Session = Depends(get_db)):
    """บันทึกข้อมูลทั่วไป"""
    record = models.DataRecord(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@app.get("/data", response_model=List[schemas.DataResponse], tags=["Data"])
def get_all_data(db: Session = Depends(get_db)):
    """ดึงข้อมูลทั้งหมด"""
    return db.query(models.DataRecord).all()


@app.get("/data/{key}", tags=["Data"])
def get_data_by_key(key: str, db: Session = Depends(get_db)):
    """ค้นหาข้อมูลตาม key"""
    records = db.query(models.DataRecord).filter(models.DataRecord.key == key).all()
    if not records:
        raise HTTPException(status_code=404, detail=f"ไม่พบข้อมูล key='{key}'")
    return records


# ROOT

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "My Cloud API is running ",
        "docs":    "/docs",
        "endpoints": ["/temperature", "/sales", "/data"]
    }