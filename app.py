from flask import Flask, render_template


app = Flask(__name__)

# https://flaskapi-stage.herokuapp.com/ | https://git.heroku.com/flaskapi-stage.git
# https://flaskapi-pro.herokuapp.com/ | https://git.heroku.com/flaskapi-pro.git


@app.route("/")
def index():
    return render_template('index.html')
