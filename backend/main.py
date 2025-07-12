from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global connection variable
conn = None

# Connect to DB when the app starts
@app.on_event("startup")
def startup_event():
    global conn
    try:
        DATABASE_URL = os.environ.get("DATABASE_URL")
        conn = psycopg2.connect(DATABASE_URL)
        print("✅ Database connected successfully!")
    except Exception as e:
        print("❌ Database connection failed:", e)

@app.get("/")
def root():
    return {"message": "🚀 HR Migration API is Live on Render!"}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.get("/api/employees")
def get_employees():
    if not conn:
        return {"error": "❌ Database not connected."}
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modern_employees")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()
        return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        return {"error": str(e)}
