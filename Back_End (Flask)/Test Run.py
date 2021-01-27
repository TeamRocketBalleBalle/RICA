import html

try:
    from flask import Flask, render_template
except ModuleNotFoundError as e:
    print(e)
    print("Flask module not found. Is flask installed on your computer? \ntry running: \npython -m pip install flask")
    quit()

app = Flask(__name__)


@app.route('/')
def landing_page() -> 'html':
    return render_template('index.html')


@app.route('/patients')
def patients_page() -> 'html':
    return "<h1>Patients page</h1> <iframe style=\"border: none; \" src=\"https://cdn.discordapp.com/emojis/768874484429226004.gif?v=1\"></iframe>"


app.run(debug=True)
