from flask import Blueprint, render_template, jsonify, render_template, request, redirect, url_for, abort
from flask_assets import Bundle, Environment
from flask_user import roles_required

bp = Blueprint('admin', __name__, template_folder='templates', static_folder='static', url_prefix='/admin')

# Frontend routes

@bp.route('/')
def main():
    return render_template(
        'main.html',  # from templates folder
        title='Admin',
        content='Smarter page templates with Flask & Jinja.'
    )

@bp.route('/dashboard')
# @roles_required('Admin')
def dashboard():
    return render_template(
        'main.html',  # from templates folder
        title='Dashboard',
        content='xxx'
    )