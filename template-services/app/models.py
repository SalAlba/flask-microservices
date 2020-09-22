from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()


def init_app(app):
    try:
        db.app = app
        db.init_app(app)
        return db
    except Exception as err:
        print('ERR ==> init_app() ', err)
        return None

def create_tables(app):
    try:
        # ...
        # db.create_all()

        # ...
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        db.metadata.create_all(engine)
        return engine
    except Exception as err:
        print('ERR ==> create_tables() ', err)
        return None


class __Model__(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    col__ = db.Column(db.String(255), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)


    def to_json(self):
        return {
            'col__': self.col__,
        }

