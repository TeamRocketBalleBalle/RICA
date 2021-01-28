import sqlite3

conn = sqlite3.connect('rica.db')

cur = conn.cursor()

cur.execute(""" CREATE TABLE Patients(
    name Text,
    age Integer,
    email Text

) """)
conn.commit()
conn.close()
