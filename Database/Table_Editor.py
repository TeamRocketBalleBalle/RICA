import sqlite3
from farjidoctors import l1

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()
# profile_list = [('Aks@epic.com','Patient')]
cur.executemany("INSERT INTO Doctors VALUES(?,?,?,?,?,?,?)",l1)
conn.commit()
conn.close()
