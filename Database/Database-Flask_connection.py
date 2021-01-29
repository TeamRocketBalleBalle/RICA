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
    #pt = query_db("SELECT Ptype from Profiles WHERE email = '?'", em)

    if p == 'Doctor':
        pass = query_db("SELECT pass from Doctors where email = '?'", em)

    elif p == 'Patient':
        pass = query_db("SELECT pass from Patients where email = '?'", em)

    elif p == 'Chemist':
        pass = query_db("SELECT pass from Chemists where email = '?'", em)
    return pass


if __name__ == "__main__":
    """
/*    .                          .        oooo                                                                         oooo        
  .o8                        .o8        `888                                                                         `888        
.o888oo  .ooooo.   .oooo.o .o888oo       888 .oo.    .ooooo.  oooo d8b  .ooooo.       oooo    ooo  .oooo.    .oooo.o  888 .oo.   
  888   d88' `88b d88(  "8   888         888P"Y88b  d88' `88b `888""8P d88' `88b       `88.  .8'  `P  )88b  d88(  "8  888P"Y88b  
  888   888ooo888 `"Y88b.    888         888   888  888ooo888  888     888ooo888        `88..8'    .oP"888  `"Y88b.   888   888  
  888 . 888    .o o.  )88b   888 .       888   888  888    .o  888     888    .o         `888'    d8(  888  o.  )88b  888   888  
  "888" `Y8bod8P' 8""888P'   "888"      o888o o888o `Y8bod8P' d888b    `Y8bod8P'          .8'     `Y888""8o 8""888P' o888o o888o 
                                                                                      .o..P'                                     
                                                                                      `Y8P'                                      
 """
    print(check_existence("yash@email.com"))  # this should return True/False
