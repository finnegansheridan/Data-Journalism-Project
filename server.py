# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/borough')
def year():
    return render_template("borough.html")


app.run(debug=True)