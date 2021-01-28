import sqlite3

conn = sqlite3.connect('rica.db')

cur = conn.cursor()

cur.execute("ALTER TABLE Doctors ADD COLUMN specialization Text")

conn.commit()
conn.close()

