import json

from flask import jsonify, request, render_template
# from flask_login import login_required

from . import order_blueprint as current_blueprint
# from app.core.utils.logger import Logger
from app.models import db, Order, OrderItem
from app.order_api.api.UserClient import UserClient

# logger = Logger(__name__).get_logger()


@current_blueprint.route('/', methods=['GET'])
# @login_required
# @loge # TODO ...
def index():
    return {
        'message':{
            'info': 'order microservices',
            'code': 201
        }
    }


@current_blueprint.route('/orders', methods=['GET'])
# @login_required
# @loge # TODO ...
def get_orders():
    data = dict(
        data=[row.to_json() for row in Order.query.all()],
        message={
            'info': 'success',
            'code': 201
        },
    )
    return data


@current_blueprint.route('/order/add-item', methods=['POST'])
def order_add_item():
    # ...
    # api_key = request.headers.get('Authorization')
    # response = UserClient.get_user(api_key)

    # if not response:
    #     return make_response(jsonify({'message': 'Not logged in'}), 401)

    # user = response['result']
    # ...
    data = request.get_json()
    print('\n\norder_add_item()')
    print(json.dumps(data, indent=4))

    p_id = int(data.get('product_id'))
    qty = int(data.get('qty'))
    # u_id = int(user['id'])
    u_id = int(data.get('user_id'))

    # Find open order
    known_order = Order.query.filter_by(user_id=u_id, is_open=1).first()

    if not known_order:
        # Create the order
        known_order = Order()
        known_order.is_open = True
        known_order.user_id = u_id

        order_item = OrderItem(p_id, qty)
        known_order.items.append(order_item)
    else:
        found = False
        # Check if we already have an order item with that product
        for item in known_order.items:
            if item.product_id == p_id:
                found = True
                item.quantity += qty

        if not found:
            order_item = OrderItem(p_id, qty)
            known_order.items.append(order_item)

    db.session.add(known_order)
    db.session.commit()

    # ...
    response = dict(
        result=item.to_json(),
        message={
            'info': 'Order added',
            'code': 201
        },
    )

    return response

