# SDLproject2024
Attendance Merger System
Overview
The Attendance Merger System is a web-based application built using Flask that merges attendance data from multiple Excel sheets. The system accepts two Excel files:

Theory and Lab Attendance
MST and Quiz Attendance
It processes these files and calculates the Final Total Attendance Percentage for each student, then generates a merged final attendance sheet.

Features
Upload two Excel files containing Theory, Lab, MST, and Quiz attendance.
Automatically merges the attendance data based on the Enrollment Number.
Computes the Final Total Attendance Percentage as a combined value of Theory, Lab, MST, and Quiz attendance.
Downloads the merged attendance sheet.
Technologies Used
Backend: Flask (Python)
Frontend: HTML, CSS
Data Processing: Pandas (Python library)
File Handling: Excel files (.xlsx, .xls)
Folder Structure
plaintext
Copy code
├── app.py                    # Main Flask application file
├── merge_excel.py             # Python file for merging Excel sheets and calculating attendance
├── uploads/                   # Folder where uploaded files are temporarily stored
├── templates/
│   └── index.html             # Frontend HTML form for uploading files
├── static/
│   └── style.css              # Styles for the frontend
└── README.md                  # Project README file
Prerequisites
Python 3.x
Required Python libraries: Flask, Pandas, openpyxl
Install these dependencies using pip:
bash
Copy code
pip install flask pandas openpyxl
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo/attendance-merger-system.git
Navigate to the project directory:

bash
Copy code
cd attendance-merger-system
Create uploads directory: Ensure the uploads directory exists for temporary file storage:

bash
Copy code
mkdir uploads
Run the Flask Application: Start the Flask development server:

bash
Copy code
python app.py
Access the Application: Open a web browser and go to:

plaintext
Copy code
http://127.0.0.1:5000
Usage:

Upload two Excel files: one containing Theory and Lab Attendance and another containing MST and Quiz Attendance.
The system will merge the data and calculate the Final Total Attendance Percentage for each student.
The merged file will automatically download.
How it Works
File Upload: The user uploads two files via the HTML form.
Excel Processing: The merge_excel.py script processes the two Excel files. It calculates the total attendance percentage for each student by averaging Theory, Lab, MST, and Quiz attendance.
Final File Generation: The merged attendance file containing the student's Name, Enrollment Number, and Final Total Attendance Percentage is generated and sent for download.
Example
If you upload the following files:

Theory and Lab Attendance.xlsx
MST and Quiz Attendance.xlsx
The application will merge the data and generate a final file with columns:

Name
Enrollment Number
Final Total Attendance Percentage
