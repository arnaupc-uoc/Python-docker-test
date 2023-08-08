from flask import Blueprint, request, render_template, jsonify, current_app as app
from flask_swagger import swagger
from src.models import User, Role
from app import db
from middleware.token_auth import token_required
from flask_swagger_ui import get_swaggerui_blueprint

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



@bp.route('/check-token', methods=['GET'])
@token_required
def check_token():
    return jsonify({'msg': 'Token is valid.'})


@bp.route('/create-user', methods=['GET'])
def create_user():

    try:
        # Creare 'admin' role
        admin_role = Role(name='Admin')
        db.session.add(admin_role)

        # Create 'user007' user with 'secret' and 'agent' roles
        user1 = User(
            username = 'user007', 
            email='admin@example.com', 
            password = app.user_manager.hash_password('Password1'),
            first_name='James',
            last_name='Bond',
            active=True
        )
        user1.roles = [admin_role]
        db.session.add(user1)

        db.session.commit() # write changes to the database

        return jsonify({'msg': 'Example user created.'})

    except Exception as e:
        return jsonify({'msg': str(e) })


# Error handlers
@bp.errorhandler(404)
def _handle_api_error(e):
    if request.path.startswith('/api/'):
        return jsonify({'msg': str(e) }), 404