from flask import Blueprint 

item = Blueprint("item", __name__, template_folder="templates")

@item.route("/item")
def show():
    return "This is the item"
