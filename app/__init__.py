from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_security import Security, SQLAlchemyUserDatastore


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    
    from .models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
