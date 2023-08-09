from flask import current_app as app
from flask_assets import Bundle


# Create stylesheet bundles


def compile_static_assets(assets):
    assets.auto_build = True
    assets.debug = False

    frontend_bundle_css = Bundle("frontend/dist/css/main.css", output="css/frontend/main.css")  # folder static in root
    assets.register("frontend_bundle_css", frontend_bundle_css)

    frontend_bundle_js = Bundle("frontend/dist/js/main.js", output="js/frontend/main.js")
    assets.register("frontend_bundle_js", frontend_bundle_js)

    admin_bundle_css = Bundle("admin/dist/css/main.css", output="css/admin/main.css")
    assets.register("admin_bundle_css", admin_bundle_css)

    admin_bundle_js = Bundle("admin/dist/js/main.js", output="js/admin/main.js")
    assets.register("admin_bundle_js", admin_bundle_js)

    # Build assets

    if app.config["FLASK_ENV"] == "development":
        frontend_bundle_css.build()
        frontend_bundle_js.build()

        admin_bundle_css.build()
        admin_bundle_js.build()

    return assets
