import sqlite3, sys, os

conn = sqlite3.connect('Rica_AlphaV0.1.db')
cur = conn.cursor()

def check_existence(em):
    # os.chdir("../Database")
    print(f"databse_connection ke andar: {os.getcwd()}")
    # breakpoint()
    cur.execute(f'SELECT * FROM Profiles WHERE email = \"{em}\"')
    return bool(cur.fetchall())


def get_user_type(em):
    cur.execute(f"SELECT Ptype FROM Profiles WHERE email = \"{em}\"")
    return cur.fetchall()[0][0]


def get_password(em):
    typ = get_user_type(em)
    cur.execute(f"SELECT pass from {typ}s WHERE email = \"{em}\"")
    return cur.fetchall()[0][0]

print(check_existence("ysh@123.com"))