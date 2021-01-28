import html

try:
    from flask import Flask, render_template
except ModuleNotFoundError as e:
    print(e)
    print("Flask module not found. Is flask installed on your computer? \ntry running: \npython -m pip install -r requirements.txt")
    quit()

app = Flask(__name__)
# this line sets the cache storage time to 0
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route('/')
def landing_page() -> 'html':
    return render_template('index.html')


@app.route('/patients')
def patients_page() -> 'html':
    # return "<h1>Patient's page</h1> <iframe style=\"border: none; \" src=\"https://cdn.discordapp.com/emojis/768874484429226004.gif?v=1\"></iframe>"
    return render_template("template.html", page_title="Patients", gif_link="https://cdn.discordapp.com/emojis/768874484429226004.gif?v=1")


@app.route('/doctors')
def doctors_page() -> 'html':
    # return "<h1>Doctor's page</h1> <iframe style=\"border: none; \" src=\"https://cdn.discordapp.com/emojis/791837082237665300.gif?v=1\"></iframe>"
    return render_template("template.html", page_title="Doctors", gif_link="https://cdn.discordapp.com/emojis/791837082237665300.gif?v=1")


@app.route('/chemists')
def chemists_page() -> 'html':
    # return "<h1>Chemist's page</h1> <iframe style=\"border: none; \" src=\"https://cdn.discordapp.com/emojis/754250296980668516.gif?v=11\"></iframe>"
    return render_template("template.html", page_title="Chemists", gif_link="https://cdn.discordapp.com/emojis/754250296980668516.gif?v=11")


app.run(debug=True)
