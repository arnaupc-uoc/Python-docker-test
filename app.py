from dotenv import load_dotenv
from flask import Flask
from flask_assets import Environment
from flask_mail import Mail
import click

# Create Flask application
def create_app():

    flask_app = Flask(__name__, instance_relative_config=False)  # set app
    flask_app.config.from_pyfile('./config.py')  # load config

    # Init assets
    assets = Environment()
    assets.init_app(flask_app)

    with flask_app.app_context():
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