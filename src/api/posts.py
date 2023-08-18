from flask import Blueprint, jsonify
from middleware.token_auth import token_required
from src.models import User
from app import db, csrf

bp = Blueprint("api_posts", __name__, url_prefix="")


# Admin Post routes


@bp.route("/posts", methods=["GET"])
@token_required
def posts():
    """Endpoint to get list of posts.
    ---
    tags:
        - Posts
    responses:
      200:
        description: A JSON object containing list of posts.
    """
    return jsonify({"msg": "List of posts."})


@bp.route("/post/<int:id>", methods=["GET"])
@token_required
def post_detail(id):
    """Endpoint to get single post detail.
    ---
    tags:
        - Posts
    parameters:
        - name: id
          description: Post Id
          required: true
          type: integer
          in: path
    responses:
      200:
        description: A JSON object containing post detail.
    """
    return jsonify({"msg": "Post detail."})


@bp.route("/post/<int:id>", methods=["PUT"])
@token_required
@csrf.exempt
def post_update(id):
    """Endpoint to update single post detail.
    ---
    tags:
        - Posts
    parameters:
        - name: id
          description: Post Id
          required: true
          type: integer
          in: path
    responses:
      200:
        description: A JSON object containing updated post detail.
    """
    return jsonify({"msg": "Post detail."})
