#!/usr/bin/python3
""" Hello Flask
    This module holds a script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Method that returns Hello text from a client requests

    Returns:
        [str]: Display “Hello HBNB!”
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
