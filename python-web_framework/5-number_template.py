#!/usr/bin/python3
"""
Script that starts a flask web application
"""
# import flask module
from flask import Flask, render_template
from markupsafe import escape

# create a flask web application instance
app = Flask(__name__)

# define route for the hello_hbnb
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    a function that displays hello hbnb
    """
    return "Hello HBNB!"

# define route for hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    a function that displays hbnb
    """
    return "HBNB"

# define route for c/<text>
@app.route('/c/<text>')
def c(text):
    """
    a function that displays c and replaces "_" with space
    """
    text = text.replace('_', " ")
    return "C {}".format(escape(text))

# define route for python/<text>
@app.route('/python/(<text>)')
@app.route('/python/<text>')
@app.route('/python/')
@app.route('/python')
def python(text='is cool'):
    """
    a function that displays python and replaces "_" with space
    """
    text = text.replace('_', " ")
    return "Python {}".format(text)

# define route for number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    a function that displays n is a number
    """
    return "{} is a number".format(n)

# define route for number_template/<n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    displays a html file when n is an integer
    """
    return render_template('5-number.html' number=n)

if __name__ == '__main__':
    # run the flask developement server
    app.run(host='0.0.0.0', port='5000')
