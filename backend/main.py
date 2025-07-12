from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = psycopg2.connect(
    dbname="hr_migration",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

@app.get("/api/employees")
def get_employees():
    cursor.execute("SELECT * FROM modern_employees")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    result = [dict(zip(columns, row)) for row in rows]
    return result
