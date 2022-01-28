# 1.Static Files:
# Dynamic web applications also need static files. That’s usually where the CSS and JavaScript files are coming from. Ideally your web server is configured to serve them for you, but during development Flask can do that as well.
# Just create a folder called static in your package or next to your module and it will be available at /static on the application.
# To generate URLs for static files, use the special 'static' endpoint name:
'''
url_for('static', filename='style.css')
'''
# The file has to be stored on the filesystem as static/style.css.



# 2.Rendering Templates:
# Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the HTML escaping on your own to keep the application secure.
# Because of that Flask configures the Jinja2 template engine for you automatically.
# To render a template you can use the render_template() method.
# All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.
# Here’s a simple example of how to render a template:
'''
from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
'''
# Case 1: a module:
'''
/application.py
/templates
    /hello.html
'''
# Case 2: a package:
'''
/application
    /__init__.py
    /templates
        /hello.html
'''
# For templates you can use the full power of Jinja2 templates.
'''
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
'''

