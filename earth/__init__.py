from flask import Blueprint
from earth.functions import crack_stone

earth = Blueprint("earth", __name__, url_prefix="/earth")


@earth.route("/")
def index():
    return "This is earth"


@earth.route("/stone")
def stone():
    return crack_stone()
