
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
http://exploreflask.com/en/latest/views.html#custom-decorators
https://flask.palletsprojects.com/en/1.1.x/logging/

Flask uses standard Python logging. 
Messages about your Flask application are logged with app.logger

Fonts:
https://tenpy.readthedocs.io/en/stable/intro/logging.html
https://docs.python-guide.org/writing/logging/
https://stackoverflow.com/questions/46466408/flask-properly-configure-logging
https://stackoverflow.com/questions/68246462/how-could-the-value-of-current-user-be-inserted-into-error-logs-emails-when-usin



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



# Blueprints

Used to organize our application into distinct components.
A blueprint defines a collection of views, templates, static files and other elements that can be applied to an application.

Fonts:
https://hackersandslackers.com/flask-blueprints/
https://hackersandslackers.com/flask-assets/
https://github.com/hackersandslackers/flask-blueprint-tutorial/blob/master/flask_blueprint_tutorial/home/home.py
https://flask.palletsprojects.com/es/latest/patterns/appfactories/



# Templates Jinja2

A Jinja template is simply a text file

https://jinja.palletsprojects.com/en/3.1.x/templates/
https://atufashireen.medium.com/creating-templates-with-jinja-in-python-3ff3b87d6740



# Makefile

JS developers are lucky, their package.json has a special scripts section.
Nothing like this is provided with Python. You can, of course, make a .sh script for each task.
Linux and macOS already have a great task automation tool for any project: Makefile

A task can include multiple steps.
To only print the output, we can prefix each shell script line with a “@”.

We can also use variables within makefiles, usually these would be stored in a separate .env file, we would use add the line include .env in the make code at the top of our makefile.

Fonts:
https://www.saattrupdan.com/2022-08-28-makefu



# Commands

pip3 install -U click

Fonts:
https://flask.palletsprojects.com/en/1.1.x/cli/#registering-commands-with-blueprints
https://click.palletsprojects.com/en/8.1.x/options/



# Error Handler

Fonts:
https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.errorhandler
https://www.digitalocean.com/community/tutorials/how-to-handle-errors-in-a-flask-application



# DebugToolbar

This extension adds a toolbar overlay to Flask applications containing useful information for debugging.

pip install flask-debugtoolbar

Fonts:
https://flask-debugtoolbar.readthedocs.io/en/latest/#installationpip 
https://github.com/ckan/ckan/issues/6995
https://stackoverflow.com/questions/31128764/show-the-sql-generated-by-flask-sqlalchemy




# flake8

Your Tool For Style Guide Enforcement.

pip install flake8

Fonts:
https://flake8.pycqa.org/en/latest/index.html
https://stackoverflow.com/questions/60865887/exclude-env-directory-from-flake8-tests
https://www.flake8rules.com

El podem instal·lar i configurar com a extensió de VSCode.
https://stackoverflow.com/questions/58977983/vs-code-preferences-user-settings-extensions-python-linting-flake8-a

McCabe complexity value
Essential complexity is a measurement developed by Thomas McCabe to determine how well a program is structured. It measures the number of entry points, termination points, and nondeductible nodes. The closer to 1 this value is, the more well structured the program is.



# Black 

By using Black, you agree to cede control over minutiae of hand-formatting. 
In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. 
You will save time and mental energy for more important matters.

Fonts:
https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file
https://stackoverflow.com/questions/73247204/black-not-respecting-extend-exclude-in-pyproject-toml/73296261#73296261



# Middleware

Middlewares are created in Flask by creating a decorator; a function can have multiple middlewares, and the order matters a lot.
A decorator is a function that takes in another function as a parameter and then returns a function.



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


# Marshmallow

It allows you to create serializers to represent your model instances with support to relations and nested objects.

pip install -U marshmallow

Fonts:
https://marshmallow.readthedocs.io/



# WTForms

WTForms is a flexible forms validation and rendering library for Python web development.
Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.

pip install -U Flask-WTF

To enable CSRF protection globally for a Flask app, register the CSRFProtect extension.


Fonts:
https://flask-wtf.readthedocs.io/en/1.1.x/
https://flask-wtf.readthedocs.io/en/1.1.x/csrf/#setup
https://www.geeksforgeeks.org/create-contact-us-using-wtforms-in-flask/



