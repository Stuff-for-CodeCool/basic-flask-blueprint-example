from flask import Blueprint

sky = Blueprint("sky", __name__, url_prefix="/sky")


@sky.route("/")
def index():
    return "This is the sky"


@sky.route("/cloud")
def cloud():
    return "This is in the sky"
