import sqlite3

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()
# profile_list = [('Aks@epic.com','Patient')]
cur.execute("DROP TABLE Doctors")
cur.execute("""CREATE TABLE Doctors(
    name Text , 
    email BLOB,
    phone no INTEGER,
    specialization BLOB,
    loc Text,
    pass BLOB,
    appointment BLOB
)""")
conn.commit()
conn.close()
