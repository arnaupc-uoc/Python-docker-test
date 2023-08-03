from dotenv import load_dotenv
from flask import Flask
from flask_assets import Bundle, Environment

# Create Flask application
def create_app():

    app = Flask(__name__, instance_relative_config=False)  # set app
    app.config.from_pyfile("./config.py")  # load config

    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our application
        
        # Frontend register
        from frontend.views import mod as front
        app.register_blueprint(front)

        # API register
        from api.views import mod as api
        app.register_blueprint(api)

        # Compile static assets
        from assets import compile_static_assets
        compile_static_assets(assets)

        return app