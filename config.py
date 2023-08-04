import os
from os.path import join, dirname
from dotenv import load_dotenv

SECRET_KEY = os.environ.get('SECRET_KEY')

# Database
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_USER = os.environ.get('DATABASE_USER')

# Flask-Mail
MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
MAIL_PORT = os.environ.get('MAIL_PORT') or 25
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or False
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or False
MAIL_DEBUG = os.environ.get('MAIL_DEBUG') or False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or None
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or None
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or  None

# Flask-User
USER_UNAUTHORIZED_ENDPOINT=''

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')