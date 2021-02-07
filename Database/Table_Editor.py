import sqlite3
# from farjidoctors import l1

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()
# profile_list = [('Aks@epic.com','Patient')]
cur.execute("ALTER TABLE Doctors ADD COLUMN UID BLOB")
cur.execute("ALTER TABLE Patients ADD COLUMN Prescription BLOB")

conn.commit()
conn.close()
