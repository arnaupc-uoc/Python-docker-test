from flask import Blueprint, request, jsonify
from src.models import User
from middleware.token_auth import token_required
import jwt
import os

bp = Blueprint('api', __name__, url_prefix='/api')


# API Endpoints

@bp.route('/hi', methods=['GET'])
def say_hello():
    """Returns hello from flask.

    Returns
    -------
    metadata : `lsst.pipe.base.Struct`
        The metadata.
    """
    return jsonify({'msg': 'Hello from Flask.'})


@bp.route('/decode-token', methods=['POST'])
def decode_token():
    token = request.headers.get('Authorization')
    data = jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
    token_user = User.query.get(data['id'])
    return jsonify(token_user.id)


@bp.route('/check-token', methods=['GET'])
@token_required
def check_token(token_user):
    return jsonify({'msg': 'Token is valid.'})


# Error handlers
@bp.errorhandler(404)
def _handle_api_error(e):
    if request.path.startswith('/api/'):
        return jsonify({'msg': str(e)}), 404
