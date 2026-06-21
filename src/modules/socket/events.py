from datetime import datetime

from flask_socketio import emit

from config.app import socketio


@socketio.on("connect")
def handle_user_connect():
    print("[SocketIO] New session started at: ", datetime.now())


@socketio.on("join")
def handle_user_join(data):
    print("[SocketIO] User joined the session:", data)
    emit("join", data, broadcast=True)


@socketio.on("message_send")
def handle_user_message(data):
    print("[SocketIO] User send message:", data)
    emit("message_send", data, broadcast=True, include_self=False)


@socketio.on("typing_started")
def handle_user_typing_started(data):
    print("[SocketIO] User started typing on the session:", data)
    emit("typing_started", data, broadcast=True, include_self=False)


@socketio.on("typing_stopped")
def handle_user_typing_stopped(data):
    print("[SocketIO] User stopped typing on the session:", data)
    emit("typing_stopped", data or {}, broadcast=True, include_self=False)
