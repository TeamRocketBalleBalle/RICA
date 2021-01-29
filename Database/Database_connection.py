import sqlite3

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()


def check_existence(em):
    cur.execute(f'SELECT * FROM Profiles WHERE email = \"{em}\"')

    return bool(cur.fetchall())


def get_user_type(em):
    cur.execute(f"SELECT Ptype FROM Profiles WHERE email = \"{em}\"")
    return cur.fetchall()[0][0]

def get_password(em):
    typ = get_user_type(em)
    cur.execute(f"SELECT pass from {typ}s WHERE email = \"{em}\"")
    return cur.fetchall()[0][0]

