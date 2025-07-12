from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Read DATABASE_URL from environment variable
DATABASE_URL = os.environ.get("DATABASE_URL")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
except Exception as e:
    print("❌ Database connection failed:", e)
    cursor = None

@app.get("/")
def root():
    return {"message": "HR Migration API Live on Render"}

@app.get("/api/employees")
def get_employees():
    if not cursor:
        return {"error": "Database not connected."}
    cursor.execute("SELECT * FROM modern_employees")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    result = [dict(zip(columns, row)) for row in rows]
    return result
