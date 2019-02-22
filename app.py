from flask import Flask
from web.public import course
from exercise.api import item

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

app.register_blueprint(course, url_prefix = "/api/v3/course")


app.register_blueprint(item, url_prefix = "/api/v2/item")
