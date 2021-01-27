import html

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/entry')
def landing_page() -> 'html':
    return render_template('index.html', the_title='Test run v1.0')

app.run()
