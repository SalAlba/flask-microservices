from flask import Blueprint
model_blueprint = Blueprint('model', __name__, template_folder='templates')
from . import routes