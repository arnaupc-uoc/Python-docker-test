reqs:  ## Recreate requirements.txt
	pipreqs --force

css:  ## Minify css
	tailwindcss -i ./static/src/main.css -o ./static/dist/main.css --minify