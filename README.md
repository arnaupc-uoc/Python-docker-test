
# Python-docker-test

Test Docker container Python Flask App

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



# Blueprints

Used to organize our application into distinct components.
A blueprint defines a collection of views, templates, static files and other elements that can be applied to an application.

https://hackersandslackers.com/flask-blueprints/
https://hackersandslackers.com/flask-assets/
https://github.com/hackersandslackers/flask-blueprint-tutorial/blob/master/flask_blueprint_tutorial/home/home.py


# Docker Live Reload


# WSGI

WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.



