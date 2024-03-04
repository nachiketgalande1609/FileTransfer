import socket
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import MultipleFileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import zipfile

# Create a Flask app instance
app = Flask(__name__)
# Set a secret key for the app for security purposes
app.config['SECRET_KEY'] = 'supersecretkey'
# Set the folder where uploaded files will be stored
app.config['UPLOAD_FOLDER'] = 'downloads'

# Get the local IP address of the machine
ip_address = socket.gethostbyname(socket.gethostname())

# Define a form for uploading multiple files
class UploadFileForm(FlaskForm):
    files = MultipleFileField("Files", validators=[InputRequired()])
    submit = SubmitField("Upload Files")

# Define a route for the home page where file upload will happen
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        files = form.files.data  # Grab the list of files

        # Create a unique name for the zip file
        zip_filename = secure_filename("uploaded_files.zip")
        zip_path = os.path.join(app.config['UPLOAD_FOLDER'], zip_filename)

        # Create a zip file and add each uploaded file to it
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            for file in files:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(file_path)
                zip_file.write(file_path, secure_filename(file.filename))
                os.remove(file_path)  # Remove individual file after adding it to the zip

        return render_template('index.html', form=form, message="Files have been uploaded")

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host=ip_address, port=5000)
