from app import app
from app import views
from flask import Flask
import requests
import json
import string
import pandas as pd

def peopleList():
    #Coletando os dados a API People
    url = "https://swapi.dev/api/people/"
    try:
        Response = requests.get(url)
    except requests.ConnectionError:
       return "Connection Error" 
 
    Response_json = Response.text

    #Usando pandas para manuseas o JSON
    dicJs = pd.read_json(Response_json)

    #Começando a tratar o json que transformei em um dicionario, para criar uma table em html
    tableLabel = "<table id='example' class='table table-striped table-bordered table-hover' cellspacing='0' width='100%'> <thead> <tr> <th>Name</th> <th>Gender</th> <th>Mass</th> <th>Height</th> <th>Film</th> <th>Starship</th> <th>Vehicle</th> <th>Planet</th> </tr></thead> <tbody>"
    tableBody = ""
    film = " "
    starship = " "
    vehicle = " "
    planet = " "
    for keys in range (0,10):
        film = " " 
        starship = " "
        vehicle = " "
        planet = " "
        if len(dicJs["results"][keys]["films"]) != 0:
            film = ""
            for i in range(0, len(dicJs["results"][keys]["films"])):
                if len(dicJs["results"][keys]["films"][i]) > 10:
                    url2 = dicJs["results"][keys]["films"][i]
                    try:
                        Response2 = requests.get(url2)
                    except requests.ConnectionError:
                        return "Connection Error"
                    Response2_json = Response2.text
                    dicJs2 = json.loads(Response2_json)
                    film = film + " | " + dicJs2["title"]

        if len(dicJs["results"][keys]["vehicles"]) != 0:
            vehicle = ""
            for i in range(0, len(dicJs["results"][keys]["vehicles"])):
                if len(dicJs["results"][keys]["vehicles"][i]) > 10:
                    url3 = dicJs["results"][keys]["vehicles"][i]
                    try:
                        Response3 = requests.get(url3)
                    except requests.ConnectionError:
                        return "Connection Error"
                    Response3_json = Response3.text
                    dicJs3 = json.loads(Response3_json)
                    vehicle = vehicle + " | " + dicJs3["name"]

        if len(dicJs["results"][keys]["starships"]) != 0:
            starship = ""
            for i in range(0, len(dicJs["results"][keys]["starships"])):
                if len(dicJs["results"][keys]["starships"][i]) > 10:
                    url4 = dicJs["results"][keys]["starships"][i]
                    try:
                        Response4 = requests.get(url4)
                    except requests.ConnectionError:
                        return "Connection Error"
                    Response4_json = Response4.text
                    dicJs4 = json.loads(Response4_json)
                    starship = starship + " | " + dicJs4["name"]

        if len(dicJs["results"][keys]["homeworld"]) != 0:
            planet = ""
            for i in range(0, 1):
                if len(dicJs["results"][keys]["homeworld"]) > 10:
                    url5 = dicJs["results"][keys]["homeworld"]
                    try:
                        Response5 = requests.get(url5)
                    except requests.ConnectionError:
                        return "Connection Error"
                    Response5_json = Response5.text
                    dicJs5 = json.loads(Response5_json)
                    planet = planet + dicJs5["name"]
            
        tableBody =  tableBody + "<tr>"
        tableBody = tableBody + "<td>" + dicJs["results"][keys]["name"] + "</td>" + "<td>" + dicJs["results"][keys]["gender"] + "</td>" + "<td>" + dicJs["results"][keys]["mass"] + "</td>" + "<td>" + dicJs["results"][keys]["height"] + "</td>" + "<td>" + film + "</td>" + "<td>" + starship + "</td>" + "<td>" + vehicle + "</td>" + "<td>" + planet + "</td>" + "</tr>"
        tableBody = tableBody + "</tr>"
    tableLabel = tableLabel + tableBody + "</tbody> </table>"
    return tableLabel

def starshipList():
    #Coletando os dados a API
    url = "https://swapi.dev/api/starships/"
    try:
        Response = requests.get(url)
    except requests.ConnectionError:
       return "Connection Error" 
 
    Response_json = Response.text

    #Usando pandas para manuseas o JSON
    dicJs = pd.read_json(Response_json)

    #Começando a tratar o json que transformei em um dicionario, para criar uma table em html
    tableLabel = "<table id='example' class='table table-striped table-bordered table-hover' cellspacing='0' width='100%'> <thead> <tr> <th>Name</th> <th>Model</th> <th>Manufacturer</th> <th>Length</th> <th>Crew</th> <th>Score</th> </tr></thead> <tbody>"
    score = 0
    num1 = 0
    num2 = 0
    tableBody = ""
    for keys in range (0,10):
        if dicJs["results"][keys]["cost_in_credits"] == "unknown":
            score = dicJs["results"][keys]["cost_in_credits"]

        else:
            num1 = float(dicJs["results"][keys]["hyperdrive_rating"])
            num2 = int(dicJs["results"][keys]["cost_in_credits"])
            score = num1/num2
            score = round(score,10)
            score = str(score)
        tableBody =  tableBody + "<tr>"
        tableBody = tableBody + "<td>" + dicJs["results"][keys]["name"] + "</td>" + "<td>" + dicJs["results"][keys]["model"] + "</td>" + "<td>" + dicJs["results"][keys]["manufacturer"] + "</td>" + "<td>" + dicJs["results"][keys]["length"] + "</td>" + "<td>" + dicJs["results"][keys]["crew"] + "</td>" + "<td>"+score+"</td>" + "</tr>"
        tableBody = tableBody + "</tr>"
    tableLabel = tableLabel + tableBody + "</tbody> </table>"

    return tableLabel
