from flask import Blueprint, render_template
from flask_user import roles_required, login_required
from src.models import User
from app import db

bp = Blueprint('users', __name__, url_prefix='')

@bp.route('/users')
# @login_required
@roles_required('Admin')
def users():
    # get all users
    query = db.select(User).order_by(User.username)
    users = db.session.execute(query).scalars()

    return render_template(
        'user/list.html',
        models=users
    )


@bp.route('/user/new')
# @login_required
@roles_required('Admin')
def user_new():
    return render_template(
        'user/new.html'
    )


@bp.route('/user/<int:id>')
# @login_required
@roles_required('Admin')
def user_detail(id):
    user = db.get_or_404(User, id)

    return render_template(
        'user/show.html',
        model=user
    )


@bp.route('/user/<int:id>/edit')
# @login_required
@roles_required('Admin')
def user_edit(id):
    user = db.get_or_404(User, id)

    return render_template(
        'user/edit.html',
        model=user
    )