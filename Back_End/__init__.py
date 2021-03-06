import sys
import os
from pathlib import Path
current_path = Path(os.getcwd())
sys.path.append(str(current_path.parent))

from colorama import Fore, init
import logging

try:
    from flask import Flask, render_template, request, redirect, session
except ModuleNotFoundError as e:
    print(e)
    print("Flask module not found. Is flask installed on your computer? \ntry running: \npython -m pip install -r "
          "requirements.txt")
    quit()

# ================================================================
# initialise Colorama
init(autoreset=True)


# Creating the logger filter class
class IPFilter(logging.Filter):
    def filter(self, record):
        try:
            email = session['username']
        except KeyError as e:
            print(Fore.RED + "this happened:", e)
            email = ""

        record.ip_address = Fore.LIGHTBLUE_EX + request.remote_addr if request else "" + f"[{email}]"
        return True


# ==============================================================

def create_app():
    """
    creates the flask app object.
    """

    # create and configure the app
    app = Flask(__name__)

    # ===================================================
    # ----------------- Configuring Flask ---------------
    # this line sets the cache storage time to 0
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    # This line uses this secret key to sign the client-side cookies. set do 'dev' for testing only
    # TODO: when project is done, set this secret key to random bytes, everytime.
    app.config["SECRET_KEY"] = 'dev' # os.urandom(16)
    # ===================================================

    # Configure logging for app.logger
    app.logger.handlers[0].setFormatter(
        logging.Formatter("%(ip_address)s - - [%(asctime)s] %(levelname)-6s [%(module)s.py -> %(funcName)s()]: "
                          "\"%(message)s\"",
                          datefmt="%d/%b/%Y %H:%M:%S"))
    app.logger.setLevel(20)  # set logger to debug
    app.logger.addFilter(IPFilter())

    # Registering the blueprints
    # Landing page
    try:
        from Back_End import landing_page, patients, doctors, chemists, login
    except ModuleNotFoundError as error:
        print("ModuleNotFoundError:", error)
        print("Are you sure you are running this file from `RICA` or `RICA/Back_End` directory?")
        print("Try running with `python -m __init__` or `python -m app` in Back_End.")
        print("Or if you are running from parent directory, try `python -m Back_End.app` or `python -m "
              "Back_End.__init__`")
        quit()
    else:
        app.register_blueprint(landing_page.bp)
        app.register_blueprint(patients.bp)
        app.register_blueprint(doctors.bp)
        app.register_blueprint(chemists.bp)
        app.register_blueprint(login.bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
