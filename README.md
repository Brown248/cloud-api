# ☁️ Cloud REST API

A production-ready REST API built with **FastAPI** and **PostgreSQL**, deployed on **Render Cloud**.

🌐 **Live Demo**: https://cloud-api-t2ch.onrender.com/docs

---

## 📌 Overview

This project demonstrates cloud API deployment with a full CRUD backend for storing and retrieving temperature readings, sales records, and general key-value data.

```
User → HTTP Request → FastAPI → PostgreSQL → JSON Response
```

---

## 🚀 Features

- REST API with FastAPI (Python)
- PostgreSQL database with SQLAlchemy ORM
- Auto-generated API documentation (Swagger UI)
- Deployed on Render Cloud (Free Tier)
- Tested with Postman

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| **FastAPI** | Web framework |
| **PostgreSQL** | Database (Cloud) |
| **SQLite** | Database (Local) |
| **SQLAlchemy** | ORM |
| **Pydantic** | Data validation |
| **Uvicorn** | ASGI server |
| **Render** | Cloud deployment |
| **Postman** | API testing |

---

## 📁 Project Structure

```
cloud-api/
├── main.py          # API endpoints
├── models.py        # Database models
├── schemas.py       # Request/Response schemas
├── database.py      # Database connection
├── requirements.txt
└── .env             # Environment variables (not committed)
```

---

## 📡 API Endpoints

### 🌡️ Temperature

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/temperature` | Add temperature record |
| `GET` | `/temperature` | Get all records |
| `GET` | `/temperature/{id}` | Get record by ID |
| `DELETE` | `/temperature/{id}` | Delete record by ID |

**POST /temperature** — Request Body:
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
|---|---|---|
| `POST` | `/sales` | Add sale record |
| `GET` | `/sales` | Get all records |
| `GET` | `/sales/summary` | Get total revenue summary |

**POST /sales** — Request Body:
```json
{
    "product": "iPhone 15",
    "amount": 29900.00,
    "quantity": 2
}
```

**GET /sales/summary** — Response:
```json
{
    "total_orders": 1,
    "total_items": 2,
    "total_revenue": 59800.0
}
```

---

### 📦 Data

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/data` | Add key-value record |
| `GET` | `/data` | Get all records |
| `GET` | `/data/{key}` | Get records by key |

**POST /data** — Request Body:
```json
{
    "key": "humidity",
    "value": "75%"
}
```

---

## ⚙️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/cloud-api.git
cd cloud-api
```

### 2. Create virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file
```env
DATABASE_URL=sqlite:///./mydb.db
```

### 5. Run the server
```bash
uvicorn main:app --reload
```

### 6. Open API docs
```
http://127.0.0.1:8000/docs
```

---

## 🌐 Deploy on Render

1. Push code to GitHub
2. Create **PostgreSQL** database on Render
3. Create **Web Service** on Render
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Add Environment Variable: `DATABASE_URL` → External Database URL
5. Deploy ✅

---

## 📬 Test with Postman

Import this collection or test manually:

```
Base URL: https://cloud-api-t2ch.onrender.com

POST /temperature  →  Add temperature
GET  /temperature  →  Get all temperatures
POST /sales        →  Add sale
GET  /sales/summary → Get revenue summary
POST /data         →  Add data
GET  /data         →  Get all data
```

---

## 📄 License

MIT License