import sqlite3

conn = sqlite3.connect('rica.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE CHEMIST (
        name Text,
        location Text,
        rating INTEGER

)
""")
conn.commit()
conn.close()
