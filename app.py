from dotenv import load_dotenv
from flask import Flask
from flask_assets import Environment
from flask_babelex import Babel
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import click

db = SQLAlchemy() # set db object global

# Create Flask application
def create_app():

    flask_app = Flask(__name__, instance_relative_config=False)  # set app
    flask_app.config.from_pyfile('./config.py')  # load config

    db.init_app(flask_app) # initialize it after creating our application
    migrate = Migrate(flask_app, db) # set migrate

    mail = Mail(flask_app)  # set mail
    babel = Babel(flask_app) # set babel

    # Init assets
    assets = Environment()
    assets.init_app(flask_app)

    with flask_app.app_context():

        # Create tables
        import apps.models as models
        db.create_all()

        # Import parts of our application
        
        # Frontend register
        from apps.frontend.views import bp as front
        flask_app.register_blueprint(front)
        
        # Panel register
        from apps.admin.views import bp as admin
        flask_app.register_blueprint(admin)

        # API register
        from apps.api.views import bp as api
        flask_app.register_blueprint(api)

        # Import commands
        from apps.commands.utils import bp as cmd_utils
        flask_app.register_blueprint(cmd_utils)

        # Compile static assets
        from apps.assets import compile_static_assets
        compile_static_assets(assets)

        return flask_app