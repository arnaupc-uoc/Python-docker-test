from dotenv import load_dotenv
from flask import Flask
from flask_assets import Bundle, Environment
from flask.cli import with_appcontext
import click

# Create Flask application
def create_app():

    app = Flask(__name__, instance_relative_config=False)  # set app
    app.config.from_pyfile('./config.py')  # load config

    # Init assets
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our application
        
        # Frontend register
        from frontend.views import bp as front
        app.register_blueprint(front)

        # API register
        from api.views import bp as api
        app.register_blueprint(api)

        # Import commands
        from commands.utils import bp as cmd_utils
        app.register_blueprint(cmd_utils)

        # Compile static assets
        from assets import compile_static_assets
        compile_static_assets(assets)


        # @app.cli.command()
        # @click.command('hello')
        # @click.option('--count', default=1, help='Number of greetings.')
        # @click.option('--name', prompt='Your name', help='The person to greet.')
        # @with_appcontext
        # def hello_cmd(count, name):
        #     print(count, name)
        #     # Simple program that greets NAME for a total of COUNT times.
        #     for _ in range(count):
        #         click.echo(f'Hello, {name}!')

        return app