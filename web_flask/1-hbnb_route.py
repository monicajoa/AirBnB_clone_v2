#!/usr/bin/python3
""" HBNB
    This module holds a script that starts a Flask web application
    web application must be listening on 0.0.0.0, port 5000
    Routes: /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    using the option strict_slashes=False in the route definition
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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Method that returns HBNB text from a client requests

    Returns:
        [str]: Display “HBNB”
    """
    return "HBNB"


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
