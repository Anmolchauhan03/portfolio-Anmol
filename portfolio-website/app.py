from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dummy admin credentials
ADMIN_USERNAME = 'Anmol Chauhan'
ADMIN_PASSWORD = '213022'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'admin' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))

    resume_uploaded = os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], 'resume.pdf'))

    if request.method == 'POST':
        resume = request.files['resume']
        if resume and resume.filename.endswith('.pdf'):
            resume_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resume.pdf')
            resume.save(resume_path)
            flash('Resume uploaded successfully!', 'success')
            return render_template('dashboard.html', resume_uploaded=True)

    return render_template('dashboard.html', resume_uploaded=resume_uploaded)

@app.route('/resume')
def resume():
    # Serve the resume file from the uploads directory
    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resume.pdf')
    if os.path.exists(resume_path):
        return send_from_directory(app.config['UPLOAD_FOLDER'], 'resume.pdf', as_attachment=True)
    else:
        flash('No resume uploaded yet.', 'danger')
        return redirect(url_for('dashboard'))

@app.route('/delete_resume', methods=['POST'])
def delete_resume():
    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resume.pdf')
    if os.path.exists(resume_path):
        os.remove(resume_path)
        flash('Resume deleted successfully!', 'success')
    else:
        flash('No resume to delete.', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('admin', None)
    flash('You have been logged out!', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
    
    
