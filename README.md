# portfolio-Anmol
Resume Upload System
A secure Flask web application for managing resume uploads with authentication. This system allows administrators to upload, download, and manage PDF resumes through a clean web interface.
Features

🔐 Secure admin authentication
📤 PDF resume upload functionality
📥 Resume download capability
🗑️ Resume deletion option
💫 Flash messages for user feedback
🎨 Bootstrap-styled responsive interface
🌐 External accessibility support

Prerequisites

Python 3.x
pip (Python package installer)

Installation

Clone the repository:

bashCopygit clone https://github.com/yourusername/resume-upload-system.git
cd resume-upload-system

Install required packages:

bashCopypip install flask waitress

Create required directories:

bashCopymkdir uploads
Project Structure
Copyresume-upload-system/
├── app.py               # Main application file
├── uploads/            # Directory for storing uploaded resumes
├── templates/          # HTML templates
│   ├── index.html     # Landing page
│   ├── login.html     # Login page
│   └── dashboard.html # Admin dashboard
└── README.md
Configuration
Update the following credentials in app.py before running:
pythonCopyADMIN_USERNAME = 'Anmol Chauhan'
ADMIN_PASSWORD = '213022'
Running the Application

Start the server:

bashCopypython app.py

Access the application:


Local access: http://127.0.0.1:5000
Network access: http://<your-local-ip>:5000
External access: http://<your-public-ip>:5000 (requires port forwarding)

External Access Setup
To make the application accessible from anywhere:

Configure port forwarding on your router for port 5000
Use your public IP address to access the application
Consider setting up HTTPS for secure access

Usage

Navigate to the application URL
Log in using admin credentials
Upload PDF resumes through the dashboard
Download or delete resumes as needed
Log out when finished

Security Features

Session-based authentication
PDF-only file upload restriction
Secure file handling
Production-ready WSGI server (Waitress)

Development
The application uses:

Flask for the web framework
Waitress as the production WSGI server
Bootstrap for frontend styling
Jinja2 for template rendering

Contributing

Fork the repository
Create a new branch for your feature
Commit your changes
Push to your branch
Create a pull request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Author

Anmol Chauhan

Acknowledgments

Flask Documentation
Bootstrap Documentation
Python Community
