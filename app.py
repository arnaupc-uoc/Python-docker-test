from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .flaskenv
app = Flask(__name__) # set app

@app.route("/")
def main():
    return "Flask - Hello World!"

@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask."})

if __name__ == "__main__":
    app.run()