### สร้าง PostgreSQL บน Render
1. ไปที่ **render.com** → Sign up ฟรี
2. กด **New +** → **PostgreSQL**
3. ตั้งชื่อ เช่น `my-cloud-db`
4. กด **Create Database**
5. Copy **External Database URL** ไว้

### Deploy Web Service
1. กด **New +** → **Web Service**
2. เชื่อม GitHub repo
3. ตั้งค่า:

| ช่อง | ค่า |
|---|---|
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

4. เพิ่ม **Environment Variable**:
   - Key: `DATABASE_URL`
   - Value: วาง External URL ของ PostgreSQL ที่ Copy ไว้

5. กด **Create Web Service** รอ ~2 นาที ✅

---

## ทดสอบ API บน Cloud ด้วย Postman
```
เปลี่ยน URL จาก:
http://127.0.0.1:8000/temperature

เป็น:
https://my-cloud-api.onrender.com/temperature
```

---

## สิ่งที่ใส่ใน Resume ได้เลย
```
✅ FastAPI (Python)        — สร้าง REST API
✅ PostgreSQL              — Relational Database
✅ SQLAlchemy              — ORM
✅ Postman                 — API Testing
✅ Render Cloud            — Cloud Deployment
✅ Git / GitHub            — Version Control
✅ REST API Design         — GET, POST, DELETE