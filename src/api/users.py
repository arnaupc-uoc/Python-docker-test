from flask import Blueprint, request, jsonify
from middleware.token_auth import token_required
from src.models import User
from app import db, csrf

bp = Blueprint("api_users", __name__, url_prefix="")
csrf.exempt(bp)  # TODO: disable csrf protection for this blueprint, not working, waitin for next version of Flask-wtf !!!


# Admin User routes


@bp.route("/users", methods=["GET"])
@token_required
def users():
    """Endpoint to get list of users.
    ---
    tags:
        - Users
    responses:
      200:
        description: A JSON object containing list of users.
    """
    return jsonify({"msg": "List of users."})
    # get all users
    # query = db.select(User).order_by(User.username)
    # users = db.session.execute(query).scalars()

    # return render_template("admin/user/list.html", models=users)


@bp.route("/user/<int:id>", methods=["GET"])
@token_required
def user_update(id):
    """Endpoint to get single user detail.
    ---
    tags:
        - Users
    parameters:
        - name: id
          description: User Id
          required: true
          type: integer
          in: path
    responses:
      200:
        description: A JSON object containing user detail.
    """
    return jsonify({"msg": "User detail."})
    # user = db.get_or_404(User, id)

    # return render_template("admin/user/show.html", model=user)


@bp.route("/user/<int:id>", methods=["PUT"])
@token_required
@csrf.exempt
def user_detail(id):
    """Endpoint to update single user detail.
    ---
    tags:
        - Users
    parameters:
        - name: id
          description: User Id
          required: true
          type: integer
          in: path
    responses:
      200:
        description: A JSON object containing updated user detail.
    """
    return jsonify({"msg": "User detail."})
    # user = db.get_or_404(User, id)

    # return render_template("admin/user/show.html", model=user)
