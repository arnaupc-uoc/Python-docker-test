from flask import Blueprint, request, render_template, jsonify, current_app as app
from flask_swagger import swagger
from src.models import User, Role
from app import db
from middleware.token_auth import token_required
from flask_swagger_ui import get_swaggerui_blueprint
import jwt
import os

bp = Blueprint('api', __name__, url_prefix='/api')

# Swagger

SWAGGER_URL = '/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

bp.register_blueprint(swaggerui_blueprint)

@bp.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))


# API Endpoints 

@bp.route('/hello', methods=['GET'])
def say_hello():
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


# Error handlers
@bp.errorhandler(404)
def _handle_api_error(e):
    if request.path.startswith('/api/'):
        return jsonify({'msg': str(e) }), 404