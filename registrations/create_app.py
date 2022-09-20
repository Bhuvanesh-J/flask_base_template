
from flask import  Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from registrations.databases import connect_to_db
from registrations.register_blueprint import register_blueprint
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app = register_blueprint(app)
    app = connect_to_db(app)
    db.init_app(app)
    Migrate(app, db)
    # homepage(app)
    # middleware(app)
    # global_errorhandler(app)

    return app