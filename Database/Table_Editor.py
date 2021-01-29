import sqlite3

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()
patients_entry = [(1,'Ysh','ysh@123.com',1234567891,'nothing','Delhi','22/06/2003','Faltu','yash123','123456578')]
cur.executemany("INSERT INTO Patients VALUES (?,?,?,?,?,?,?,?,?,?)",patients_entry)
conn.commit()
conn.close()
chemvalues=[("Ram Gopal","ramgopal@123.com",9876543210,5,"Borawali East",1,"id.user",2021)]
cur.executemany("INSERT CHEMIST VALUES (?,?,?,?,?,?,?,?)",chemvalues)
conn.commit()
conn.close()