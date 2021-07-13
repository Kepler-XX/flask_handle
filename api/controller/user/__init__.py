from flask import Blueprint
user_api = Blueprint('user', __name__)
from . import userapi
