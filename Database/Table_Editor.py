import sqlite3

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()
profile_list = [('Aks@epic.com','Patient')]
cur.execute("DELETE FROM Profiles WHERE rowid = 7")
conn.commit()
conn.close()
