import sqlite3

conn = sqlite3.connect('rica.db')

cur = conn.cursor()

cur.execute("ALTER TABLE Patients ADD COLUMN loc Text")
conn.commit()
conn.close()
