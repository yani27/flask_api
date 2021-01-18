## Flask plugin with docker and heroku

<h4> postgresql </h4>

- create database psql named flask_api

<h4> for docker </h4>
- docker-compose up --build

<h4> for heroku </h4>

<h6> production mode </h6>
-heroku run python3 run.py --app flaskapi-pro

<h6> stage mode </h6>
-heroku run python3 run.py --app flaskapi-stage
