import html
import os
import sys
from pathlib import Path

path = Path(os.getcwd())
print(f"path.parnet: {path.parent}")
sys.path.append(path.parent)
print(f"os.getcwd(): {os.getcwd()}")


try:
    from flask import Flask, render_template, request, redirect
except ModuleNotFoundError as e:
    print(e)
    print("Flask module not found. Is flask installed on your computer? \ntry running: \npython -m pip install -r "
          "requirements.txt")
    quit()

app = Flask(__name__)
# this line sets the cache storage time to 0
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route('/')
def landing_page() -> 'html':
    return render_template('index.html')


@app.route('/patients')
def patients_page() -> 'html':
    return render_template("template.html", page_title="Patients",
                           gif_link="https://cdn.discordapp.com/emojis/768874484429226004.gif?v=1")


@app.route('/doctors')
def doctors_page() -> 'html':
    return render_template("template.html", page_title="Doctors",
                           gif_link="https://cdn.discordapp.com/emojis/791837082237665300.gif?v=1")


@app.route('/chemists')
def chemists_page() -> 'html':
    return render_template("template.html", page_title="Chemists",
                           gif_link="https://cdn.discordapp.com/emojis/754250296980668516.gif?v=11")


@app.route('/login', methods=["GET", "POST"])
def login_page() -> 'html':
    """
    if the userid and password are correct, the user is redirected to the resp page [ie, Patient's, Doctor's, Chemist's]
    if they're not, then we redirect to the same sign-in page, with an error message popping up [bootstrap]
    """
    if request.form:
        # --------- Verifying user's entry------------
        os.chdir("../Database")
        from Database import loginVerify
        from Database.Database_connection import get_user_type

        email = request.form['email']
        password = request.form['password']

        if loginVerify.login(email, password):
            return redirect(f"/{loginVerify.get_user_type(email).lower()}s")
        else:
            return render_template("login.html", page_title="Login", login_failed=True)

    else:
        return render_template("login.html", page_title="Login", login_failed=False)


app.run(debug=True)
