from app import app
from app import helpers
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/people")
def people():
    tableLabel = helpers.peopleList()
    return render_template("people.html", variable = tableLabel)

@app.route("/starships")
def starships():
    tableLabel = helpers.starshipList()
    return render_template("starships.html", variable = tableLabel)
   
