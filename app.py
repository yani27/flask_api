from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import requests


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/flask_api"

# db = SQLAlchemy(app)
# db.create_all()
# from models import User


@app.route("/")
def index():

    url = "https://elenasport-io1.p.rapidapi.com/v2/leagues"

    querystring = {"page": "1"}

    headers = {
        'x-rapidapi-key': "f1627161dbmshd649e45ef5916fcp17cc65jsnebacaaea77f8",
        'x-rapidapi-host': "elenasport-io1.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    print(response.text)
    return render_template('index.html')
