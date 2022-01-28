# 1.File Uploads:
# You can handle uploaded files with Flask easily.
# Just make sure not to forget to set the enctype="multipart/form-data" attribute on your HTML form, otherwise the browser will not transmit your files at all.
'''
from flask import request
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...
'''
# If you want to know how the file was named on the client before it was uploaded to your application, you can access the filename attribute.
# However please keep in mind that this value can be forged so never ever trust that value.
# If you want to use the filename of the client to store the file on the server, pass it through the secure_filename() function that Werkzeug provides for you:
'''
from werkzeug.utils import secure_filename
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(f.filename)}")
    ...
'''


