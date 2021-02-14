import datetime
from .book_appointment.send_appointment import add_appointment
from flask import request, redirect

from Back_End.common_modules import *
from Database.Database_connection import get_phone_patient, get_name_patient

# initialising the blueprint
bp = Blueprint("patients", __name__, url_prefix="/patients", static_folder='static')


@bp.route("")
@login_required(page_type="Patient")
def patients_page() -> 'html':
    """
    This function handles the requests for Landing page for the patients category.
    This function also performs `is_logged_in?` verification check too before letting them access member-only content

    ||[low key sounds like handling youtube membership😆]||
    :return: html
    """
    PAGE_TITLE = "Patient"
    # If user is not logged in
    current_app.logger.debug(f"Before calling function: {os.getcwd()}")
    if "username" not in session:
        alternate_text = "You need to login to view this page"
    # if above is false, then user is logged in
    # So check if their account type is different than this page's requirement
    elif get_user_type(session['username']) != PAGE_TITLE:
        alternate_text = "You are not authorised to view this page"
    # if we reach here, then the user is a patient indeed
    else:
        alternate_text = None

    current_app.logger.info(
        Fore.YELLOW +
        f"{'{} [{}]'.format(session['username'], session['type']) if 'username' in session else 'Anonymous'}: "
        f"tried to access {PAGE_TITLE}s page "
    )

    return render_template(
        "patients_landing_page.html",
        useBootstrap=True,
        page_title=f"{PAGE_TITLE}s",
        dictionary=f"{dict(session)}",
        gif_link="https://cdn.discordapp.com/emojis/768874484429226004.gif?v=1",
        alternateText=alternate_text,
    )


@bp.route("/retrieve")
def retrieve_docs(doc_ocs=None) -> "html":
    """
    Test function to check whether for-looping works to display the docs
    :param doc_ocs: the list containing doctors
    :return: 'html'
    """
    return render_template("retrieve_docOcs.html", page_title="Testing", dictionary=f"{dict(session)}",
                           gif_link="https://cdn.discordapp.com/emojis/768874484429226004.gif?v=1",
                           doc_ocs=doc_ocs
                           )


@bp.route("/appointment", methods=["GET", "POST"])
def appointments() -> "html":
    """
    The handler function to display the page to book appointments
    :return: html
    """
    if request.form:
        # store that request in cookie for future reference.
        session["last_docs_requested"] = request.form["docs"]
        # also get the doc
        doc = get_doc_names(request.form["docs"])
        # doc = [(doc_id, name) for doc_id, name in enumerate(doc)]
        current_app.logger.debug(Fore.WHITE + f"CATEGORY RECEIVED:- {request.form['docs']}")
        current_app.logger.debug(Fore.WHITE + f"DB respond sent:- {doc}")
        return render_template(
            "appointment_booking.html",
            page_title="Book Your Doctor",
            dictionary=f"{dict(session)}",
            gif_link="https://cdn.discordapp.com/emojis/768874484429226004.gif?v=1",
            docs=doc,
            useBootstrap=True,
        )
    else:
        docs = []
    return render_template("doctor.html", page_title="SHR08OPXD page", doc_ocs=docs, useBootstrap=True)


@bp.route("/book", methods=["GET", "POST"])
def book_appointment() -> html:
    if request.form:
        current_app.logger.debug(Fore.BLUE + f"Request received: {request.form}")

        any_exceptions = False
        # extracting the data from the form.
        try:
            doc_id = int(request.form["doc_id"])
        except ValueError:
            current_app.logger.critical(
                Fore.RED + f"Unable to parse: doc_id {request.form['doc_id']}"
            )
            any_exceptions = True

        try:
            date_time = datetime.datetime.fromisoformat(request.form["datetime"])
        except ValueError:
            current_app.logger.critical(
                Fore.RED + f"Unable to parse: datetime {request.form['datetime']}"
            )
            any_exceptions = True

        if any_exceptions:
            return render_template(
                "appointment_booking.html",
                page_title="Book Your Doctor",
                error=True,
                useBootstrap=True,
                docs=get_doc_names(session["last_docs_requested"]),
            )

        symptoms = request.form["symptoms"].strip(" ")
        name_of_patient = get_name_patient(session["username"])
        contact_number = get_phone_patient(session["username"])

        # call that function
        add_appointment(doc_id, name_of_patient, date_time, contact_number, symptoms)

        return render_template("patients/response_submission.html")
    return redirect("/patients")
