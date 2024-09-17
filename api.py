from fastapi import FastAPI
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()   # Load environment variables from .env file

app = FastAPI()


def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432')
    )
    return conn


@app.post("/perevals/")
def create_pereval(name: str, title: str, other_titles: str, connect: str, add_time: str, status: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO pereval_added (beautyTitle, title, other_titles, connect, add_time, status) 
               VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (name, title, other_titles, connect, add_time, status))
    conn.commit()
    conn.close()
    return {"message": "Pereval added successfully!"}


@app.get("/perevals/")
def get_perevals(title: str = None):
    conn = get_db_connection()
    cursor = conn.cursor()

    if title:
        # If title is provided, fetch perevals matching the title
        query = "SELECT * FROM pereval_added WHERE title = %s"
        cursor.execute(query, (title,))
    else:
        # If no title is provided, fetch all perevals
        query = "SELECT * FROM pereval_added"
        cursor.execute(query)

    result = cursor.fetchall()  # Fetch results (all or filtered)

    conn.close()

    return {"perevals": result}

