from dotenv import load_dotenv
from flask import Flask, jsonify, render_template
from flask_assets import Bundle, Environment

load_dotenv()  # take environment variables
app = Flask(__name__)  # set app

# set assets
assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")

assets.register("css", css)
css.build()

# set routes
@app.route("/")
def main():
    return render_template(
        'base.html',  # from templates folder
        title="Jinja Demo Site",
        content="Smarter page templates with Flask & Jinja."
    )
    # return "Hello World!"

@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask."})

if __name__ == "__main__":
    app.run()