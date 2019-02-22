from flask import Flask
from web.public import course
from exercise.api import item
from ext import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///alabala.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATION"] = True

db.init_app(app)


@app.before_first_request
def create():
    db.create_all()


@app.route("/")
def hello():
    return "Hello world"

app.register_blueprint(course, url_prefix = "/api/v3/course")


app.register_blueprint(item, url_prefix = "/api/v2/item")

