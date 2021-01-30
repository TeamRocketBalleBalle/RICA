import os
import sqlite3


def connect_and_close(func):
    """
    wrapper function to start and close the connection to database whenever the other functions are called.
    :param func: function
    :return: function output
    """

    def wrap(*args, **kwargs):
        # connect to the database
        conn = sqlite3.connect('Rica_AlphaV0.1.db')
        cur = conn.cursor()
        args += (cur,)  # give the cursor argument to the func
        # call the function
        result = func(*args, **kwargs)

        # close the connection to database
        conn.close()
        return result

    return wrap


@connect_and_close
def check_existence(em, cur):
    # os.chdir("../Database")
    print(f"databse_connection ke andar: {os.getcwd()}")
    # breakpoint()
    cur.execute(f'SELECT * FROM Profiles WHERE email = \"{em}\"')
    return bool(cur.fetchall())


@connect_and_close
def get_user_type(em, cur):
    cur.execute(f"SELECT Ptype FROM Profiles WHERE email = \"{em}\"")
    return cur.fetchall()[0][0]


@connect_and_close
def get_password(em, cur):
    typ = get_user_type(em)
    cur.execute(f"SELECT pass from {typ}s WHERE email = \"{em}\"")
    return cur.fetchall()[0][0]


if __name__ == "__main__":
    print(check_existence("ysh@123.com"))
