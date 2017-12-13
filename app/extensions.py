from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_bootstrap import Bootstrap
from flask_apscheduler import APScheduler

db = SQLAlchemy()
security = Security()
bootstrap = Bootstrap()
scheduler = APScheduler()
