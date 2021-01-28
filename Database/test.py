import sqlite3

conn = sqlite3.connect('rica.db')

cur = conn.cursor()

cur.execute("SELECT * FROM Patients")
print(cur.fetchall())
conn.commit()
conn.close()
