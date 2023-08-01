
# Python-docker-test

Test Docker container Python Flask App

cd python-docker-test

Before starting to install dependencies, let’s create the Python virtual environment: is used to isolate the installation of the packages, so whenever you try to install anything with pip these new dependencies are added in the lib folder inside venv.
python3 -m venv venv 
source venv/bin/activate 

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