import html

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'hello World'


@app.route('/entry')
def landing_page() -> 'html':
    return render_template('index.html')


app.run()
