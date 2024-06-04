from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    socketio.init_app(app, cors_allowed_origins="*")

    from .app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
