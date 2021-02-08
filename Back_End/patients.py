from Back_End.common_modules import *
from flask import request

# initialising the blueprint
bp = Blueprint("patients", __name__, url_prefix="/patients", static_folder='static')


@bp.route("")
def patients_page() -> 'html':
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

    return render_template("template.html", page_title=f"{PAGE_TITLE}s", dictionary=f"{dict(session)}",
                           gif_link="https://cdn.discordapp.com/emojis/768874484429226004.gif?v=1",
                           alternateText=alternate_text)


@bp.route("/retrieve")
def retrieve_docs() -> html:
    from Database.Database_connection import get_all_docs
    return render_template("retrieve_docOcs.html", page_title="Testing", dictionary=f"{dict(session)}",
                           gif_link="https://cdn.discordapp.com/emojis/768874484429226004.gif?v=1",
                           doc_ocs=get_all_docs()
                           )


@bp.route("/appointment", methods=["GET", "POST"])
def appointments() -> html:
    if request:
        current_app.logger.debug(request.form["docs"])
    return render_template("doctor.html", page_title="SHR08OPXD page")
