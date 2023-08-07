from flask import Blueprint, render_template
from flask_user import roles_required, login_required
from src.models import User
from app import db

bp = Blueprint('posts', __name__, url_prefix='')

# Admin Post routes

@bp.route('/posts')
# @login_required
@roles_required('Admin')
def posts():
    return render_template(
        'admin/post/list.html'
    )


@bp.route('/post/new')
# @login_required
@roles_required('Admin')
def post_new():
    return render_template(
        'admin/post/new.html'
    )


@bp.route('/post/<int:id>')
# @login_required
@roles_required('Admin')
def post_detail():
    return render_template(
        'admin/post/show.html'
    )


@bp.route('/post/<int:id>/edit')
# @login_required
@roles_required('Admin')
def post_edit():
    return render_template(
        'admin/post/edit.html'
    )