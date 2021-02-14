"""
so first of all, when doctor logs in, and views their appointments, then their username is in the session cookie
so from there we get their UID, and start processing stuff 🔥
"""
import datetime
import json
from colorama import Fore
from flask import current_app
from Database.Database_connection import get_appointments, set_appointments, get_doc_id


def load_and_filter_appointments(email: str) -> dict:
    """
    gets the doctor's appointments [past and upcoming] from the email and returns the filtered appointment list
    :param email: str, email of the doctor
    :return: json of appointments which has been updated/filtered
    """
    # get the doc_id
    doc_id = get_doc_id(email)

    # update the appointments in DB
    update_appointments(doc_id)

    # now load the new appointments from DB
    return get_appointments(doc_id)


# TODO: remove this test argument one the testing is done
def update_appointments(doc_id: int, test=None) -> None:
    """
    updates the appointments of doctors, aka moves appointments from upcoming -> past
    :param doc_id: int, the unique id of the doctor
    :param test: function internal purpose.
    :return: None

    # Pseudocode:
    - gets the appointment JSON.
    - if:
        - if upcoming appointments is empty, or DNE, then leave it as it is and exit
    - otherwise go through each element in the list [preferably from last] and pop those appointments and move 'em
      to `past_appointments` if their date has passed
    - dump that json back to the DB
    """
    appointment_json: dict = dict()
    if not test:
        appointments_json = get_appointments(doc_id)
    else:
        appointments_json = test

    # if the appointments_json is empty, then exit the function.
    # we're done over here 😤
    if "upcoming_appointments" not in appointments_json:
        return None
    # if the upcoming_appointments list is empty [cuz, there's no appointment for them], then also, we're done
    elif not appointments_json["upcoming_appointments"]:
        return None
    # now we know there's some processing to be done * cracks knuckles *
    # start iterating through that list
    upcoming_appointments_copy = []
    past_appointments = []
    length_of_upcoming = len(appointments_json["upcoming_appointments"])
    for index, appointment_data in enumerate(
        appointments_json["upcoming_appointments"]
    ):
        date = appointment_data["time"]

        # check if the time has passed or not and then add the appointment data in either of the list
        # either in upcoming_appointments_copy or in past_appointments

        # if time has passed
        if appointment_passed(date):
            # move it to past_appointments
            past_appointments.append(appointment_data)
        # here, we know that appointment_data is still relevant and upcoming in the future.
        # let it stay in the copy
        else:
            upcoming_appointments_copy.append(appointment_data)

    # now create that updated json file.
    appointments_json["upcoming_appointments"] = upcoming_appointments_copy
    appointments_json["past_appointments"] = (
        appointments_json.setdefault("past_appointments", list()) + past_appointments
    )

    if test:
        return appointments_json

    # log what we've done:
    if not test:
        current_app.logger.info(Fore.LIGHTCYAN_EX +
                                f"Moved {length_of_upcoming - len(appointments_json['updated_appointments'])}"
                                + " to the past")

    # now at last, we push the new json to the database
    set_appointments(doc_id, appointment_json)


def appointment_passed(appointment_date: str) -> bool:
    """
    Takes in appointment's datetime value and checks whether that time has passed or not
    time has passed is determined by checking the appointment time against current computer time
    :param appointment_date: str iso format date
    :return: bool, True if appointment time has passed, False if date is in near future
    """
    return datetime.datetime.fromisoformat(appointment_date) < datetime.datetime.now()


if __name__ == "__main__":
    print("===Testing date time passed====")
    x = str(datetime.datetime.fromisoformat("2021-02-14T01:43:00"))
    print(f"date: {str(x)}\t time passed? {appointment_passed(x)}")
    now = str(datetime.datetime.now())
    print(f"date: {str(now)}\t time passed? {appointment_passed(now)}")
    future = str(datetime.datetime.fromisoformat("2021-02-18T01:43:00"))
    print(f"date: {str(future)}\t time passed? {appointment_passed(future)}")

    # ===================
    test_json = {
        "upcoming_appointments": [
            {
                "doc_id": 1,
                "name_of_patient": "Yash",
                "time": "2021-02-14T02:00:00",
                "contact_number": 1234567891,
                "symptoms": "pls help me 😢",
            }
        ]
    }
    test_json_past = {
        "upcoming_appointments": [
            {
                "doc_id": 1,
                "name_of_patient": "ysh",
                "time": "2021-02-14T02:00:00",
                "contact_number": 1234567891,
                "symptoms": "pls help me 😢",
            },
            {
                "doc_id": 1,
                "name_of_patient": "Tom and Jeery",
                "time": x,
                "contact_number": 1234567891,
                "symptoms": "pls help me 😢",
            },
        ]
    }
    test_json_future = {
        "upcoming_appointments": [
            {
                "doc_id": 1,
                "name_of_patient": "shr80 of the futurea",
                "time": future,
                "contact_number": 1234567891,
                "symptoms": "my rocket powered battle car destroy :(",
            },
            {
                "doc_id": 1,
                "name_of_patient": "Tom and Jeery in the future",
                "time": now,
                "contact_number": 1234567891,
                "symptoms": "pls help me 😢",
            },
        ]
    }
    test_json_empty = {"upcoming_appointments": []}
    test_json_empty2 = {}

    print()
    print("====Testing update json==========")
    print(f"old json:\n{json.dumps(test_json, indent=2)}")
    print(f"updated json:\n{json.dumps(update_appointments(1, test_json), indent=1)}")
    print()
    print("PAST")
    print(f"old json:\n{json.dumps(test_json_past, indent=2)}")
    print(
        f"updated json:\n{json.dumps(update_appointments(1, test_json_past), indent=1)}"
    )
    print()
    print("Future")
    print(f"old json:\n{json.dumps(test_json_future, indent=2)}")
    print(
        f"updated json:\n{json.dumps(update_appointments(1, test_json_future), indent=1)}"
    )
    print()
    print("Empty 1")
    print(f"old json:\n{json.dumps(test_json_empty, indent=2)}")
    print(
        f"updated json:\n{json.dumps(update_appointments(1, test_json_empty), indent=1)}"
    )
    print()
    print("Empty 2")
    print(f"old json:\n{json.dumps(test_json_empty2, indent=2)}")
    print(
        f"updated json:\n{json.dumps(update_appointments(1, test_json_empty2), indent=1)}"
    )
    print()
