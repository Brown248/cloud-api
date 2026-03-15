🌐 **Live URL:** https://cloud-api-t2ch.onrender.com

---

## 📋 สารบัญ

- [Tech Stack](#-tech-stack)
- [Features](#-features)
- [Architecture](#-architecture)
- [Endpoints](#-endpoints)
- [การติดตั้ง](#-การติดตั้ง)
- [ทดสอบด้วย Postman](#-ทดสอบด้วย-postman)
- [Deploy](#-deploy)

---

## 🛠 Tech Stack

| เทคโนโลยี | การใช้งาน |
|---|---|
| **FastAPI** | สร้าง REST API |
| **PostgreSQL** | Database บน Cloud |
| **SQLAlchemy** | ORM จัดการ Database |
| **Pydantic** | Validate ข้อมูล Request/Response |
| **Render** | Cloud Deployment |
| **Postman** | ทดสอบ API |
| **Git / GitHub** | Version Control |

---

## ✨ Features

- ✅ CRUD API ครบ — GET, POST, DELETE
- ✅ 3 Endpoints หลัก — Temperature, Sales, Data
- ✅ PostgreSQL บน Cloud (Render)
- ✅ รองรับ SQLite สำหรับ Local Development
- ✅ Auto-generate Docs ด้วย Swagger UI
- ✅ Validation ด้วย Pydantic

---

## 🏗 Architecture

```
User → Postman / Browser
         │
         ▼
   FastAPI (Render)
         │
         ▼
   SQLAlchemy ORM
         │
         ▼
  PostgreSQL Database
```

---

## 📡 Endpoints

### 🌡️ Temperature

| Method | Endpoint | คำอธิบาย |
|---|---|---|
| `POST` | `/temperature` | บันทึกข้อมูลอุณหภูมิ |
| `GET` | `/temperature` | ดูข้อมูลอุณหภูมิทั้งหมด |
| `GET` | `/temperature/{id}` | ดูข้อมูลตาม ID |
| `DELETE` | `/temperature/{id}` | ลบข้อมูลตาม ID |

**ตัวอย่าง Request:**
```json
POST /temperature
{
  "location": "Bangkok",
  "value": 38.5,
  "unit": "celsius"
}
```

**ตัวอย่าง Response:**
```json
{
  "id": 1,
  "location": "Bangkok",
  "value": 38.5,
  "unit": "celsius",
  "recorded_at": "2026-03-15T10:00:00"
}
```

---

### 💰 Sales

| Method | Endpoint | คำอธิบาย |
|---|---|---|
| `POST` | `/sales` | บันทึกข้อมูลการขาย |
| `GET` | `/sales` | ดูข้อมูลการขายทั้งหมด |
| `GET` | `/sales/summary` | สรุปยอดขายรวม |

**ตัวอย่าง Request:**
```json
POST /sales
{
  "product": "iPhone 15",
  "amount": 29900.00,
  "quantity": 2
}
```

**ตัวอย่าง Response (summary):**
```json
{
  "total_orders": 1,
  "total_items": 2,
  "total_revenue": 59800.0
}
```

---

### 📦 Data

| Method | Endpoint | คำอธิบาย |
|---|---|---|
| `POST` | `/data` | บันทึกข้อมูลทั่วไป |
| `GET` | `/data` | ดูข้อมูลทั้งหมด |
| `GET` | `/data/{key}` | ค้นหาตาม key |

**ตัวอย่าง Request:**
```json
POST /data
{
  "key": "humidity",
  "value": "75%"
}
```

---

## 💻 การติดตั้ง

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/cloud-api.git
cd cloud-api
```

### 2. สร้าง Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

### 4. ตั้งค่า Environment Variables
สร้างไฟล์ `.env`:
```env
# Local (SQLite)
DATABASE_URL=sqlite:///./mydb.db

# Cloud (PostgreSQL)
DATABASE_URL=postgresql://user:password@host/dbname
```

### 5. รัน Server
```bash
uvicorn main:app --reload
```

เปิด Browser → **http://127.0.0.1:8000/docs**

---

## 🧪 ทดสอบด้วย Postman

1. เปิด Postman
2. เลือก Method `POST`
3. ใส่ URL `http://127.0.0.1:8000/temperature`
4. คลิก **Body** → **raw** → **JSON**
5. วาง JSON แล้วกด **Send**

หรือทดสอบผ่าน Swagger UI ได้เลยที่:
```
https://cloud-api-t2ch.onrender.com/docs
```

---

## 🚀 Deploy

โปรเจคนี้ Deploy บน **Render** โดยใช้:
- **Web Service** — รัน FastAPI
- **PostgreSQL** — Database

ขั้นตอน Deploy:
1. Push โค้ดขึ้น GitHub
2. เชื่อม Render กับ GitHub repo
3. ตั้งค่า Environment Variable `DATABASE_URL`
4. กด Deploy

---