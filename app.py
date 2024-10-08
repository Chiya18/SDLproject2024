from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename
import os
import pandas as pd
from merge_excel import merge_excel  # Import the merge_excel function from merge_excel.py

app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)  # Create the folder if it doesn't exist
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the allowed file extensions
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')  # Renders index.html from the 'templates' folder

# Route for uploading files
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file1' not in request.files or 'file2' not in request.files:
        return 'No files were uploaded'
    
    file1 = request.files['file1']
    file2 = request.files['file2']
    
    if file1.filename == '' or file2.filename == '':
        return 'No files were uploaded'
    
    if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)
        
        # Save the files
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
        file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
        
        # Use the merge_excel function from merge_excel.py to merge the files
        merged_df = merge_excel(os.path.join(app.config['UPLOAD_FOLDER'], filename1), 
                                os.path.join(app.config['UPLOAD_FOLDER'], filename2))
        
        # Save the merged Excel file
        merged_filename = 'merged_attendance.xlsx'
        merged_filepath = os.path.join(app.config['UPLOAD_FOLDER'], merged_filename)
        merged_df.to_excel(merged_filepath, index=False)
        
        # Return the merged Excel file for download
        return send_file(merged_filepath, as_attachment=True)

    return 'Invalid file type'

if __name__ == '__main__':
    app.run(debug=True)
