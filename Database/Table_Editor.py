import sqlite3

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()
profile_list = [('ramgopal@123.com','Chemist'),('gabbarakshay!321.com','Chemist'),('jayant@456.com','Chemist'),('ysh@123.com','Patient'),('Shr@epic.com','Patient'),('Aks@epic.com','Patients')]
cur.executemany("INSERT INTO Profiles VALUES(?,?)",profile_list)
conn.commit()
conn.close()
