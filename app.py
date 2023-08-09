from flask import Flask, jsonify
from flask_assets import Environment
from flask_babelex import Babel
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager
from flask_swagger_ui import get_swaggerui_blueprint
from flask_debugtoolbar import DebugToolbarExtension
import json

db = SQLAlchemy()  # set db object global
migrate = Migrate()  # set migrate object global


# Create Flask application
def create_app():

    app = Flask(__name__, instance_relative_config=False)  # set app
    app.config.from_pyfile('./config.py')  # load config

    db.init_app(app)  # initialize it after creating our application
    migrate.init_app(app, db)  # set migrate

    Mail(app)  # set mail
    Babel(app)  # set babel
    DebugToolbarExtension(app)  # set debug toolbar

    # Init assets
    assets = Environment()
    assets.init_app(app)

    with app.app_context():

        import src.models as models
        db.create_all()

        # set user manager
        UserManager(app, db, models.User)

        # Swagger

        SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
        API_URL = ''  # Our API url (can of course be a local resource)

        # Call factory function to create our blueprint
        swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
            API_URL,
            config={  # Swagger UI config overrides
                'app_name': "Test application",
                "swagger": "2.0",
                "info": {
                    "title": "Sample API",
                    "description": "A sample API that demonstrates how to use Flask-SwaggerUI.",
                    "version": "1.0"
                },
                "basePath": "/api",
                "schemes": [
                    "http"
                ],
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ]
            }
        )

        app.register_blueprint(swaggerui_blueprint)

        @app.route('/swagger.json')
        def swagger():
            with open('swagger.json', 'r') as f:
                return jsonify(json.load(f))

        # Import parts of our application

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
