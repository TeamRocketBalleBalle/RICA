import html

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/entry')
def landing_page() -> 'html':
    return render_template('index.html')


app.run()
