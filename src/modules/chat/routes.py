from flask import Blueprint, render_template

from config.constants import API_PREFIX

api = Blueprint("chat", __name__, url_prefix=f"{API_PREFIX}/v1/chat/")


@api.route("/", methods=["GET"])
def index():
    return render_template("index.html", host="http://127.0.0.1:5000")
