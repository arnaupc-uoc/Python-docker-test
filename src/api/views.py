from flask import Blueprint, request, jsonify, render_template, current_app as app
from src.models import User
from middleware.token_auth import token_required
import jwt
import os
from app import db
from flask_swagger import swagger
from flask_login import login_required
from src.api.users import bp as users
from src.api.posts import bp as posts

bp = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


# Swagger Endpoints


@login_required
@bp.route("/docs")
def docs():
    return render_template(
        "swagger-ui.html",
    )


@login_required
@bp.route("/spec")
def spec():
    swag = swagger(app)
    # configuration values for swagger 2.0: info and security options
    config = {
        "swagger": "2.0",
        "info": {
            "title": "Sample API",
            "description": "This is a sample api for a simple app.",
            "termsOfService": "/terms",
            "contact": {
                "name": "API Support",
                "url": "/support",
                "email": "support@example.com"
            },
            "version": "1.0.0"
        },
        "securityDefinitions": {
            "apiKey": {
                "type": "apiKey",
                "description": "JWT authorization of an API",
                "in": "header",
                "name": "Authorization"
            }
        },
        "security": [
            {
                "apiKey": []
            }
        ]
    }
    swag.update(config)
    return jsonify(swag)


# API Endpoints


@bp.route("/check-token", methods=["GET"])
@token_required
def check_token(token_user):
    """Endpoint to check user token provided.
    ---
    tags:
        - Token
    responses:
      200:
        description: A JSON object containing a success message.
    """
    return jsonify({"msg": "Token is valid."})


@bp.route("/decode-token", methods=["GET"])
@token_required
def decode_token(token_user):
    """Example endpoint decoding token to return user id.
    ---
    tags:
        - Token
    responses:
      200:
        description: A JSON object containing user info.
    """
    token = request.headers.get("Authorization")
    data = jwt.decode(token, os.environ.get("SECRET_KEY"), algorithms=["HS256"])
    token_user = db.get_or_404(User, data["id"])
    return jsonify(token_user.id)


# Register admin subroutes

bp.register_blueprint(users)
bp.register_blueprint(posts)


# Error handlers
@bp.errorhandler(404)
def _handle_api_error(e):
    if request.path.startswith("/api/"):
        return jsonify({"msg": str(e)}), 404
