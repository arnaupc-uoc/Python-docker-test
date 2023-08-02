from flask import current_app as app
from flask_assets import Bundle

# Create stylesheet bundles

def compile_static_assets(assets):
    assets.auto_build = True
    assets.debug = False

    frontend_bundle_css = Bundle("frontend/dist/css/main.css",output="css/main.css")
    assets.register("frontend_bundle_css", frontend_bundle_css)

    # Build assets
    # if app.config["FLASK_ENV"] == "development":
    #     frontend_bundle.build()
    # return assets
    frontend_bundle_css.build()

