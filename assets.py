from flask import current_app as app
from flask_assets import Bundle

# Create stylesheet bundles

def compile_static_assets(assets):
    assets.auto_build = True
    assets.debug = False

    frontend_bundle = Bundle("frontend/src/css/main.css",output="dist/css/man.css")
    assets.register("frontend_bundle", frontend_bundle)

    # Build assets
    # if app.config["FLASK_ENV"] == "development":
    #     frontend_bundle.build()
    # return assets
    frontend_bundle.build()

