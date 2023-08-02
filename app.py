from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, redirect, url_for, abort
from flask_assets import Bundle, Environment

load_dotenv()  # take environment variables
app = Flask(__name__)  # set app

# set assets
assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")

assets.register("css", css)
css.build()

# Frontend routes
@app.route("/")
def main():
    return render_template(
        'main.html',  # from templates folder
        title="Jinja Demo Site",
        content="Smarter page templates with Flask & Jinja."
    )
    # return "Hello World!"

@app.route("/send-form", methods=["POST"])
def send_form():
    data = request.form.to_dict();
    print("Send Form!")
    return redirect(url_for('main'))
    #return jsonify({"msg": "Form send."})

@app.route("/error")
def error():
    code = 404
    message = 'There\'s an error!'
    abort(code, message)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html'), 404

# API routes

@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask."})

if __name__ == "__main__":
    app.run()