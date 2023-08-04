from flask import Blueprint, render_template, jsonify, current_app
from flask_user import current_user, user_manager
from src.models import User, Role
from app import db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/hello', methods=['GET'])
def say_hello():
    return jsonify({'msg': 'Hello from Flask.'})


@bp.route('/create-user', methods=['GET'])
def create_user():

    try:
        # Creare 'admin' role
        admin_role = Role(name='Admin')
        db.session.add(admin_role)

        # # Create 'user007' user with 'secret' and 'agent' roles
        # user1 = User(
        #     username = 'user007', email='admin@example.com', active=True,
        #     password = user_manager.hash_password('Password1'))
        # user1.roles = [admin_role,]
        # db.session.add(user1)

        # db.session.commit()

        return jsonify({'msg': 'Example user created.'})

    except Exception as e:
        return jsonify({'msg': str(e) })


# Error handlers
@bp.errorhandler(404)
@bp.errorhandler(405)
def _handle_api_error(ex):
    if request.path.startswith('/api/'):
        return jsonify_error(ex)