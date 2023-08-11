from os import environ as env

FLASK_ENV = env.get("FLASK_ENV") or "development"
FLASK_DEBUG = env.get("FLASK_DEBUG") or 1
FLASK_APP = env.get("FLASK_APP") or "app.py"

SECRET_KEY = env.get("SECRET_KEY")
LANGUAGES = ["ca", "es", "en"]

# Database
DATABASE_PASSWORD = env.get("DATABASE_PASSWORD")
DATABASE_USER = env.get("DATABASE_USER")

# Flask-Mail
MAIL_SERVER = env.get("MAIL_SERVER") or "localhost"
MAIL_PORT = env.get("MAIL_PORT") or 25
MAIL_USE_TLS = env.get("MAIL_USE_TLS") or False
MAIL_USE_SSL = env.get("MAIL_USE_SSL") or False
MAIL_DEBUG = env.get("MAIL_DEBUG") or False
MAIL_USERNAME = env.get("MAIL_USERNAME") or None
MAIL_PASSWORD = env.get("MAIL_PASSWORD") or None
MAIL_DEFAULT_SENDER = env.get("MAIL_DEFAULT_SENDER") or None

# Flask-Caching
CACHE_TYPE = "FileSystemCache"
CACHE_DIR = env.get("CACHE_DIR") or "./.cache"

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = env.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_RECORD_QUERIES = env.get("SQLALCHEMY_DATABASE_URI") or False

# Flask-DebugToolbar
DEBUG_TB_HOSTS = "127.0.0.1"
DEBUG_TB_INTERCEPT_REDIRECTS = False
DEBUG_TB_PROFILER_ENABLED = True
DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True
