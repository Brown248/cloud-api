# ☁️ Cloud API — FastAPI + SQLite

REST API สำหรับเก็บข้อมูล Temperature, Sales และ Data  
Deploy บน Render Cloud

---

## 🛠️ Tech Stack

- **FastAPI** — Python Web Framework
- **SQLAlchemy** — ORM
- **SQLite** (Local) / **PostgreSQL** (Cloud)
- **Render** — Cloud Deployment
- **Postman** — API Testing

---

## 📁 Project Structure
```
cloud-api/
├── main.py         # API Endpoints
├── models.py       # Database Models
├── schemas.py      # Request/Response Schema
├── database.py     # Database Connection
├── requirements.txt
└── .env            # Environment Variables (ไม่ได้ push)
```

---

## 🚀 Run Locally
```bash
# 1. Clone repo
git clone https://github.com/yourusername/cloud-api.git
cd cloud-api

# 2. สร้าง Virtual Environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# 3. ติดตั้ง Dependencies
pip install -r requirements.txt

# 4. สร้างไฟล์ .env
echo DATABASE_URL=sqlite:///./mydb.db > .env

# 5. รัน Server
uvicorn main:app --reload
```

เปิด → http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

### 🌡️ Temperature

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/temperature` | บันทึกค่าอุณหภูมิ |
| GET | `/temperature` | ดูข้อมูลทั้งหมด |
| GET | `/temperature/{id}` | ดูตาม ID |
| DELETE | `/temperature/{id}` | ลบตาม ID |

**POST /temperature — Request Body**
```json
{
    "location": "Bangkok",
    "value": 38.5,
    "unit": "celsius"
}
```

---

### 💰 Sales

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/sales` | บันทึกการขาย |
| GET | `/sales` | ดูข้อมูลทั้งหมด |
| GET | `/sales/summary` | ดูยอดขายรวม |

**POST /sales — Request Body**
```json
{
    "product": "iPhone 15",
    "amount": 29900.00,
    "quantity": 2
}
```

---

### 📦 Data

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/data` | บันทึกข้อมูลทั่วไป |
| GET | `/data` | ดูข้อมูลทั้งหมด |
| GET | `/data/{key}` | ค้นหาตาม key |

**POST /data — Request Body**
```json
{
    "key": "humidity",
    "value": "75%"
}
```

---

## 🌐 Live Demo

> https://your-app-name.onrender.com


---