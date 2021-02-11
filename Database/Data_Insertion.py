import sqlite3
import Database_Data

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()

cur.executemany("INSERT INTO Doctors Values(?,?,?,?,?,?,?,?)", Database_Data.Doctors_Data)
cur.executemany("INSERT INTO Patients Values(?,?,?,?,?,?,?,?,?,?)", Database_Data.Patients_Data)
cur.executemany("INSERT INTO Chemists Values(?,?,?,?,?,?,?)", Database_Data.Chemists_Data)
conn.commit()
conn.close()