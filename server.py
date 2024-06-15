# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import numpy as np
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def about():
    return render_template("about.html")
@app.route('/city')
def city():
    f = open("data/macro.json", "r")
    data = json.load(f)
    f.close()
    year = "2016"
    Bronx = ((data["Bronx"][year]))
    Brooklyn =(data["Brooklyn"][year])
    Manhattan = ((data["Manhattan"][year]))
    Queens =((data["Queens"][year]))
    Staten_Island = ((data["Staten_Island"][year]))
    
    return render_template(
        "index.html", year=year, Bronx=Bronx, Brooklyn=Brooklyn, Manhattan=Manhattan, Queens = Queens, Staten_Island= Staten_Island
    )
    
@app.route('/borough')
def borough():
    f = open("data/micro.json", "r")
    data = json.load(f)
    f.close()
    bxData = []
    for x in data["Bronx"].values():
        bxData.append(x)
    bkData = []
    for x in data["Brooklyn"].values():
        bkData.append(x)
    manData = []
    for x in data["Manhattan"].values():
        manData.append(x)
    queData = []
    for x in data["Queens"].values():
        queData.append(x)
    siData = []
    for x in data["Staten_Island"].values():
        siData.append(x)
    
    bxLine = []
    for i in range(len(bxData) - 1):
        bxLine.append([bxData[i], bxData[i + 1]])
    bkLine = []
    for i in range(len(bkData) - 1):
        bkLine.append([bkData[i], bkData[i + 1]])
    manLine = []
    for i in range(len(manData) - 1):
        manLine.append([manData[i], manData[i + 1]])
    queLine = []
    for i in range(len(queData) - 1):
        queLine.append([queData[i], queData[i + 1]])
    siLine = []
    for i in range(len(siData) - 1):
        siLine.append([siData[i], siData[i + 1]])
    return render_template("borough.html", years=data["Bronx"].keys(),Bronx=bxLine,Brooklyn=bkLine,Manhattan=manLine,Queens=queLine,Staten_Island=siLine)
app.run(debug=True)
