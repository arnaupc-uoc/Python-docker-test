include .env

run:  ## Run app
	@python app.py

reqs:  ## Recreate requirements.txt
	@pipreqs --force

css:  ## Minify css --watch
	@cd frontend && tailwindcss -i ./static/src/css/main.css -o ./static/dist/css/main.css --minify

docker:  ## Build docker image
	@docker build -t python-docker-test:1.0.0 .