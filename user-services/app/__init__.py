
from flask import Flask

from flask_cors import CORS
# from flask_jwt_extended import JWTManager

# from app.config import configure_app
from . import models
# from app.modules.home import home_blueprint
# from app.modules.mail import mail_blueprint
from app.user_api import user_blueprint


def create_app():
    try:
        # ...
        app = Flask(__name__)

        # ...
        # configure_app(app)
        # CORS(app)
        init_db(app)
        register_modules(app)
        # register_extensions(app)
        # register_errorhandlers(app)
        # register_shellcontext(app)
        return app
    except Exception as err:
        # app.logger.exception('__init__()  ==>  {err}.'.format(err=err))
        print('__init__()  ==>  {err}.'.format(err=err))
        return None

def register_modules(app):
    app.register_blueprint(user_blueprint, url_prefix='/api')

def init_db(app):
    app.config.update(dict(
        # SECRET_KEY="powerful secretkey",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_DATABASE_URI='sqlite:///db.sqllite3',
    ))
    models.init_app(app)
    models.create_tables(app)

def app_config():
    return app.config