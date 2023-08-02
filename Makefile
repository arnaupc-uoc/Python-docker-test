include .env

run:  ## Run app
	@python app.py

reqs:  ## Recreate requirements.txt
	@pipreqs --force

css:  ## Minify css
	@tailwindcss -i ./static/src/main.css -o ./static/dist/main.css --minify

docker: ## Build docker image
    @docker build -t python-docker-test:1.0.0 .