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

