from flask import Blueprint, render_template, jsonify

mod = Blueprint('api', __name__, template_folder='templates', static_folder='static', url_prefix='/api')

# API routes

@mod.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask."})


# Error handlers
