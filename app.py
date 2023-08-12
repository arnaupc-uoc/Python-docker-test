from flask import Flask, jsonify
from flask_assets import Environment
from flask_babelex import Babel
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_caching import Cache
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
import json
import src.logging

# Globally accessible libraries

db = SQLAlchemy()  # set db object global
migrate = Migrate()  # set migrate object global
cors = CORS()  # set cors object global
mail = Mail()  # set mail object global
babel = Babel()  # set babel object global
debug_toolbar = DebugToolbarExtension()  # set debug toolbar object global
csrf = CSRFProtect()  # set csrf object global
cache = Cache()  # set cache object global
assets = Environment()  # set assets object global
login_manager = LoginManager()  # set login manager object global

# Create Flask application


def create_app():
    app = Flask(__name__, instance_relative_config=False)  # set app
    app.config.from_pyfile("./config.py")  # load config

    # Set up extensions

    db.init_app(app)  # initialize it after creating our application
    migrate.init_app(app, db)  # set migrate
    cors.init_app(app)  # set cors
    mail.init_app(app)  # set mail
    babel.init_app(app)  # set babel
    debug_toolbar.init_app(app)  # set debug toolbar
    csrf.init_app(app)  # set csrf
    cache.init_app(app)  # set cache

    login_manager.init_app(app)  # set login manager

    with app.app_context():

        # create/use database
        
        db.create_all()

        # set user manager

        login_manager.login_view = "auth.login"
        login_manager.session_protection = "strong"

        from src.models import User

        @login_manager.user_loader
        def load_user(user_id):
            # query for the user
            return User.query.get(int(user_id))

        assets.init_app(app)  # set assets

        # Swagger

        SWAGGER_URL = "/api/docs"  # URL for exposing Swagger UI (without trailing '/')
        API_URL = ""  # Our API url (can of course be a local resource)

        # Call factory function to create our blueprint
        swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
            API_URL,
            config={  # Swagger UI config overrides
                "app_name": "Test application",
                "swagger": "2.0",
                "info": {
                    "title": "Sample API",
                    "description": "A sample API that demonstrates how to use Flask-SwaggerUI.",
                    "version": "1.0",
                },
                "basePath": "/api",
                "schemes": ["http"],
                "consumes": ["application/json"],
                "produces": ["application/json"],
            },
        )

        app.register_blueprint(swaggerui_blueprint)

        @app.route("/swagger.json")
        def swagger():
            with open("swagger.json", "r") as f:
                return jsonify(json.load(f))

        # Import parts of our application

        # Frontend register
        from src.auth.views import bp as auth
        app.register_blueprint(auth)

        # Frontend register
        from src.frontend.views import bp as front
        app.register_blueprint(front)

        # Panel register
        from src.admin.views import bp as admin
        app.register_blueprint(admin)

        # API register
        from src.api.views import bp as api

        app.register_blueprint(api)

        # Import commands
        from src.commands.utils import bp as cmd_utils

        app.register_blueprint(cmd_utils)

        # Compile static assets
        from src.assets import compile_static_assets

        compile_static_assets(assets)

    return app
