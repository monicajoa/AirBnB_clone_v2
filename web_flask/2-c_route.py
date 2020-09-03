#!/usr/bin/python3
""" C is fun
    This module holds a script that starts a Flask web application
    web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text> display “C ” followed by the value of the text variable
    using the option strict_slashes=False in your route definition
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


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """ Method that returns “C <text> from a client requests

    Args:
        text ([str]): variable in the url

    Returns:
        [str]: Display “C ” followed by the value of the text variable
    """
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
