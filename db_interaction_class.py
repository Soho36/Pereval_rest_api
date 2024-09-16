import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()   # Load environment variables from .env file


class PerevalDatabase:

    def __init__(self):
        db_name = os.getenv('DB_NAME')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST', 'localhost')  # Default to localhost
        port = os.getenv('DB_PORT', '5432')  # Default to 5432

        try:
            # Establish database connection
            self.connection = psycopg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.cursor = self.connection.cursor()
            print("Database connection successful")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    # Method for inserting into the pereval_added table
    def insert_pereval(self, name, title, other_titles, connect, add_time, status):
        try:
            query = """INSERT INTO pereval_added (beautytitle, title, other_titles, connect, add_time, status) 
                       VALUES (%s, %s, %s, %s, %s, %s)"""
            self.cursor.execute(query, (name, title, other_titles, connect, add_time, status))
            self.connection.commit()
            print("Record inserted successfully")
        except Exception as e:
            print(f"Error inserting data: {e}")

    def fetch_perevals(self):
        try:
            self.cursor.execute("SELECT * FROM pereval_added")
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

    def close(self):    # Close the database connection
        try:
            self.cursor.close()
            self.connection.close()
            print("Database connection closed")
        except Exception as e:
            print(f"Error closing database connection: {e}")


db = PerevalDatabase(db_name="pereval", user="postgres", password="admin")
db.insert_pereval("пер. ", "Смоленского", "Четырев", "", "2024-09-16 23:25:13", 'new')
perevals = db.fetch_perevals()
print(perevals)
db.close()
