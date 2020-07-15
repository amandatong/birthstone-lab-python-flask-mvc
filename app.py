# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_display


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/yourbirthstone', methods=['GET', 'POST'])
def birthstone():
    if request.method == 'POST':
        props = get_display(request.form)
        return render_template('results.html', props = props)
    else:
        return "You didn't enter a form!"