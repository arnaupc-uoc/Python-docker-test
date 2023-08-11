from flask import Blueprint, render_template

bp = Blueprint("posts", __name__, url_prefix="")


# Admin Post routes


@bp.route("/posts")
def posts():
    return render_template("admin/post/list.html")


@bp.route("/post/new")
def post_new():
    return render_template("admin/post/new.html")


@bp.route("/post/<int:id>")
def post_detail():
    return render_template("admin/post/show.html")


@bp.route("/post/<int:id>/edit")
def post_edit():
    return render_template("admin/post/edit.html")
