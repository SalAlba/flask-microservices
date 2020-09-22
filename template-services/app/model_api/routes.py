from flask import jsonify, render_template
# from flask_login import login_required

from . import model_blueprint as current_blueprint
# from app.core.utils.logger import Logger
from app.models import db, __Model__

# logger = Logger(__name__).get_logger()


@current_blueprint.route('/', methods=['GET'])
# @login_required
# @loge # TODO ...
def index():
    return {
        'message':{
            'info': 'microservices template',
            'code': 201
        }
    }



@current_blueprint.route('/models', methods=['GET'])
# @login_required
# @loge # TODO ...
def get_all_models__():
    data = dict(
        data=[row.to_json() for row in __Model__.query.all()],
        message={
            'info': 'success',
            'code': 201
        },
    )
    return data
