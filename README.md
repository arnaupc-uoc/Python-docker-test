
# WSGI

WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.



# Python-docker-test

Install Python, add route to PATH:
export PATH="$PATH:/Users/arnaupc/Library/Python/3.9/bin"

Create and go to app folder:
cd python-docker-test

Before starting to install dependencies, let’s create the Python virtual environment: is used to isolate the installation of the packages, so whenever you try to install anything with pip these new dependencies are added in the lib folder inside venv.

python3 -m venv venv 
source venv/bin/activate 

Flask is a Micro Framework written in Python, extremely flexible, with low footprint and lightweight:

pip install flask
pip install python-dotenv

python3 app.py
flask run --host 0.0.0.0 --port 5000 --debug

docker build -t python-docker-test:1.0.0 .

Fonts:
https://www.imaginarycloud.com/blog/flask-python/

--> Install all dependencies in virtual environment.



# Python Requirements File

While it is possible to create it manually, it is a good practice to use the pipreqs module. It is used to scan your imports and build a Python requirements file for you.

pip freeze
pip install pipreqs
pipreqs --force -> rewrite 

To install all of the Python modules and packages listed in your requirements.txt file use:
pip install -r requirements.txt
This saves time and effort.

Output a list of outdated packages with:
pip list --outdated

Upgrade the required package with:
pip install -U PackageName

It is also possible to upgrade everything with: 
pip install -U -r requirements.txt

Check for missing dependencies:
python -m pip check

Fonts:
https://learnpython.com/blog/python-requirements-file/



# Templates Jinja2

A Jinja template is simply a text file

https://jinja.palletsprojects.com/en/3.1.x/templates/
https://atufashireen.medium.com/creating-templates-with-jinja-in-python-3ff3b87d6740



# Set up Tailwind CSS with Flowbite inside a Flask project 

Make sure that you have both Node.js and Python installed on your local machine.

Flask-Assets helps you to integrate webassets into your Flask application:
pip install Flask-Assets

Tailwind CSS is notoriously dependent on Node.js, this dependency may not be welcome in your Docker container.
Python package pytailwindcss lets you install the Tailwind CSS executable via pip, it runs a standalone Tailwind CSS build that doesn’t require Node.js to be installed:

pip install pytailwindcss
tailwindcss init
tailwindcss -i ./static/src/main.css -o ./static/dist/main.css --minify

Fonts:
https://testdriven.io/blog/flask-htmx-tailwind/
https://flowbite.com/docs/getting-started/flask/
https://timonweb.com/python/you-can-now-use-pip-to-install-tailwind-css-nodejs-is-no-longer-required/
https://byby.dev/at-rule-tailwind



# Makefile

JS developers are lucky, their package.json has a special scripts section.
Nothing like this is provided with Python. You can, of course, make a .sh script for each task.
Linux and macOS already have a great task automation tool for any project: Makefile

A task can include multiple steps.
To only print the output, we can prefix each shell script line with a “@”.

We can also use variables within makefiles, usually these would be stored in a separate .env file, we would use add the line include .env in the make code at the top of our makefile.

Fonts:
https://www.saattrupdan.com/2022-08-28-makefu



# Mail

The Flask-Mail extension provides a simple interface to set up SMTP with your Flask application and to send messages from your views and scripts.

pip3 install Flask-Mail

Fonts:
https://pythonhosted.org/Flask-Mail/



# Commands

pip3 install -U click

Fonts:
https://flask.palletsprojects.com/en/1.1.x/cli/#registering-commands-with-blueprints
https://click.palletsprojects.com/en/8.1.x/options/



# User Control Access

Flask-User is a Customizable User Authentication, User Management, and more.

pip install Flask-User
pip install email_validator

World timezone definitions, modern and historical:
pip install pytz

Fonts:
https://flask-user.readthedocs.io/en/latest/authorization.html



# Blueprints

Used to organize our application into distinct components.
A blueprint defines a collection of views, templates, static files and other elements that can be applied to an application.

Fonts:
https://hackersandslackers.com/flask-blueprints/
https://hackersandslackers.com/flask-assets/
https://github.com/hackersandslackers/flask-blueprint-tutorial/blob/master/flask_blueprint_tutorial/home/home.py
https://flask.palletsprojects.com/es/latest/patterns/appfactories/



# Middleware



# Tests

In general, testing helps ensure that your app will work as expected for your end users.

The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing. 
pytest will recursively search through your project structure to find the Python files that start with test_*.py
pytest supports running Python unittest-based tests out of the box.

pip3 install pytest

To run the tests:
python3 -m pytest -v --setup-show

If you only want to run a specific type of test:
python3 -m pytest tests/functional/

When developing tests, it's nice to get an understanding of how much of the source code is actually tested (code coverage).
python3 -m pytest --cov=project

Fonts:
https://testdriven.io/blog/flask-pytest/
https://flask.palletsprojects.com/en/2.3.x/testing/

--> In Python you should add self as the first parameter to all defined methods in classes.
--> Python Ternary Operator: x = a if condition else b
--> Python Null-coalescing Operator (Elvis Operator): other = s or "some default value"



# I11N

pip install Flask-BabelEx
pip install pytz



# Docker Live Reload

--> DOCKER VOLUMES !!!



# Flask RESTfull

--> Swagger Annotations



# Flask SQLAlchemy

Flask-SQLAlchemy simplifies using SQLAlchemy by automatically handling creating, using, and cleaning up the SQLAlchemy objects you’d normally work with. 

pip install -U Flask-SQLAlchemy

Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. The database operations are made available through the Flask command-line interface.

pip install Flask-Migrate
pip install pymysql

Create a migration repository with the following command:
flask db init

You can then generate an initial migration:
flask db migrate -m "Initial migration."

Then you can apply the changes described by the migration script to your database:
flask db upgrade

Each time the database models change, repeat the migrate and upgrade commands.
To sync the database in another system just refresh the migrations folder from source control and run the upgrade command.

Fonts:
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/
https://flask-migrate.readthedocs.io/en/latest/
https://cmmorrow.medium.com/using-sqlalchemy-and-flask-to-build-a-simple-data-driven-web-app-17e2d43778bb
https://www.digitalocean.com/community/tutorials/https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
https://docs.sqlalchemy.org/en/20/orm/session_basics.html


--> 'flask_user.user_manager' has no attribute 'hash_password'

--> relationship 'UserEmail.user' will copy column users.id to column user_emails.user_id, which conflicts with relationship(s): 'User.user_emails' (copies users.id to user_emails.user_id). If this is not the intention, consider if these relationships should be linked with back_populates


# WTForms

pip install -U Flask-WTF

# Gunicorn 



