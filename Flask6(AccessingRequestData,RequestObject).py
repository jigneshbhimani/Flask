# 1.Accessing Request Data:
'''
from flask import request
with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
'''
# The other possibility is passing a whole WSGI environment to the request_context() method:
'''
with app.request_context(environ):
    assert request.method == 'POST'
'''



# 2.Request Object:
# The request object is documented in the API section and we will not cover it here in detail (see Request).
# Here is a broad overview of some of the most common operations.
# First of all you have to import it from the flask module:
'''
from flask import request
'''
# The current request method is available by using the method attribute.
# To access form data (data transmitted in a POST or PUT request) you can use the form attribute.
# Here is a full example of the two attributes mentioned above:
'''
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
'''
# What happens if the key does not exist in the form attribute? In that case a special KeyError is raised.
# You can catch it like a standard KeyError but if you don’t do that, a HTTP 400 Bad Request error page is shown instead.
# So for many situations you don’t have to deal with that problem.
# To access parameters submitted in the URL (?key=value) you can use the args attribute:
'''
searchword = request.args.get('key', '')
'''