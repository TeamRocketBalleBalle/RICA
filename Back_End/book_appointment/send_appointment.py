"""
how i think this could work:
get existing json from database.
append new json to the upcoming appointments list
*optional: move the old appointments to past_appointments list
"""

import datetime
import json
import os
from colorama import Fore
from Database.Database_connection import (
    get_appointments,
    get_name_patient,
    get_phone_patient,
)
from flask import current_app, session


# TODO: when doctor request their upcoming appointments then server should move past appointmnets to another list
def add_apppointment(
        doc_id: int, name_of_patient: str, date_time, contact_number: int, symptoms: str
):
    """
    This function appends the new appointment's data into a JSON.
    :param doc_id: the unique id of a particular doctor
    :param name_of_patient: The name of the patient who requested the consultation
    :param date_time: the date/time selected by the patient for the consultation
    :param contact_number: the phone number of the patient
    :param symptoms: the symptoms listed by the patient for the doctor to "prepare in advance" or something
    """
    # sanitise datetime here.
    # TODO: what to do when date/time entered is of wrong form??
    try:
        date_time = datetime.datetime.fromisoformat(date_time)
    except ValueError:
        current_app.logger.critical(
            Fore.BLUE
            + "!!!!"
            + Fore.RED
            + f"Invalid date received from {Fore.GREEN + session['username']} : {date_time}"
        )
        date_time = datetime.datetime.now()
    # breakpoint()
    old_appointment_list_json = json.loads(get_appointments(doc_id))
    data_to_append = {
        "doc_id": doc_id,
        "name_of_patient": name_of_patient,
        "time": date_time.isoformat(),
        "contact_number": contact_number,
        "symptoms": symptoms,
    }

    old_appointment_list_json.setdefault("upcoming_appointments", list()).append(data_to_append)
    return old_appointment_list_json


if __name__ == "__main__":
    os.chdir("../")
    doc_id: int = 1
    name_of_patient: str = "Dela Cruz"
    date_time = "today [TODO]"
    contact_number: int = "9999999"
    symptoms: str = "#AprilFoold 101"

    TEST_JSON = {
        "upcoming_appointments": [
            {
                "doc_id": 1,
                "name_of_patient": "Tom from Jerry",
                "time": "today [TODO]",
                "contact_number": "9999999",
                "symptoms": "#AprilFoold 101",
            }
        ]
    }

    # print(
    #     f"""old json: {json.dumps(append_appointment.TEST_JSON, indent=2)}
    # New JSON: {append_appointment(doc_id, name_of_patient, date_time, contact_number, symptoms)}
    # """
    # )
    
    # ImmutableMultiDict([('doc_id', '1'), ('datetime', '2021-02-14T02:00'), ('symptoms', 'pls help me 😢')])
    test = {"doc_id": 1, "datetime": "2021-02-14T02:00", "symptoms": "pls help me 😢"}
    result = add_apppointment(
        test["doc_id"],
        get_name_patient(session['username']),
        test["datetime"],
        get_phone_patient(session['username'], ),
        test["symptoms"],
    )
    print(f"New json yippee: {result}")
    # os.chdir("/book_appointment")
