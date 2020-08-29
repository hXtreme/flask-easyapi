from flask import Flask

from flask_easyapi import EasyAPI

app = Flask(__name__)
api = EasyAPI("greet-api", __name__)


@api.route("/simple_greet")
def simple_greet():
    return "Hello, World!"


@api.route("/greet_parameterized")
def greet_parameterized(name: str):
    return f"Hello, {name}!"


@api.route("/custom_greet_parameterized")
def custom_greet_parameterized(greeting: str, name: str):
    return f"{greeting}, {name}!"


@api.route("/greet/<name>")
def greet_name(name: str):
    return f"Hello, {name}!"


@api.route("/custom_greet_mixed/<greeting>")
def custom_greet_mixed_greeting(greeting, name):
    return f"{greeting}, {name}!"


app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
