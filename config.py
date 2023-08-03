import os
from os.path import join, dirname
from dotenv import load_dotenv

SECRET_KEY = os.environ.get('SECRET_KEY')

# Database
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_USER = os.environ.get('DATABASE_USER')

# Flask-Mail
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_DEBUG = False
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = None