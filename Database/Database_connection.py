import os
import sqlite3


def connect_and_close(func):
    """
    wrapper function to start and close the connection to database whenever the other functions are called.
    :param func: function
    :return: function output
    """

    def wrap(*args, **kwargs):
        # print("Before:", os.getcwd())
        os.chdir("../Database")
        # print("After:", os.getcwd())
        # connect to the database
        conn = sqlite3.connect('Rica_AlphaV0.1.db')
        cur = conn.cursor()
        args += (cur,)  # give the cursor argument to the func
        # call the function
        result = func(*args, **kwargs)

        # close the connection to database
        conn.close()
        os.chdir("../Back_End")
        return result

    return wrap


@connect_and_close
def check_existence(em: str, cur):
    """
    checks whether the argument `em` [email] exists in the database or not.
    returns boolean for that
    :param em: email
    :param cur: the sqlite cursor object
    :return: bool
    """
    # os.chdir("../Database")
    # print(f"databse_connection ke andar: {os.getcwd()}")
    # breakpoint()
    cur.execute(f'SELECT * FROM Profiles WHERE email = \"{em}\"')
    return bool(cur.fetchall())


@connect_and_close
def get_user_type(em: str, cur) -> str:
    """
    Get's the user type from database using email as key
    :param em: emaail
    :param cur: Sqlite cursor object
    :return: str, any one from  "Patient", "Doctor", "Chemist"
    """
    cur.execute(f"SELECT Utype FROM Profiles WHERE email = \"{em}\"")
    return cur.fetchall()[0][0]


@connect_and_close
def get_password(em: str, cur):
    """
    returns the **PLAIN TEXT** password for a given email
    :param em: email
    :param cur: the sqlite cursor object
    :return: str
    """
    typ = get_user_type(em)
    cur.execute(f"SELECT password from {typ}s WHERE email = \"{em}\"")
    return str(cur.fetchall()[0][0])


@connect_and_close
def get_all_docs(cur) -> tuple:
    """
    returns a tuple of doctors from the database
    :param cur: the sqlite cursor object
    :return: tuple
    """
    return cur.execute("""SELECT name, specialization, loc, password FROM Doctors""").fetchall()


@connect_and_close
def get_doc_names(spec: str, cur) -> tuple:
    """
    Given a category [specialisation] of doctors fetch all the matching docs from the database
    :param spec: specialisation
    :param cur: the sqlite cursor object
    :return: tuple
    """
    return cur.execute(f"SELECT name from Doctors where specialization == '{spec}'").fetchall()


if __name__ == "__main__":
    print(check_existence("ysh@123.com"))
    print(get_user_type("ysh@123.com"))
    print((get_doc_names("Cardiologist")))
    print(get_password("ysh@123.com"))