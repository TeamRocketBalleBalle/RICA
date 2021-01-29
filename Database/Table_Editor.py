import sqlite3

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()
patient_entry = [(2,'SHR08OPXD','Shr@epic.com',3454389841,'Hyper Tension','Omicron','08/04/2004','Faltu','Shr88','testcase1'),(3,'MofoAkshat','Aks@epic.com',6584271395,'Covid Survivor','Delta Noida','04/08/2001','Faltu','MofoAks','testcase2')]
cur.executemany("INSERT INTO Patients VALUES(?,?,?,?,?,?,?,?,?,?)",patient_entry)
conn.commit()
conn.close()