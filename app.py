"""Flask App Demo."""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """Homepage."""
    return "Home page"
