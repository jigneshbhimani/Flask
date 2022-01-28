# 1.Cookies:
# To access cookies you can use the cookies attribute.
# To set cookies you can use the set_cookie method of response objects.
# The cookies attribute of request objects is a dictionary with all the cookies the client transmits.
# If you want to use sessions, do not use the cookies directly but instead use the Sessions in Flask that add some security on top of cookies for you.

# How to read cookies:
'''
from flask import request
@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
'''

# How to store cookies:
'''
from flask import make_response
@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
'''




# 2.Sessions:
# Which allows you to store information specific to a user from one request to the next.
# This is implemented on top of cookies for you and signs the cookies cryptographically.

# How to work session:

# from flask import session
# Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# @app.route('/')
# def index():
#     if 'username' in session:
#         return f'Logged in as {session["username"]}'
#     return 'You are not logged in'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
    # return '''
        # <form method="post">
        #     <p><input type=text name=username>
        #     <p><input type=submit value=Login>
        # </form>
    # '''

# @app.route('/logout')
# def logout():
    # remove the username from the session if it's there
    # session.pop('username', None)
    # return redirect(url_for('index'))




# 3.API with JSON:
# A common response format when writing an API is JSON.
# It’s easy to get started writing such an API with Flask.
# If you return a dict from a view, it will be converted to a JSON response.
'''
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }
'''
# Depending on your API design, you may want to create JSON responses for types other than dict. In that case, use the jsonify() function, which will serialize any supported JSON data type.
'''
from flask import jsonify
@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])
'''