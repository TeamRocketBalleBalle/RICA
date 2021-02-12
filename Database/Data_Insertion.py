import sqlite3
import Database_Maker
import Database_Data
import logging

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()
data = logging.getLogger()
cur.executemany("INSERT INTO Doctors Values(?,?,?,?,?,?,?,?,?)", Database_Data.Doctors_Data)
data.debug("Doctors Table Updated")

cur.executemany("INSERT INTO Patients Values(?,?,?,?,?,?,?,?,?,?)", Database_Data.Patients_Data)
data.debug("Patients Table updated")

cur.executemany("INSERT INTO Chemists Values(?,?,?,?,?,?,?)", Database_Data.Chemists_Data)
data.debug("Chemists table updated")

cur.executemany("INSERT INTO Profiles Values(?,?)", Database_Data.Profiles_Data)
data.debug("Profiles table updated")

conn.commit()
conn.close()
