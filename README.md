# Python-docker-test
Test Docker container Python Flask App

cd python-docker-test

Before starting to install dependencies, let’s create the Python virtual environment: is used to isolate the installation of the packages, so whenever you try to install anything with pip these new dependencies are added in the lib folder inside venv.
python3 -m venv venv 
source venv/bin/activate 

pip3 install flask
pip3 install python-dotenv

python3 app.py
flask run --host 0.0.0.0 --port 5000 --debug

docker build -t python-docker-test:1.0.0 .


Fonts:
https://www.imaginarycloud.com/blog/flask-python/



# Python Requirements File

While it is possible to create it manually, it is a good practice to use the pipreqs module. It is used to scan your imports and build a Python requirements file for you.

pip3 install pipreqs
pipreqs


