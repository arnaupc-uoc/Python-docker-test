include .env

run:  ## Run app
	@python app.py

reqs:  ## Recreate requirements.txt
	@pipreqs --force

css:  ## Minify css
	@tailwindcss -i ./frontend/static/src/main.css -o ./frontend/static/dist/main.css --minify --watch

docker: ## Build docker image
    @docker build -t python-docker-test:1.0.0 .