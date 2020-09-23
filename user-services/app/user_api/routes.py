import json
from passlib.hash import sha256_crypt

from flask import jsonify, request, render_template
# from flask_login import login_required

from . import user_blueprint as current_blueprint
# from app.core.utils.logger import Logger
from app.models import db, User

# logger = Logger(__name__).get_logger()


@current_blueprint.route('/', methods=['GET'])
# @login_required
# @loge # TODO ...
def index():
    return {
        'message':{
            'info': 'user services',
            'code': 201
        }
    }


@current_blueprint.route('/users', methods=['GET'])
# @login_required
# @loge # TODO ...
def get_users():
    data = dict(
        result=[row.to_json() for row in User.query.all()],
        message={
            'info': 'success',
            'code': 201
        },
    )
    return data


@current_blueprint.route('/user/id/<_id>', methods=['GET'])
# @login_required
# @loge # TODO ...
def get_user_by_id(_id):
    item = User.query.filter_by(id=_id).first()
    if not item:
        response = jsonify(dict(
            message={
                'info': 'user not found',
                'code': 404
            },
        )), 404
    else:
        response = jsonify(dict(
            result=item.to_json(),
            message={
                'info': 'success',
                'code': 201
            }
        ))

    return response


@current_blueprint.route('/user/create', methods=['POST'])
# @login_required
# @loge # TODO ...
def create_user():
    # ...
    data = request.get_json()
    print('\n\ncreate_user()')
    print(json.dumps(data, indent=4))
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    username = data.get('username')
    password = sha256_crypt.hash((str(data.get('password'))))

    # TODO move to controller ..
    user = User()
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.password = password
    user.username = username
    user.authenticated = True
    user.active = True

    # ...
    db.session.add(user)
    db.session.commit()

    response = dict(
        result=user.to_json(),
        message={
            'info': 'User added',
            'code': 201
        },
    )

    return jsonify(response)
