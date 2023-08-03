include .env

install:  ## Install dependencies
	@pip3 install -r requirements.txt

run:  ## Run app
	@flask run --port 5000

reqs:  ## Recreate requirements.txt
	@pipreqs --force

test:  ## Run tests
	@python3 -m pytest -v --setup-show --disable-warnings 

css:  ## Minify css --watch
	@cd frontend && tailwindcss -i ./static/src/css/main.css -o ./static/dist/css/main.css --minify

docker:  ## Build docker image
	@docker build -t python-docker-test:1.0.0 .

docker-volume:  ## Build docker volume
	@docker run -dp 5000:5000 -w  -v "$(pwd):" python-docker-test:1.0.0