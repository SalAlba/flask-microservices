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


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    items = db.relationship('OrderItem', backref='orderItem')
    is_open = db.Column(db.Boolean, default=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def create(self, user_id):
        self.user_id = user_id
        self.is_open = True
        return self

    def to_json(self):
        items = []
        for i in self.items:
            items.append(i.to_json())

        return {
            'items': items,
            'is_open': self.is_open,
            'user_id': self.user_id
        }


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer, default=1)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

    def to_json(self):
        return {
            'product': self.product_id,
            'quantity': self.quantity,
        }
