from Back_End.common_modules import *

# Initialising the Blueprint
bp = Blueprint("doctors", __name__, url_prefix="/doctors")

@bp.route("")
def doctors_page() -> 'html':
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

    return render_template("template.html", page_title=f"{PAGE_TITLE}s", dictionary=f"{dict(session)}",
                           gif_link="https://cdn.discordapp.com/emojis/791837082237665300.gif?v=1",
                           alternateText=alternate_text)
