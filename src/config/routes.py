from flask import Flask

from modules import chat_api


def register_routes_and_events(app: Flask):
    app.register_blueprint(chat_api)

    import modules.socket.events
