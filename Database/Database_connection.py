import json
import os
import sqlite3
from colorama import Fore
from flask import current_app


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


def connect_commit_close(func):
    """
    wrapper function to start, commit and close the connection to database whenever the other functions are called.
    :param func: function
    :return: function output
    """

    def wrap(*args, **kwargs):
        # print("Before:", os.getcwd())
        os.chdir("../Database")
        # print("After:", os.getcwd())
        # connect to the database
        conn = sqlite3.connect("Rica_AlphaV0.1.db")
        cur = conn.cursor()
        args += (cur,)  # give the cursor argument to the func
        # call the function
        result = func(*args, **kwargs)

        # commit the changes to the database
        conn.commit()
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


# @connect_and_close
# def get_all_docs(cur) -> tuple:
#     """
#     returns a tuple of doctors from the database
#     :param cur: the sqlite cursor object
#     :return: tuple
#     """
#     return cur.execute("""SELECT name, specialization, loc, password FROM Doctors""").fetchall()


@connect_and_close
def get_doc_names(spec: str, cur) -> tuple:
    """
    Given a category [specialisation] of doctors fetch all the matching docs from the database
    :param spec: specialisation
    :param cur: the sqlite cursor object
    :return: tuple
    """
    return cur.execute(f"SELECT name , UID, Year from Doctors where specialization == '{spec}'").fetchall()


@connect_and_close
def get_appointments(doc_id: int, cur) -> json:
    """
    returns the json of appointments of a doctor of given doc_id
    :param doc_id: int, unique id of the doctor in the database
    :param cur: sqlite cursor object
    :return: json
    """
    return cur.execute(
        f"SELECT appointment FROM Doctors where UID = {doc_id};"
    ).fetchone()[0]


@connect_and_close
def get_name_patient(email: str, cur) -> str:
    """
    returns the name of the patient of given email
    :param email: str, email of the patient
    :param cur: sqlite cursor object
    :return: str
    """
    return cur.execute(f"SELECT name from Patients where email = ?;", (email, )).fetchone()[0]

@connect_and_close
def get_name_doc(doc_id: int, cur) -> str:
    """
    returns the name of the doctor of given doc_id
    :param doc_id: int, doc_id of the patient
    :param cur: sqlite cursor object
    :return: str
    """
    return cur.execute(f"SELECT name from Doctors where UID = ?;", (doc_id,)).fetchone()[0]

@connect_and_close
def get_phone_patient(email: str, cur) -> int:
    """
    returns the phone number of the patient of given email
    :param email: str, email of the patient
    :param cur: sqlite cursor object
    :return: int, phone number
    """
    return cur.execute(f"SELECT Contact_No from Patients where email = ?;", (email, )).fetchone()[0]


@connect_commit_close
def set_appointments(doc_id: int, appointment_json: json, cur) -> None:
    """
    updates the appointment list of doctors in the database based on the new json provided
    :param doc_id: int, unique id of the doctor in the database
    :param appointment_json: json
    :param cur: sqlite cursor object
    :return: None
    """
    appointment_json = json.dumps(appointment_json)
    cur.execute("UPDATE Doctors SET appointment = ? WHERE UID = ?;", (appointment_json, doc_id))
    try:
        current_app.logger.debug(Fore.WHITE + "Successfully updated the appointments in the database")
    except RuntimeError:
        pass


if __name__ == "__main__":
    print(check_existence("ysh@123.com"))
    print(get_user_type("ysh@123.com"))
    print((get_doc_names("Cardiologist")))
    print(get_password("ysh@123.com"))

    print("========Testing JSON========")
    print(get_appointments(2))
    print("setting appointments")
    test_json = {'upcoming_appointments': [{'doc_id': 1, 'name_of_patient': 'Yash', 'time': '2021-02-14T02:00:00', 'contact_number': 1234567891, 'symptoms': 'pls help me 😢'}]}
    set_appointments(2, test_json)
    print("after setting appointments:")
    print(get_appointments(2))
