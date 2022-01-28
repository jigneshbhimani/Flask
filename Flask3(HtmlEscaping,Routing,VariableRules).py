# 1.HTML Escaping:
# When returning HTML (the default response type in Flask), any user-provided values rendered in the output must be escaped to protect from injection attacks.
# HTML templates rendered with Jinja, introduced later, will do this automatically.
# escape(), shown here, can be used manually.
# It is omitted in most examples for brevity, but you should always be aware of how you’re using untrusted data.
'''
from markupsafe import escape
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
'''
# If a user managed to submit the name <script>alert("bad")</script>, escaping causes it to be rendered as text, rather than running the script in the user’s browser.
# <name> in the route captures a value from the URL and passes it to the view function.



# 2.Routing:
# Modern web applications use meaningful URLs to help users.
# Users are more likely to like a page and come back if the page uses a meaningful URL they can remember and use to directly visit a page.
# Use the route() decorator to bind a function to a URL.
'''
@app.route('/')
def index():
    return 'Index Page'
@app.route('/hello')
def hello():
    return 'Hello, World'
'''
# You can make parts of the URL dynamic and attach multiple rules to a function.



# 3.Variable Rules:
# You can add variable sections to a URL by marking sections with <variable_name>.
# Your function then receives the <variable_name> as a keyword argument.
# You can use a converter to specify the type of the argument like <converter:variable_name>.
'''
from markupsafe import escape
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
'''
# Converter types:
# string:(default) accepts any text without a slash
# int:accepts positive integers
# float:accepts positive floating point values
# path:like string but also accepts slashes
# uuid:accepts UUID strings