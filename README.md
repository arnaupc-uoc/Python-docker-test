# Python-docker-test
Test Docker container Python Flask App

cd python-docker-test

create the Python virtual environment and then activate the environment.
python3 -m venv venv 
source venv/bin/activate 

pip3 install flask

python3 app.py
flask run --host 0.0.0.0 --port 5000 

docker build -t python-docker-test:1.0.0 .