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

    item = User.query.filter_by(username=username).first()
    if not item:
        response = jsonify(dict(
            result=item,
            message={
                'info': 'success',
                'code': 201
            },
        ))
    else:
        response = jsonify(dict(
            message={
                'info': 'success',
                'code': 201
            }
            )), 404

    return response


@user_api_blueprint.route('/api/user/create', methods=['POST'])
# @login_required
# @loge # TODO ...
def create_user():
    first_name = request.get('first_name')
    last_name = request.get('last_name')
    email = request.get('email')
    username = request.get('username')
    password = sha256_crypt.hash((str(request.get('password'))))

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
