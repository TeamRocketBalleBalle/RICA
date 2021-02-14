import functools
from Back_End.common_modules import *
from Database.Database_connection import get_user_type
from flask import request, current_app, redirect, url_for
from random import choice

# Initialising the BluePrint

bp = Blueprint("login", __name__, url_prefix="/login")


@bp.route("", methods=["GET", "POST"])
def login_page() -> 'html':
    """
    UPDATE: User Session Management.
    - If 'username' is not in the session dictionary, then user is not logged in.
        - Then login the user store their email in the session cookie
    - If 'username' is in the sessions dictionary, and we're on login page:
        - Log them out, clear the sessions dictionary

    if the userid and password are correct, the user is redirected to the resp page [ie, Patient's, Doctor's, Chemist's]
    if they're not, then we redirect to the same sign-in page, with an error message popping up [bootstrap]
    """

    # if 'username' is not in session then login and add the email to session
    # also, do this if we have form data
    if request.form and 'username' not in session:
        email = request.form['email']
        password = request.form['password']
        current_app.logger.info(Fore.CYAN + f"{email}: connected")

        # --------- Verifying user's entry------------
        from Database import loginVerify


        # If logged in successfully
        if loginVerify.login(email, password):
            session['username'] = email
            session['type'] = get_user_type(email)
            current_app.logger.info(Fore.GREEN + f"{email}: Logged in SUCCESFULLY")
            return redirect(f"/{loginVerify.get_user_type(email).lower()}s")
        # Login FAILED
        else:
            current_app.logger.debug(Fore.WHITE + f"{email}: Login FAILED")
            return render_template("login_with_jinja.html", page_title="Login", login_failed=True,
                                   useBootstrap=True)

    # else if the 'username' is in session, and hence log out the user.
    elif 'username' in session:
        # -------- Log out user ---------------
        current_app.logger.debug(Fore.CYAN + f"LOGGING OUT: {session['username']}")
        session.clear()
        return render_template("log_out.html")

    else:
        return render_template("login_with_jinja.html", page_title="Login", login_failed=False, useBootstrap=True)


def login_required(page_type=None):
    """
    source reference
    I would like to thank: https://stackoverflow.com/questions/5929107/decorators-with-parameters
    :param page_type:
    :return:
    """

    def decorator(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if "username" not in session:
                return redirect(url_for("login.login_page"))
            elif page_type and get_user_type(session["username"]) != page_type:
                # TODO: replace this not authorised with maybe a template
                # return "Not authorised to view"
                return render_template(
                    "template.html",
                    page_title=f"{page_type}s",
                    gif_link=choice(
                        [
                            "https://cdn.discordapp.com/emojis/791837082237665300.gif?v=1",
                            "https://cdn.discordapp.com/emojis/754250296980668516.gif?v=11",
                            "https://media.discordapp.net/attachments/787448623351726080/808661838455504896/rick.gif"
                        ]
                    ),
                    alternateText="You are not authorised to view this page."
                                  f"\nPlease view <b>{get_user_type(session['username'])}</b>",
                )
            return view(**kwargs)

        return wrapped_view

    return decorator