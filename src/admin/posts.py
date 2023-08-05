from flask import Blueprint, render_template
from flask_user import roles_required, login_required
from src.models import User
from app import db

bp = Blueprint('posts', __name__, url_prefix='')

@bp.route('/posts')
# @login_required
@roles_required('Admin')
def posts():
    return render_template(
        'post/list.html',
        title='Dashboard'
    )


@bp.route('/post/new')
# @login_required
@roles_required('Admin')
def post_new():
    return render_template(
        'post/new.html',
        title='Dashboard'
    )


@bp.route('/post/<int:id>')
# @login_required
@roles_required('Admin')
def post_detail():
    return render_template(
        'post/show.html',
        title='Dashboard'
    )


@bp.route('/post/<int:id>/edit')
# @login_required
@roles_required('Admin')
def post_edit():
    return render_template(
        'post/edit.html',
        title='Dashboard'
    )