from dotenv import load_dotenv
from flask import Flask
from flask_assets import Environment
from flask_babelex import Babel
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager
import click

db = SQLAlchemy() # set db object global

# Create Flask application
def create_app():

    app = Flask(__name__, instance_relative_config=False)  # set app
    app.config.from_pyfile('./config.py')  # load config

    db.init_app(app) # initialize it after creating our application
    migrate = Migrate(app, db) # set migrate

    mail = Mail(app)  # set mail
    babel = Babel(app) # set babel

    # Init assets
    assets = Environment()
    assets.init_app(app)

    with app.app_context():

        # Create tables
        import src.models as models
        db.create_all()
        user_manager = UserManager(app, db, models.User)  # set user manager

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