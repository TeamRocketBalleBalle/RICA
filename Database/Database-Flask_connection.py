import sqlite3
from flask import g

DATABASE = "Database/Rica_AlphaV0.1.db"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def check_existence(em):
    ans = query_db("""SELECT email WHEN EXISTS (SELECT TOP 1 *
                             FROM dbo.Profiles 
                             WHERE email = '?') 
                THEN CAST (1 AS BIT) 
                ELSE CAST (0 AS BIT) END""", em, one=True)
    if ans == 0:
        return True
    else:
        return False


def get_user_type(em):
    pt = query_db("SELECT Ptype from Profiles WHERE email = '?'", em, one=True)
    return pt

def get_password(em):
    p = get_user_type(em)
    pt = query_db("SELECT Ptype from Profiles WHERE email = '?'", em)

    if p == 'Doctor':
        pass = query_db("SELECT pass from Doctors where email = '?'", em)

    elif p == 'Patient':
        pass = query_db("SELECT pass from Patients where email = '?'", em)

    elif p == 'Chemist':
        pass = query_db("SELECT pass from Chemists where email = '?'", em)
    return pass