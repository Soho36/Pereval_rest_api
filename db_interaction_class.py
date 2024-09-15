import psycopg2

conn = psycopg2.connect("dbname=pereval user=postgres password=admin")
cur = conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
conn.commit()
cur.close()
conn.close()

