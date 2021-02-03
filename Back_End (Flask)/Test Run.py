import html
import os
import logging
from colorama import Fore, init

# import sys
# from pathlib import Path

# path = Path(os.getcwd())
# print(f"path.parent: {path.parent}")
# sys.path.append(path.parent)
# print(f"os.getcwd(): {os.getcwd()}")

# Initialising colorama
init(autoreset=True)

# ========================================================================================================
# Creating a filter for Logginf IP
# src: https://stackoverflow.com/questions/17558552/how-do-i-add-custom-field-to-python-log-format-string


class IPFilter(logging.Filter):
    def filter(self, record):
        record.ip_address = Fore.LIGHTWHITE_EX + request.remote_addr if request else ""
        return True


# =======================================================================================================
# =======================================================================================================
"""
 .oooooo..o               .       .    o8o                              oooooooooooo oooo                     oooo        
d8P'    `Y8             .o8     .o8    `"'                              `888'     `8 `888                     `888        
Y88bo.       .ooooo.  .o888oo .o888oo oooo  ooo. .oo.    .oooooooo       888          888   .oooo.    .oooo.o  888  oooo  
 `"Y8888o.  d88' `88b   888     888   `888  `888P"Y88b  888' `88b        888oooo8     888  `P  )88b  d88(  "8  888 .8P'   
     `"Y88b 888ooo888   888     888    888   888   888  888   888        888    "     888   .oP"888  `"Y88b.   888888.    
oo     .d8P 888    .o   888 .   888 .  888   888   888  `88bod8P'        888          888  d8(  888  o.  )88b  888 `88b.  
8""88888P'  `Y8bod8P'   "888"   "888" o888o o888o o888o `8oooooo.       o888o        o888o `Y888""8o 8""888P' o888o o888o 
                                                        d"     YD                                                         
                                                        "Y88888P'                                                         
"""
# ----- Setting up Flask ----------------------------


try:
    from flask import Flask, render_template, request, redirect, session
except ModuleNotFoundError as e:
    print(e)
    print("Flask module not found. Is flask installed on your computer? \ntry running: \npython -m pip install -r "
          "requirements.txt")
    quit()

app = Flask(__name__)
# this line sets the cache storage time to 0
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
# This line uses this secret key to sign the client-side cookies. set do 'dev' for testing only
# TODO: when project is done, set this secret key to random bytes, everytime.
app.config["SECRET_KEY"] = 'dev'
# breakpoint()
# Configure logging for app.logger
app.logger.handlers[0].setFormatter(
    logging.Formatter("%(ip_address)s - - [%(asctime)s] %(levelname)s: \"%(message)s\"", datefmt="%d/%b/%Y %H:%M:%S"))
app.logger.setLevel(10)
app.logger.addFilter(IPFilter())

# -------------------------------------------------
# =====================================================================================================================
"""
ooo        ooooo            o8o                     .oooooo.                   .o8            
`88.       .888'            `"'                    d8P'  `Y8b                 "888            
 888b     d'888   .oooo.   oooo  ooo. .oo.        888           .ooooo.   .oooo888   .ooooo.  
 8 Y88. .P  888  `P  )88b  `888  `888P"Y88b       888          d88' `88b d88' `888  d88' `88b 
 8  `888'   888   .oP"888   888   888   888       888          888   888 888   888  888ooo888 
 8    Y     888  d8(  888   888   888   888       `88b    ooo  888   888 888   888  888    .o 
o8o        o888o `Y888""8o o888o o888o o888o       `Y8bood8P'  `Y8bod8P' `Y8bod88P" `Y8bod8P'                                                                                     
"""

# ------------- Giving routes --------------------


@app.route('/')
def landing_page() -> 'html':
    session['ip'] = request.remote_addr
    return render_template('index.html')


@app.route('/patients')
def patients_page() -> 'html':
    return render_template("template.html", page_title=f"Patients {dict(session)}",
                           gif_link="https://cdn.discordapp.com/emojis/768874484429226004.gif?v=1")


@app.route('/doctors')
def doctors_page() -> 'html':
    return render_template("template.html", page_title="Doctors",
                           gif_link="https://cdn.discordapp.com/emojis/791837082237665300.gif?v=1")


@app.route('/chemists')
def chemists_page() -> 'html':
    return render_template("template.html", page_title=f"Chemists {dict(session)}",
                           gif_link="https://cdn.discordapp.com/emojis/754250296980668516.gif?v=11")


@app.route('/login', methods=["GET", "POST"])
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
        app.logger.info(Fore.CYAN + f"{email}: connected")

        # --------- Verifying user's entry------------
        os.chdir("../Database")
        from Database import loginVerify
        from Database.Database_connection import get_user_type

        # If logged in successfully
        if loginVerify.login(email, password):
            session['username'] = email
            app.logger.info(Fore.GREEN + f"{email}: Logged in SUCCESFULLY")
            return redirect(f"/{loginVerify.get_user_type(email).lower()}s")
        # Login FAILED
        else:
            app.logger.debug(Fore.WHITE + f"{email}: Login FAILED")
            return render_template("login_with_jinja.html", page_title="Login", login_failed=True,
                                   useBootstrap=True)

    # else if the 'username' is in session, and hence log out the user.
    elif 'username' in session:
        # -------- Log out user ---------------
        app.logger.debug(Fore.CYAN + f"LOGGING OUT: {session['username']}")
        session.clear()
        # TODO: replace LOGGED OUT with the html file which shows the message logged out
        # Maybe use the bootstrap thingy on login page but instead change the color and text
        return "LOGGED OUT"

    else:
        return render_template("login_with_jinja.html", page_title="Login", login_failed=False, useBootstrap=True)


@app.route("/jinja")
def jinja_test() -> "html":
    return render_template("login_with_jinja.html", page_title="Testing Jinja", useBootstrap=True)


app.run(debug=True)
