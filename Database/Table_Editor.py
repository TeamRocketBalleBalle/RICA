import sqlite3

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()
cur.execute("ALTER TABLE Patients ADD COLUMN id BLOB")
cur.execute("ALTER TABLE Patients ADD COLUMN pass BLOB")
cur.execute("ALTER TABLE Doctors ADD COLUMN id BLOB")
cur.execute("ALTER TABLE Doctors ADD COLUMN pass BLOB")
cur.execute("ALTER TABLE Chemists ADD COLUMN id BLOB")
cur.execute("ALTER TABLE Chemists ADD COLUMN pass BLOB")
conn.commit()
conn.close()