# Flask-CORS

A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.

pip install -U flask-cors

Fonts:
https://flask-cors.corydolphin.com/en/latest/api.html



# User Control Access

pip install Flask-Login

Fonts:
https://github.com/do-community/flask_auth_scotch/blob/master/project/auth.py
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
https://flask-login.readthedocs.io/en/latest/#how-it-works
https://github.com/toddbirchard/flasklogin-tutorial/tree/master/flask_login_tutorial
https://github.com/lingthio/Flask-User/blob/master/flask_user


World timezone definitions, modern and historical:
pip install pytz



# JWT Authentication

Authentication verifies identity (usually through credential validation) while authorization grants or denies permissions to a user.
Authorization is used to verify that a user has permission to do something.

Inside thie decorator function, you check if there is an Authorization field in the headers, if this is missing you return an authorization error.

pip install pyjwt

Fonts:
https://www.loginradius.com/blog/engineering/guest-post/securing-flask-api-with-jwt/
https://www.geeksforgeeks.org/using-jwt-for-user-authentication-in-flask/
https://circleci.com/blog/authentication-decorators-flask/
https://circleci.com/blog/authentication-decorators-flask/
https://4geeks.com/lesson/what-is-JWT-and-how-to-implement-with-Flask



# API Documentation - Flask Swagger

API description formats like the OpenAPI Specification have automated the documentation process, making it easier for teams to generate and maintain them.
Swagger UI allows to visualize and interact with the API’s resources. 
It’s automatically generated from your OpenAPI specification (using docstrings).


Fonts:
https://code.likeagirl.io/swagger-and-postman-build-a-swagger-ui-for-your-python-flask-application-141bb4d0c203
https://diptochakrabarty.medium.com/flask-python-swagger-for-rest-apis-6efdf0100bd7
https://developer.lsst.io/python/numpydoc.html
https://developer.lsst.io/python/numpydoc.html#sections-in-method-and-function-docstring-sections
https://github.com/getsling/flask-swagger/tree/master
https://swagger.io/specification/v2/
https://apitools.dev/swagger-parser/online/
https://github.com/swagger-api/swagger-ui/issues/3229
https://stackoverflow.com/questions/63846280/swagger-ui-requestinterceptor-throws-the-cannot-set-property-x-csrf-token-of
https://flask-wtf.readthedocs.io/en/latest/api.html#flask_wtf.csrf.CSRFProtect.exempt



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



# I11N

pip install Flask-BabelEx
pip install pytz



# Docker Live Reload

--> DOCKER VOLUMES !!!



# Flask-Caching

pip install Flask-Caching


Flask-Limiter



# Gunicorn 

Gunicorn is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model.
It is best to use Gunicorn behind an HTTP proxy server. We strongly advise you to use nginx.

The most basic and the default worker type is a synchronous worker class that handles a single request at a time.
The asynchronous workers available are based on Greenlets (via Eventlet and Gevent). Greenlets are an implementation of cooperative multi-threading for Python.
Gunicorn should only need 4-12 worker processes to handle hundreds or thousands of requests per second.
Generally we recommend (2 x $num_cores) + 1 as the number of workers to start off with.
Always remember, there is such a thing as too many workers. After a point your worker processes will start thrashing system resources decreasing the throughput of the entire system.

pip install gunicorn

You may want to install Eventlet or Gevent if you expect that your application code may need to pause for extended periods of time during request processing. 
Check out the design docs for more information on when you’ll want to consider one of the alternate worker types.

Eventlet is a concurrent networking library for Python that allows you to change how you run your code, not how you write it.
gevent is inspired by eventlet but features a more consistent API, simpler implementation and better performance.



# Mongo

PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python.

pip install pymongo



# Image Processing

The Python Imaging Library adds image processing capabilities to your Python interpreter.
The library contains basic image processing functionality.

pip install --upgrade Pillow


Flask-Session

Flask-SocketIO



# Mail

The Flask-Mail extension provides a simple interface to set up SMTP with your Flask application and to send messages from your views and scripts.

pip3 install Flask-Mail

Fonts:
https://pythonhosted.org/Flask-Mail/