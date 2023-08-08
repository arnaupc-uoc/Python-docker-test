from flask import Blueprint, render_template, redirect, url_for, current_app as app, jsonify
from flask_user import roles_required, current_user, login_required
from src.models import User, Role
from app import db
import jwt
from datetime import datetime, timezone, timedelta

bp = Blueprint('admin', __name__, template_folder='../../templates/admin', static_folder='../../static/admin', url_prefix='/admin')

# Admin routes

@bp.route('/')
def main():
    # check is logged and redirect
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    else:
        return redirect('/admin/login')


@bp.route('/dashboard')
# @login_required
@roles_required('Admin')
def dashboard():
    return render_template(
        'admin/dashboard.html'
    )


@bp.route('/get-token', methods=['GET'])
@roles_required('Admin')
def get_token():
    # generates the JWT Token
    token = jwt.encode({
        'id': current_user.id,
        'email': current_user.email,
        'exp' : datetime.now(timezone.utc) + timedelta(days = 30)
    }, app.config['SECRET_KEY'])
  
    return jsonify({'token' : token}), 201


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


# Admin subroutes

from src.admin.users import bp as users
bp.register_blueprint(users)

from src.admin.posts import bp as posts
bp.register_blueprint(posts)


# Error handlers

@bp.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('admin/error.html'), 404  # need folder