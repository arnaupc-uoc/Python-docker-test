from flask import Blueprint, render_template
from flask_user import roles_required

bp = Blueprint('admin', __name__, template_folder='../../templates/admin', static_folder='../../static/admin', url_prefix='/admin')

# Frontend routes

@bp.route('/')
def main():
    return render_template(
        'admin.html',  # from templates folder
        title='Admin',
        content='Smarter page templates with Flask & Jinja.'
    )

@bp.route('/login')
def login():
    return render_template(
        'main.html',  # from templates folder
        title='Login',
        content='Smarter page templates with Flask & Jinja.'
    )

@bp.route('/dashboard')
@roles_required('Admin')
def dashboard():
    return render_template(
        'main.html',  # from templates folder
        title='Dashboard',
        content='xxx'
    )