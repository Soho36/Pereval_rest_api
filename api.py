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


@app.get("/perevals/")
def get_perevals(id: int = None):   # Get one entry for pereval by ID
    conn = get_db_connection()
    cursor = conn.cursor()

    if id:
        # If id is provided, fetch perevals matching the id
        query = "SELECT * FROM pereval_added WHERE id = %s"
        cursor.execute(query, (id,))
    else:
        # If no id is provided, fetch all perevals
        query = "SELECT * FROM pereval_added"
        cursor.execute(query)

    result = cursor.fetchall()  # Fetch results (all or filtered)

    conn.close()

    return {"perevals": result}


@app.post("/perevals/")
def create_pereval(
        name: str,
        title: str,
        other_titles: str,
        connect: str,
        add_time: str,
        status: str
):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO pereval_added (beautyTitle, title, other_titles, connect, add_time, status) 
               VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (name, title, other_titles, connect, add_time, status))
    conn.commit()
    conn.close()
    return {"state": 1, "message": "Pereval added successfully!"}


@app.patch("/perevals/{pereval_id}")
def update_pereval(
        pereval_id: int,
        name: str = None,
        title: str = None,
        other_titles: str = None,
        connect: str = None,
        add_time: str = None,
        status: str = None
):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check current status of the entry
    cursor.execute("SELECT status FROM pereval_added WHERE id = %s", (pereval_id,))
    result = cursor.fetchone()

    if not result:
        return {"state": 0, "error": "Pereval not found"}

    current_status = result[0]

    # Only allow update if status is 'new'
    if current_status != 'new':
        return {"state": 0, "error": "Cannot update entry unless its status is 'new'."}

    # Build the dynamic query based on the provided fields
    query = "UPDATE pereval_added SET "
    updates = []
    values = []

    if name:
        updates.append("beautytitle = %s")
        values.append(name)
    if title:
        updates.append("title = %s")
        values.append(title)
    if other_titles:
        updates.append("other_titles = %s")
        values.append(other_titles)
    if connect:
        updates.append("connect = %s")
        values.append(connect)
    if add_time:
        updates.append("add_time = %s")
        values.append(add_time)
    if status:
        updates.append("status = %s")
        values.append(status)

    # If no fields were provided, return an error
    if not updates:
        return {"state": 0, "error": "No fields provided to update."}

    # Finalize the query and append the pereval_id for the WHERE clause
    query += ", ".join(updates) + " WHERE id = %s"
    values.append(pereval_id)

    try:
        cursor.execute(query, values)
        conn.commit()

        # Check if any row was affected
        if cursor.rowcount == 0:
            return {"state": 0, "error": "Pereval not found or no changes were made."}

        return {"state": 1, "message": "Pereval updated successfully."}

    except Exception as e:
        return {"state": 0, "error": str(e)}

    finally:
        cursor.close()
        conn.close()


