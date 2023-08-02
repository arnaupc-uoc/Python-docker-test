include .env

run:  ## Run app
	@flask run

reqs:  ## Recreate requirements.txt
	@pipreqs --force

css:  ## Minify css --watch
	@cd frontend && tailwindcss -i ./static/src/css/main.css -o ./static/dist/css/main.css --minify

docker:  ## Build docker image
	@docker build -t python-docker-test:1.0.0 .

docker-dev:  ## Build docker image
	@docker run -dp 5000:5000 -w  -v "$(pwd):" python-docker-test:1.0.0