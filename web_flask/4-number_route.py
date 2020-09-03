#!/usr/bin/python3
""" Is it a number
    This module holds a script that starts a Flask web application
    web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text> display “C ” followed by the value of the text variable
    /python/(<text>): show “Python”, followed by the value of the text variable
    /number/<n>: display “n is a number” only if n is an integer
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    """ Method that returns python/(<text>) from a client requests

    Args:
        text (str, optional): [text after]. Defaults to 'is cool'.

    Returns:
        [str]: Display “Python ” followed by the value of the text variable
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ Method that returns a number from a client requests

    Args:
        n ([int]): integer to print

    Returns:
        [int]: Display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
