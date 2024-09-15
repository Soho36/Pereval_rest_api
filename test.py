import psycopg2

conn = psycopg2.connect("dbname=pereval user=postgres password=admin")
cur = conn.cursor()
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "preved kotlet!"))

cur.execute("SELECT * FROM test;")
result = cur.fetchone()
print(result)

# conn.commit()
cur.close()
conn.close()


# *****************************************************
def fetch_perevals(self):
    try:
        self.cursor.execute("SELECT * FROM pereval_added")
        results = self.cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []


def close(self):
    self.cursor.close()
    self.connection.close()

