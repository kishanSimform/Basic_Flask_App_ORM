from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
api = Api()
api.endpoints


def setup_with_app(main_app):
    api.init_app(main_app)
    db.init_app(main_app)
    migrate.init_app(main_app, db)
    ma.init_app(main_app)