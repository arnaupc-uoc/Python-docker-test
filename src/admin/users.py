from flask import Blueprint, render_template, request
from flask import current_app as app
from src.models import User
from app import db

bp = Blueprint("users", __name__, url_prefix="")


# Admin User routes
# TODO: queries !!!

@bp.route("/users")
def users():
    # get all users
    query = db.select(User).order_by(User.username)
    users = db.session.execute(query).scalars()

    return render_template("admin/user/list.html", models=users)


@bp.route("/user/new")
def user_new():
    if request.method == "POST":
        print("post new user...")
    else:
        return render_template("admin/user/new.html")


@bp.route("/user/<int:id>")
def user_detail(id):
    user = db.get_or_404(User, id)

    return render_template("admin/user/show.html", model=user)


@bp.route("/user/<int:id>/edit")
def user_edit(id):
    if request.method == "POST":
        print("post new user...")
    else:
        user = db.get_or_404(User, id)

        return render_template("admin/user/edit.html", model=user)
