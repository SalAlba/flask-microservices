import json

from flask import jsonify, request, render_template
# from flask_login import login_required

from . import product_blueprint as current_blueprint
# from app.core.utils.logger import Logger
from app.models import db, Product

# logger = Logger(__name__).get_logger()


@current_blueprint.route('/', methods=['GET'])
# @login_required
# @loge # TODO ...
def index():
    return {
        'message':{
            'info': 'products services',
            'code': 201
        }
    }


@current_blueprint.route('/products', methods=['GET'])
# @login_required
# @loge # TODO ...
def get_products():
    data = dict(
        result=[row.to_json() for row in Product.query.all()],
        message={
            'info': 'success',
            'code': 201
        },
    )
    return data


@current_blueprint.route('product/<slug>', methods=['GET'])
# @login_required
# @loge # TODO ...
def product_by_slug(slug):
    item = Product.query.filter_by(slug=slug).first()
    if item:
        response = dict(
            result=item.to_json(),
            message={
                'info': 'success',
                'code': 201
            },
        )
    else:
        response = dict(
            message={
                'info': 'not found product',
                'code': 404
            }
        ), 404
    return response


@current_blueprint.route('product/create', methods=['POST'])
# @login_required
# @loge # TODO ...
def create_product():
    # ...
    data = request.get_json()
    print('\n\ncreate_user()')
    print(json.dumps(data, indent=4))
    name = data.get('name')
    slug = data.get('slug')
    image = data.get('image')
    price = data.get('price')

    # ...
    item = Product()
    item.name = name
    item.slug = slug
    item.image = image
    item.price = price

    db.session.add(item)
    db.session.commit()

    # ...
    response = dict(
        result=item.to_json(),
        message={
            'info': 'Product added',
            'code': 201
        },
    )

    return response
