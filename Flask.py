# A simple framework for building complex web applications.

# install : pip install Flask

# lightweight WSGI web application framework.
# Designed to make getting started quick and easy, with the ability to scale up to complex applications.
# Simple wrapper around Jinja and has become one of the most popular Python web application framework.
# It is up to the developer to choose the tools and libraries they want to use.
# There are many extensions provided by the community that make adding new functionality easy.

# Examples:
'''
# save this as app.py
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"
'''
'''
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
'''