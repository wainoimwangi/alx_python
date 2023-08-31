#!/usr/bin/python3
"""
Script that starts a flask web application
"""
from flask import Flask

# create a flask web application instance
app = Flask(__name__)

# define route for the homepage
@app.route("/", strict_slasher=False)
def hello():
    """
    a function that displays hello hbnb
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    # run the flask developement server
    app.run(host='0.0.0.0', port=5000)
