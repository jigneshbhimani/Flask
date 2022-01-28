# 1.Unique URLs / Redirection Behavior:
# The following two rules differ in their use of a trailing slash.
'''
@app.route('/projects/')
def projects():
    return 'The project page'
@app.route('/about')
def about():
    return 'The about page'
'''


# 2.URL Building:
# To build a URL to a specific function, use the url_for() function.
# It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule.
# Unknown variable parts are appended to the URL as query parameters.

# Why would you want to build URLs using the URL reversing function url_for() instead of hard-coding them into your templates?
# 1.Reversing is often more descriptive than hard-coding the URLs.
# 2.You can change your URLs in one go instead of needing to remember to manually change hard-coded URLs.
# 3.URL building handles escaping of special characters transparently.
# 4.The generated paths are always absolute, avoiding unexpected behavior of relative paths in browsers.
# 5.If your application is placed outside the URL root, for example, in /myapplication instead of /, url_for() properly handles that for you.

# For example, here we use the test_request_context() method to try out url_for(). test_request_context() tells Flask to behave as though it’s handling a request even while we use a Python shell.
'''
from flask import url_for
@app.route('/')
def index():
    return 'index'
@app.route('/login')
def login():
    return 'login'
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
'''
'''
/
/login
/login?next=/
/user/John%20Doe
'''



# 3.HTTP Methods:
# Web applications use different HTTP methods when accessing URLs.
# You should familiarize yourself with the HTTP methods as you work with Flask.
# By default, a route only answers to GET requests.
# You can use the methods argument of the route() decorator to handle different HTTP methods.
'''
from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
'''
# If GET is present, Flask automatically adds support for the HEAD method and handles HEAD requests according to the HTTP RFC.
# Likewise, OPTIONS is automatically implemented for you.