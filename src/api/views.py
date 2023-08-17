from flask import Blueprint, request, jsonify, render_template, current_app as app
from src.models import User
from middleware.token_auth import token_required
import jwt
import os
from app import db
from flask_swagger import swagger
from flask_login import login_required

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
    # configuration values for swagger 2.0
    config = {
        "info": {
            "title": "Sample API",
            "summary": "User and posts CRUD an other utilities.",
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
            'api_key': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authoriation'
            }
        },
        "security": {
            'api_key': []
        }
    }
    swag.update(config)
    return jsonify(swag)


# API Endpoints


@bp.route("/hi", methods=["GET"])
def say_hello():
    """Example endpoint returning a welcome message.
    This is using docstrings for specifications.
    ---
    tags:
        - Example
    responses:
      200:
        description: A JSON object containing a welcome message.
    """
    return jsonify({"msg": "Hello from Flask."})


@bp.route("/decode-token", methods=["POST"])
def decode_token():
    token = request.headers.get("Authorization")
    data = jwt.decode(token, os.environ.get("SECRET_KEY"), algorithms=["HS256"])
    token_user = db.get_or_404(User, data["id"])
    return jsonify(token_user.id)


@bp.route("/check-token", methods=["GET"])
@token_required
def check_token(token_user):
    """Endpoint to check user token provided.
    ---
    tags:
        - Example
    responses:
      200:
        description: A JSON object containing a success message.
    """
    return jsonify({"msg": "Token is valid."})


# Error handlers
@bp.errorhandler(404)
def _handle_api_error(e):
    if request.path.startswith("/api/"):
        return jsonify({"msg": str(e)}), 404
