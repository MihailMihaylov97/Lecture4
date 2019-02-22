from sqlite3 import connect

conn=connect("test.db")
cur=conn.cursor()
cur.execute(
    "CREATE TABLE test (id serial PRIMARY KEY, username text, password text)")
user = (1, "jose", "pass123")
insert_query="INSERT INTO test VALUES (?,?,?)"
cur.execute(insert_query,user)
conn.commit()
conn.close()








# conn = connect('test.db')
# cur = conn.cursor()
# cur.execute(
#     "CREATE TABLE test (id serial PRIMARY KEY, username text, password text)")

# user = (1, 'jose', 'pass123')
# insert_query = "INSERT INTO test VALUES (?, ?, ?)"
# cur.execute(insert_query, user)

# conn.commit()
# conn.close()