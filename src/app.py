from flask import Flask
from src.utils.config import Config
from src.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    db.app = app
    db.create_all()
    return app
