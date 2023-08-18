from flask import Blueprint, jsonify
from middleware.token_auth import token_required
from src.models import User, UserSchema
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
    query = db.select(User).order_by(User.id)
    users = db.session.execute(query).scalars()
    schema = UserSchema()
    result = schema.dump(users, many=True)
    return jsonify(result)


@bp.route("/user/<int:id>", methods=["GET"])
@token_required
def user_detail(id):
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
    user = db.get_or_404(User, id)
    schema = UserSchema()
    result = schema.dump(user)
    return jsonify(result)


@bp.route("/user/<int:id>", methods=["PUT"])
@token_required
@csrf.exempt
def user_update(id):
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
    user = db.get_or_404(User, id)
    schema = UserSchema()
    result = schema.dump(user)
    return jsonify(result)
