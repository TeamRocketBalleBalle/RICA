import html
try:
    from flask import Flask, render_template
except ModuleNotFoundError as e:
    print(e)
    print("Flask module not found. Is flask installed on your computer? \ntry running: \npython -m pip install flask")
    quit()

    
app = Flask(__name__,static_folder="templates")


@app.route('/entry')
def landing_page() -> 'html':
    return render_template('index.html')


app.run(debug=True)
