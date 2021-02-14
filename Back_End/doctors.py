from Back_End.common_modules import *
from Database.Database_connection import get_name_doc

# Initialising the Blueprint
bp = Blueprint("doctors", __name__, url_prefix="/doctors", static_folder='static')


@bp.route("")
@login_required("Doctor")
def doctors_page() -> 'html':
    """
    This function handles the requests for Landing page for the doctors category.
    This function also performs `is_logged_in?` verification check too before letting them access member-only content
    :return: html
    """
    PAGE_TITLE = "Doctor"
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
    # TODO: show an alert at the top of the page if there's an upcoming appointment in the next 1-2 hour
    return render_template("doctor_landing_page.html", page_title=f"{PAGE_TITLE}s",
                           useBootstrap=True,
                           doc_name = get_name_doc(session['username']),
                           alternateText=alternate_text)
