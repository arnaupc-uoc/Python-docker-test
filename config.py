import os
from os.path import join, dirname
from dotenv import load_dotenv

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_USER = os.environ.get("DATABASE_USER")