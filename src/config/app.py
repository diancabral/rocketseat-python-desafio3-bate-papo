from flask import Flask
from flask_socketio import SocketIO

from config.constants import SECRET_KEY

from .routes import register_routes_and_events

socketio = SocketIO()


def create_app(config_name: str = "default") -> Flask:
    app = Flask(__name__, template_folder="../templates")

    socketio.init_app(app)

    app.config["SECRET_KEY"] = SECRET_KEY

    register_routes_and_events(app)

    return app
